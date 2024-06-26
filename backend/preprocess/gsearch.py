'''
Class defintion of Google search and parsing functionality

'''

import requests
import json
from bs4 import BeautifulSoup
import requests
from backend.preprocess.parse_page import parse_webpage

class GSearch():

    def __init__(self, keychain, testing, top_n, test_timestamp) -> None:
        
        self.top_n_google_searches      = top_n
        self.keychain                   = keychain
        self.testing                    = testing
        self.context_limiter            = 40000
        self.test_timestamp             = test_timestamp

        return None
    

    def explore_search_result_top_n(self, data) -> None:
        # Not called in normal runtime
        # Looking at data in search results (data = results)
        # Print some of the result metadata and the top 3 Search links found
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
    
    def run_google_searches(self, claim, additional_info = '') -> dict:

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
    
    def extract_webpage_text_from_link(self, result_link):
        parsed_result = parse_webpage(result_link)
        return parsed_result
    
    def extract_search_items_for_context(self, this_item) -> str:

        context_from_this_item = ''

        error_count = 0
        try:
            page_text = self.extract_webpage_text_from_link(this_item['link'])
            context_from_this_item += 'LINK: '+ this_item['link']
            context_from_this_item += '\n'
            context_from_this_item += 'PAGE EXTRACT: ' + page_text
            context_from_this_item += '\n'
        except KeyError:
            error_count+=1
        
        try:
            context_from_this_item += 'HTML TITLE: '+ this_item['htmlTitle']
            context_from_this_item += '\n'
        except KeyError:
            error_count+=1

        try:
            context_from_this_item += 'SNIPPET: ' +this_item['snippet']
            context_from_this_item += '\n'
        except KeyError:
            error_count+=1

        try:
            context_from_this_item += 'HTML SNIPPET: ' +this_item['htmlSnippet']
            context_from_this_item += '\n'
        except KeyError:
            error_count+=1

        #context_from_this_item += 'PAGEMAP: ' +json.dumps(this_item['pagemap'])
        #context_from_this_item += '\n'
       
        if error_count == 4:
            print("None of the keys are accessible.")
        else:
            if error_count >5:
                print('Some keys are inaccessible:', error_count)

        #print(context_from_this_item)
        return context_from_this_item

    
    def basic_parse_google_search_results(self, data) -> str:
        '''
        Runs basic parse of google search results
        '''
        #print('DATA:',type(data))
        #print('DATA:',data.keys())
        #print(data['error'])

        context_for_gpt = ''

        if 'error' in data.keys():
            print('\n\n\nGOOGLE SEARCH ERROR\n\n\n')
            print(data['error'])
        print('LENGTH OF GOOGLE RESPONSE',len(data['items']))
        print('Exploring Top ',min(self.top_n_google_searches,len(data['items'])),' Search Links:')
        for i in range(min(self.top_n_google_searches,len(data['items']))):
            #print('RESULT:',i)
            context_for_gpt += '\n\nSEARCH RESULT '+str(i+1)+':\n'
            
            this_item = data['items'][i]
            context_from_item = self.extract_search_items_for_context(this_item)
            context_for_gpt += context_from_item

        return context_for_gpt
    


    def extract_context_from_google_search_results(self, 
                                                   data, 
                                                   mode = basic_parse_google_search_results) -> str:
        
        '''
        Runs multiple extractions of data from google search results
        '''
        
        combined_items_from_search_results = ''
        
        context_for_gpt = mode(self, data)
        combined_items_from_search_results += context_for_gpt

        # Placeholder for additional parse steps

        context_for_gpt = combined_items_from_search_results

        return context_for_gpt[:self.context_limiter]

    
