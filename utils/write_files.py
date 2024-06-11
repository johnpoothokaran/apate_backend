import json
import os

def prepare_directory(filename):
    # Extract directory path from filename
    directory = os.path.dirname(filename)

    # If directory does not exist, create it
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    return None


def write_text_to_file(filename, data_to_write):
    prepare_directory(filename)
    with open(filename, "w") as text_file:
        text_file.write(data_to_write)

    return None


def write_json_to_file(filename, data_to_write):
    prepare_directory(filename)
    with open(filename, "a") as json_file:
        json.dump(data_to_write, json_file, indent=4)

    return None
