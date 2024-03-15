'''
Class definitions
Input       - Query + Context for LLMs
Output      - Formatted output for post processing

Provides multiple options for LLM operations
Runs LLM operations and provides formatted output for post processing

'''
from backend.llm_ops import openai
import json

class LLM_Ops():

    def __init__(self, keychain, testing) -> None:
        self.keychain       = keychain
        self.testing        = testing
        
        return None
    
    def pick_llm(self):
        pass

    def get_response_from_openai() -> dict:
        pass

    # def get_response_from_other_llm():
    #   pass

    def get_llm_response(self, query, context) -> dict():

        gpt_caller = openai.GPTHandler(self.keychain, self.testing)
        response_from_llm = gpt_caller.get_response_from_gpt(query, context)

        #test_response_from_llm = "{'test_key': 'test_value'}"
        
        return response_from_llm