'''
Runs pipeline end to end
Input   - Query from client
Output  - JSON response for client

Handles the keychain object and provides it to different class objects

'''

from utils import get_keys
from backend.preprocess import preprocess
from backend.llm_ops import llm_ops


class Pipeline():

    def __init__(self, testing = False):
        
        #self.query = None
        #self.response = None
        self.keychain = get_keys.read_keys_from_json()
        self.testing = testing
        print('Successful creation of Pipeline object')
        
    
    def run_pipeline(self, query: str):
        
        print('\nUSER QUERY:',query)
        
        #print('\n',self.keychain,'\n')

        # runs preprocess functions
        context_collector = preprocess.Preprocess(self.keychain, self.testing)
        context_collected = context_collector.get_context_for_gpt(query)

        print('CONTEXT COLLECTED:',type(context_collected)) # Dictionary object with search result fields


        # runs LLM ops functions
        print('LLM TIME')
        print('QUERY length:', len(query))
        print('CONTEXT length:',len(context_collected))

        llm_operator = llm_ops.LLM_Ops(self.keychain, self.testing)
        llm_response = llm_operator.get_llm_response(query, context_collected)

        print('LLM Response:', type(llm_response),llm_response)

        # runs postprocess functions
        print('FINAL RESPONSE:', llm_response)
        response = 'See you next time...\n\n'
        print(response)
