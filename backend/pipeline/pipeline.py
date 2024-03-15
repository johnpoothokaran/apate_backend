'''
Runs pipeline end to end
Input   - Query from client
Output  - JSON response for client

Handles the keychain object and provides it to different class objects

'''

from utils import get_keys
from backend.preprocess import preprocess


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
        context_collection = preprocess.Preprocess(self.keychain, self.testing)
        context_collected = context_collection.get_context_for_gpt(query)

        print('CONTEXT COLLECTED:',type(context_collected)) # Dictionary object with search result fields

        # runs LLM ops functions


        # runs postprocess functions

        response = 'Maybe next time...\n\n'
        print('RESPONSE:',response)
