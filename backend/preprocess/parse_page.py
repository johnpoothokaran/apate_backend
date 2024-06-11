import requests
from bs4 import BeautifulSoup
import re

# Function to add new lines for readability
def extract_text_with_newlines(element):
    text = ''
    for tag in element.descendants:
        if isinstance(tag, str):
            text += tag
        elif tag.name in ['p', 'div', 'br', 'li']:
            text += '\n'
    return text


def test_filtering(line):
    total_len = len(line) + 1.0
    if total_len > 20:
        count_special_char = sum(1 for char in line if (not char.isalnum()) and (not char == ' '))
        special_char_percent = round(count_special_char*100.0/total_len)

        '''
        if special_char_percent > 20:
            print(special_char_percent,'% SPECIAL CHAR COUNT')
            print('LINE START',line,'LINE END')
        print(line[:200], 'AND SPECIAL CHAR %',special_char_percent, 'WITH LENGTH',len(line))
        '''

    return None


# Function to filter out non-natural language chunks
def filter_non_natural_language(text):
    # Split text into lines
    lines = text.split('\n')
    filtered_lines = []
    for line in lines:
        # Skip empty lines
        if len(line) == 0:
            continue

        # Remove lines with patterns typical of non-natural language
        if re.search(r'window\.__|{.*}|;|:', line):
            # print('DELETED 1')
            continue
        # Remove lines that contain too many special characters
        if re.search(r'[{};=]', line):
            # print('DELETED 2')
            continue

        total_len = len(line) + 1.0
        count_special_char = sum(1 for char in line if (not char.isalnum()) and (not char == ' '))
        special_char_percent = round(count_special_char*100.0/total_len)

        # Remove longer lines containing more than 20% of special char (not including spaces)
        if total_len > 100 and special_char_percent > 15:
            # print('DELETED 3')
            continue

        # Remove lines with less than 10 characters
        if total_len < 10:
            # print('DELETED 4')
            continue

        #print(len(line),'chars added to the next line')
        filtered_lines.append(line)
    return '\n'.join(filtered_lines)


def parse_webpage(url):
    # URL of the webpage you want to scrape
    # url = 'https://example.com'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the <body> tag
        body_tag = soup.body
        #print('SOUP keys:')
        #print(type(soup))
        #print(soup.keys)
        
        # Extract text from the <body> tag
        if body_tag:
            # Get the text from the body tag
            # Gets a single line thats hard to read
            # body_text = body_tag.get_text()

            # Adds newlines based on tags in the html structure
            body_text_unfiltered = extract_text_with_newlines(body_tag)
            body_text = filter_non_natural_language(body_text_unfiltered)
            # Print the extracted text
            # print(body_text)
        else:
            print("No <body> tag found on the webpage.")
            body_text = 'NO BODY FOUND'
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        body_text = 'NO WEBPAGE FOUND'

    return body_text.strip()

