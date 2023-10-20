import json
import os

def search_file_for_array(json_file_path="myfile.json", array_name="array-1"):
    if os.path.exists(json_file_path):
        read_fp = open(json_file_path,"r")
        data = json.load(read_fp)
        print(type(data))

    for element in data:
        if element["array_name"] == array_name:
            print(element)
            return element
    
    print("Can not find array name")
    return None

search_file_for_array()