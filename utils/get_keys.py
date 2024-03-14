import json

def read_keys_from_json():
    try:
        with open("./keys/actual_keys.json", "r") as file:
            keys_data = json.load(file)
            return keys_data
    except FileNotFoundError:
        print("Error: actual_keys.json file not found.\nCheck path from where script is run")
        return {}

# Example usage:
# keychain = read_keys_from_json()
# print(keychain)