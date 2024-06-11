'''
Scrape webpage test
'''
from utils.read_files import read_text_from_file, read_csv_to_df
from utils import get_keys
import time
from datetime import datetime
from backend.preprocess.parse_page import parse_webpage
from backend.preprocess.gsearch import GSearch
from backend.preprocess import preprocess
import random
from utils.write_files import write_text_to_file

def print_text_samples(full_text, n_samples = 5):

    text_len = len(full_text)
    for i in range(n_samples):

        sample_start = int(i*(text_len/n_samples))
        random_sample_len = random.choice([20, 40, 50, 60, 75, 100])

        sample_end = int(min(text_len-1, 
                             sample_start + random_sample_len))
        
        print(full_text[sample_start:sample_end])
    return None

def save_scrape_text_to_file(full_text, link_scraped):


    test_timestamp = str(datetime.today())[:16]

    # Write to test file to read later
    filename = "test_data/test_"+test_timestamp+"/scrape_from_links.txt"

    # Include the data_to_write
    data_to_write = 'LINK:'+link_scraped + '\n\nSCRAPE_TEXT:\n\n'+ full_text

    write_text_to_file(filename, data_to_write)

    return None
    
def scrape_test():

    # Get link to scrape
    link_list = ['https://www.example.com',
                 'https://medium.com/@spaw.co/best-websites-to-practice-web-scraping-9df5d4df4d1']
    n_text_samples = 5

    # Scrape the webpage and output text
    for link_to_scrape in link_list[1:]:
        print('Running webpage scrape for:')
        print(link_to_scrape)

        # Get body text from webpage parser
        body_text = parse_webpage(link_to_scrape).strip()

        assert body_text != 'NO WEBPAGE FOUND', body_text

        # Check text (How?)
        print('\n\nLINK:',link_to_scrape)
        print('BODY:')
        #print_text_samples(body_text, n_text_samples)
        print(len(body_text),'is the length of body text')

        #print('start',body_text.strip(),'end')

        save_scrape_text_to_file(body_text, link_to_scrape)

    return None

def gsearch_test():

    keychain = get_keys.read_keys_from_json()
    testing  = True
    top_n_searches = 1
    test_timestamp = str(datetime.today())[:16]

    gsearcher = GSearch(keychain,
                        testing,
                        top_n_searches,
                        test_timestamp)
    
    claim = 'Full moons make people crazy'
    print('CLAIM:',claim)
    search_data = gsearcher.run_google_searches(claim)
    context_for_gpt = gsearcher.extract_context_from_google_search_results(search_data)

    print(context_for_gpt)
    pass