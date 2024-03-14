'''
Project Apate: 
Verifying online information and protecting against misinformation

Runs the backend processes
    Takes in query and returns the response
Manages the API

'''

from utils import get_keys
from backend.pipeline import pipeline
#from pipeline import Pipeline

def main():

    test_run = pipeline.Pipeline()
    test_run.run_pipeline("I'm the test query")

    return None

if __name__ == "__main__":
    main()
