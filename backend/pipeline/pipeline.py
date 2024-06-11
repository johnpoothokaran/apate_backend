'''
Runs pipeline end to end
Input   - Query from client
Output  - JSON response for client

Handles the keychain object and provides it to different class objects

'''

from utils import get_keys
from backend.preprocess import preprocess
from backend.llm_ops import llm_ops
from datetime import datetime


class Pipeline():

    def __init__(self, testing = False):
        
        #self.query = None
        #self.response = None
        self.keychain = get_keys.read_keys_from_json()
        self.testing = testing
        if self.testing:
            self.test_timestamp         = str(datetime.today())[:16]
        else:
            self.test_timestamp         = None
        print('Successful creation of Pipeline object')
        
    
    def run_pipeline(self, query: str):
        
        print('\nUSER QUERY:',query)
        
        #print('\n',self.keychain,'\n')

        # runs preprocess functions
        context_collector = preprocess.Preprocess(self.keychain, self.testing, self.test_timestamp)
        context_collected = context_collector.get_context_for_gpt(query)

        print('CONTEXT COLLECTED') # String collection of all relevant information

        # runs LLM ops functions
        print('LLM TIME')
        print('QUERY length:', len(query))
        print('CONTEXT length:',len(context_collected))

        llm_operator = llm_ops.LLM_Ops(self.keychain, self.testing, self.test_timestamp)
        llm_response = llm_operator.get_llm_response(query, context_collected)

        #print('LLM Response:', type(llm_response),llm_response)

        # runs postprocess functions
        
        print('See you next time...\n\n')

        return llm_response
