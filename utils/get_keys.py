import json

def read_keys_from_json():
    try:
        with open("../keys/keys.json", "r") as file:
            keys_data = json.load(file)
            return keys_data
    except FileNotFoundError:
        print("Error: keys.json file not found.")
        return {}

# Example usage:
# keychain = read_keys_from_json()
# print(keychain)