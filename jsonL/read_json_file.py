import json

def search_file_for_array(array_name="array-1"):
    read_fp = open("myfile.json","r")
    data = json.load(read_fp)
    print(type(data))

    for element in data:
        if element["array_name"] == array_name:
            print(element)
            return element
    
    print("Can not find array name")
    return None

search_file_for_array()