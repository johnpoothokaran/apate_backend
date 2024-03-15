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
from backend.preprocess import gsearch

class Preprocess():

    def __init__(self, keychain, testing = False) -> None:
        self.context_all                = None
        self.context_google_search      = None
        self.data_google                = None
        self.keychain                   = keychain
        self.testing                    = testing
        self.top_n_google_searches      = 10

    
    
    def get_gsearch_context_for_gpt(self, claim, additional_info = '') -> str:

        # create gsearch class object
        gsearcher = gsearch.GSearch(self.keychain,
                                    self.testing,
                                    self.top_n_google_searches)

        data_google = gsearcher.run_google_searches(claim, additional_info)

        if self.testing:
            filename = "test_data/test_"+str(datetime.today())[:19]+"/gdata_test.json"
            data_to_write = data_google
            write_json_to_file(filename, data_to_write)
        
        context_for_gpt = gsearcher.extract_context_from_google_search_results(data_google)

        if self.testing:
            filename = "test_data/test_"+str(datetime.today())[:19]+"/gcontext_for_gpt.txt"
            data_to_write = context_for_gpt
            write_text_to_file(filename, data_to_write)

        return context_for_gpt
    
    def get_context_for_gpt(self, claim, additional_info = '') -> str:

        context = ''
        context += self.get_gsearch_context_for_gpt(claim, additional_info)
        
        return context
