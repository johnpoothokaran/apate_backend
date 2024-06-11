'''
Runs the test scripts for Project Apate

Testing regime
    End to end test     - Full pipeline
    Key test            - for API keys
    Response test       - small dataset
    Response test       - big dataset
    Consistency test    - same query n times
'''

from tests.pipeline_test import pipeline_test
from tests.preprocess_test import scrape_test, gsearch_test

def run_all_tests():
    scrape_test()
    pipeline_test(debug =False) # debug default is True which limits the run to 3 claims
    return None

def run_gsearch_test():
    # To be completed
    gsearch_test()
    return None

def run_scrape_test():
    scrape_test()
    return None

def main():

    # Run to do a full set of tests that check each subsystem and fully integrated system
    run_all_tests()

    # Run to check the scrape of a single page
    # run_scrape_test()

    # Run to test a single link to search on google and return the context_for_gpt that is provided to the LLM
    #run_gsearch_test()

    print('END TESTS\n\n\n')
    return None

if __name__ == "__main__":
    main()

'''
Current work:
- Parsing webpage for context for LLM
    - Files of focus - parse_page.py

Next steps:
- 
- 

'''