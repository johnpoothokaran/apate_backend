'''
Full pipeline test
'''
from backend.pipeline import pipeline

def pipeline_test():

    test_run = pipeline.Pipeline(testing=True)

    test_run.run_pipeline("I'm the test query")

    test_run.run_pipeline('Joe Biden is president')

    return None