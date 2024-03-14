'''
Runs pipeline end to end
Input   - Query from client
Output  - JSON response for client


'''

from utils import get_keys


class Pipeline():

    def __init__(self):
        
        #self.query = None
        #self.response = None
        self.keychain = get_keys.read_keys_from_json()
        print('Successful creation of Pipeline object')
        
    
    def run_pipeline(self, query: str):
        
        print('\nUSER QUERY:',query)
        
        #print('\n',self.keychain,'\n')

        # runs preprocess functions

        # runs LLM ops functions

        # runs postprocess functions

        response = 'Maybe next time...\n\n'
        print('RESPONSE:',response)
