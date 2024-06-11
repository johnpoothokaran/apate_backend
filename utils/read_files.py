import pandas as pd

def read_text_from_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def read_csv_to_df(filename):
    try:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
# Example usage:
#text_content = read_text_from_file('prompts/system_message_v0.txt')
#if text_content is not None:
#    print(text_content)
#read_text = read_from_text_file('prompts/system_message_v0.txt')