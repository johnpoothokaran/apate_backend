'''
Key names
1. openai_api_key
2. openai_org_key
3. google_search_api_key
4. google_search_engine_id
'''
import json

# Example usage:
# keychain = read_keys_from_json()
# print(keychain)

def read_keys_from_json():
    try:
        with open("./keys/actual_keys.json", "r") as file:
            keys_data = json.load(file)
            return keys_data
    except FileNotFoundError:
        print("Error: actual_keys.json file not found.\nCheck path from where script is run")
        return {}

