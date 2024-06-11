'''
Full pipeline test
'''
from backend.pipeline import pipeline
from utils.read_files import read_text_from_file, read_csv_to_df
import time

def get_queries_to_test(fname):

    filename = './test_data/query_test_set/'+fname
    queries_file = read_text_from_file(filename)
    #print(queries_file)

    query_list = queries_file.split('\n')
    #print(query_list)

    test_queries = []

    for q in query_list:
        items = q.split(':')
        test_queries.append((items[0],items[1])) #contains (query,result)
    
    return test_queries

def get_fake_covid_claims():
    
    filename = './test_data/query_test_set/ClaimFakeCOVID-19.csv'
    df_fake_covid_claims = read_csv_to_df(filename)

    print(df_fake_covid_claims['title'])
    claims_list = list(df_fake_covid_claims['title'])
    test_queries = []

    for q in claims_list:
        test_queries.append((q,'FALSE')) #contains (query,result)

    return test_queries
        

def pipeline_test(debug = True):

    test_run = pipeline.Pipeline(testing=True)

    #test_run.run_pipeline("I'm the test query")

    #test_run.run_pipeline('Joe Biden is president')

    #test_run.run_pipeline('George Bush is president')

    '''
    test_run.run_pipeline("Applying lemon juice to your skin can cure acne")
    # False

    test_run.run_pipeline("Narendra Modi is Prime minister")
    # True

    test_run.run_pipeline("Climate change is a hoax")
    # False

    #'''
    #test_queries = get_queries_to_test("query_100.txt")
    test_queries = get_queries_to_test("query_tester.txt")
    #test_queries = get_fake_covid_claims()
    #print(test_queries)

    correct_answer_count = 0
    mistakes = []
    start = time.time()

    if debug:
        queries_to_run = 3
    else:
        queries_to_run = len(test_queries)

    for query_answer in test_queries:#[:queries_to_run]:#[:2]:

        q = query_answer[0]
        a = query_answer[1]
        # print("QUERY:",q,"\nANSWER:",a)

        llm_response = test_run.run_pipeline(q)

        a_llm = llm_response['LABEL']
        if '/' in a:
            a = a.split('/')
        else:
            a = [a]
        
        print(a, a_llm)
        if a_llm in a:
            correct_answer_count += 1
        else:
            mistakes.append((q,a,a_llm))
    
    print('LLM accuracy:',correct_answer_count*100.0/queries_to_run,"%")
    
    for each_mistake in mistakes:
        print(each_mistake[0])
        print('Expected:',each_mistake[1])
        print('Given:',each_mistake[2])

    print('Time taken:',round(time.time() - start,2))


    
    return None

