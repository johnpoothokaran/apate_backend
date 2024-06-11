'''
Class definition for Open AI/ChatGPT functionality
'''

import json
import openai
from openai import OpenAI
from utils.read_files import read_text_from_file

class GPTHandler():

    def __init__(self, keychain, testing = False, test_timestamp = None) -> None:
        self.keychain       = keychain
        self.testing        = testing
        self.test_timestamp = test_timestamp

        self.max_tokens     = None
        self.model_type     = None
        pass

    def set_gpt_params(self, 
                       max_tokens = 100, 
                       model_type = 'gpt-3.5-turbo'):
        
        self.max_tokens     = max_tokens
        self.model_type     = model_type
        return None

    def get_system_message(self,message):
        system_message = {
            'role':'system',
            'content':message
        }
        return system_message

    def get_user_message(self,message):
        user_message = {
            'role':'user',
            'content':message
        }
        return user_message

    

    # Basic test messages to make sure OpenAI API calls are working
    def get_hello_world_messages(self):
        messages = []
        messages.append(self.get_system_message('You are a test assistant. Do your best'))
        messages.append(self.get_user_message('This is a hello world test. You know what to do'))
        return messages

    
    """
    Takes in a query that can be true, false, or unclear
    Returns a formatted input message for a LLM that instructs the model
    to only use a fixed context when evalulating the query
    """
    def get_verify_messages(self, query, context):
        
        messages = []
        system_message = read_text_from_file('prompts/system_message_v0.txt')
        if system_message is None:
            print('PROBLEM: PROMPT NOT FOUND')

        query = 'QUERY:'+query+'\n'
        context = 'CONTEXT'+context+'\n'
        user_message = query+context

        messages.append(self.get_system_message(system_message))
        messages.append(self.get_user_message(user_message))
        return messages


    def get_response_from_gpt(self, query, context):

        '''
        INPUT: Query (string) and Context (string)
        OUTPUT: 
        Takes in a query and context (e.g. Google search results)
        Returns GPT response categorizing query as true, false, or unclear based on context
        '''
        
        # gpt_url = "https://api.openai.com/v1/completions"
        openai_api_key = self.keychain['openai_api_key']
        openai_org_key = self.keychain['openai_org_key']

        client = OpenAI(api_key=openai_api_key)

        # Model Parameters
        self.set_gpt_params()

        #messages = get_hello_world_messages()
        messages = self.get_verify_messages(query, context)

        # Make API Request
        response = client.chat.completions.create(model=self.model_type,
                                                    messages=messages)

        gpt_response = response.choices[0].message.content
        #print('Response:', gpt_response)

        response = gpt_response
        print('GPT RESPONSE:',len(response))
        print(response)
        response_from_llm = json.loads(response)

        return response_from_llm
    