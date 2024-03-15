'''
Class definition for Open AI/ChatGPT functionality
'''

import json
import openai
from openai import OpenAI

class GPTHandler():

    def __init__(self, keychain, testing = False) -> None:
        self.keychain       = keychain
        self.testing        = testing

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

        system_message = '''
        You are an assistant who helps users identify truth, lies, and misinformation.
        You will be given the QUERY
        You will be given a fixed CONTEXT. You will not use any prior knowledge.

        The context may contain information obtained from several different APIs - including google search, social media etc.
        Your response will be any one of the following 3 options in response to the QUERY
        1 - TRUE
        2 - FALSE
        3 - UNCLEAR

        For options 1 and 2, you will provide a one line explanation with the necessary information summarized from the context
        For option 3, you will provide reasoning for the lack of clarity and suggest how to get more information to the user
        In all 3 cases, you will name the most reliable sources from the provided context.

        The response will be formatted as Python dictionary object, with these labels:
        {
            "STATEMENT" : "Input claim, NOT the name of the claim variable",
            "LABEL" : "TRUE, FALSE, or UNCLEAR",
            "EXPLANATION" : "One line explanation",
            "SOURCES" : "List of most reliable sources from the provided context used to support label and explanation"
        }
        '''



        query = 'QUERY:'+query+'\n'
        context = 'CONTEXT'+context+'\n'
        user_message = query+context


        messages.append(self.get_system_message(system_message))
        messages.append(self.get_user_message(user_message))
        return messages


    def get_response_from_gpt(self, query, context):

        '''
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
    