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


def run_all_tests():
    pipeline_test()
    return None

def main():
    run_all_tests()
    return None

if __name__ == "__main__":
    main()
