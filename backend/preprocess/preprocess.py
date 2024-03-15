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
from utils.write_files import write_text_to_file, write_json_to_file
from datetime import datetime

class Preprocess():

    def __init__(self, keychain, testing = False):
        self.context_all                = None
        self.context_google_search      = None
        self.data_google                = None
        self.keychain                   = keychain
        self.testing                    = testing
        self.top_n_google_searches      = 3

    
    def explore_search_result_top_n(self):
        # Looking at data in search results (data = results)
        # Print some of the result metadata and the top 3 Search links found

        data = self.data_google
        print(data.keys())
        print('Kind',data['kind'])
        print('url',data['url'])
        print('Queries',data['queries'])
        print('Context',data['context'])
        print('Search Information',data['searchInformation'])
        print('Items',data['items'][0])

        print('\nKeys for items:')
        print(data['items'][0].keys())
        print('\n')
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

        data_google = results.json()
        
        return data_google
    
    def extract_context_from_google_search_results(self, data):
        
        context_for_gpt = ''
        top_n = self.top_n_google_searches

        print('Exploring Top '+str(top_n)+' Search Links:')
        for i in range(top_n):

            context_from_this_item = '\n\nSEARCH RESULT ' +str(i+1)+'\n'

            this_item = data['items'][i]
            #print('\nKIND',this_item['kind']) # Do not include
            #print('\nPAGEMAP', type(this_item['pagemap']))
            #display(this_item['pagemap'])
            #print(this_item['pagemap'].keys())

            context_from_this_item += 'LINK: '+ this_item['link']
            context_from_this_item += '\n'

            context_from_this_item += 'HTML TITLE: '+ this_item['htmlTitle']
            context_from_this_item += '\n'

            context_from_this_item += 'SNIPPET: ' +this_item['snippet']
            context_from_this_item += '\n'

            context_from_this_item += 'HTML SNIPPET: ' +this_item['htmlSnippet']
            context_from_this_item += '\n'

            context_from_this_item += 'PAGEMAP: ' +json.dumps(this_item['pagemap'])
            context_from_this_item += '\n'
            #print(context_from_this_item)
        print('Exploration done!\n')

        context_for_gpt += context_from_this_item
        return context_for_gpt

    
    def get_context_for_gpt(self, claim, additional_info = ''):

        top_n = self.top_n_google_searches

        data_google = self.run_google_searches(claim, additional_info)


        if self.testing:
            filename = "test_data/test_"+str(datetime.today())[:19]+"/data_google_test.json"
            data_to_write = data_google
            write_json_to_file(filename, data_to_write)
        
        gsearch_context_for_gpt = self.extract_context_from_google_search_results(data_google)

        if self.testing:
            filename = "test_data/test_"+str(datetime.today())[:19]+"/context_for_gpt.txt"
            data_to_write = gsearch_context_for_gpt
            write_text_to_file(filename, data_to_write)

        return gsearch_context_for_gpt
