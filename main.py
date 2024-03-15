'''
Project Apate: 
Verifying online information and protecting against misinformation

Runs the backend processes
    Takes in query and returns the response
Manages the API

To run the create new virtualenv in a cloned repo, run the following
('.env' can be replaced with <env_name>)
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt


'''

from utils import get_keys
from backend.pipeline import pipeline

def main():

    test_run = pipeline.Pipeline(testing=True)

    test_run.run_pipeline("I'm the test query")

    test_run.run_pipeline('Joe Biden is president')

    return None

if __name__ == "__main__":
    main()
