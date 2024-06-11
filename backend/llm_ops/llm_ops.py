'''
Class definitions
Input       - Query + Context for LLMs
Output      - Formatted output for post processing

Provides multiple options for LLM operations
Runs LLM operations and provides formatted output for post processing

'''
from backend.llm_ops import openai
from utils.write_files import write_json_to_file

class LLM_Ops():

    def __init__(self, keychain, testing, test_timestamp) -> None:
        self.keychain       = keychain
        self.testing        = testing
        self.test_timestamp = test_timestamp

        
        return None
    
    def pick_llm(self):
        pass

    def get_response_from_openai() -> dict:
        pass

    def get_response_from_other_llm():
       pass

    def get_llm_response(self, query, context) -> dict():

        gpt_caller = openai.GPTHandler(self.keychain, self.testing, self.test_timestamp)
        response_from_llm = gpt_caller.get_response_from_gpt(query, context)

        if self.testing:
            filename = "test_data/test_"+self.test_timestamp+"/llm_response_test.json"
            data_to_write = response_from_llm
            write_json_to_file(filename, data_to_write)
        
        #test_response_from_llm = "{'test_key': 'test_value'}"
        
        return response_from_llm