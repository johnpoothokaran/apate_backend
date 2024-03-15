'''
Class definition - preprocess
Input   - Query from client
Output  - Context for LLM

Collects information based on the query
Pre processes the collected information
Provides necessary context for LLMs to process

'''
import json
import requests
from datetime import datetime

class Preprocess():

    def __init__(self, keychain, testing = False):
        self.context_all                = None
        self.context_google_search      = None
        self.data_google                = None
        self.keychain                   = keychain
        self.testing                    = testing

    
    def write_search_result_json_to_file(self):

        today = datetime.today()
        filename = "test_data/data_google_test_"+str(today)[:19]+".json"
        with open(filename, "w") as json_file:
            json.dump(self.data_google, json_file, indent=4)

        return None
    
    def run_google_searches(self, claim, additional_info = ''):

        '''
        Function to get google search results for a query
        Input: search query
        Output: json (dict) object with results

        Needs google search API key and Search engine ID from keychain
        '''

        search_url = 'https://customsearch.googleapis.com/customsearch/v1'
        # search_url_2 = 'https://www.googleapis.com/customsearch/v1?[parameters]'

        google_search_api_key = self.keychain['google_search_api_key']
        search_engine_id = self.keychain['google_search_engine_id']
        search_params = dict()

        # API key
        search_params['key'] = google_search_api_key

        # Programmable search engine ID - from John
        search_params['cx'] = search_engine_id

        # Query to search
        self.query = claim + additional_info
        search_params['q'] = self.query

        results = requests.get(url=search_url,
                               params=search_params)

        data = results.json()

        self.data_google = data
        if self.testing:
            self.write_search_result_json_to_file()

        #print('Results:', results)
        return data

