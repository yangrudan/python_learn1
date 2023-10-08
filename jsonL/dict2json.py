from decimal import Decimal
import json
import os
from pprint import pprint

import numpy as np
result = np.linspace(0, 512*1.2, 512).tolist()  # 精度不好看


if os.path.exists("myfile.json"):
    read_fp = open("myfile.json","r")
    list_data = json.load(read_fp)
else:
    list_data=[]

data = {
    "array_name": "array-2",
    "sensor_num": 512,
    "connector_pos": 32,
    "sampling_rate": 5000,
    "detection_azimuth" : [0,180],
    "operation_band": [10,625],
    "3d_array_position": [ [round(i*1.2,2)  for i in range(512)],
             [0]*512,
             [0]*512]

}

list_data.append(data)

json_str = json.dumps(list_data, indent=6)

out_file = open("myfile.json", "w") 
json.dump(list_data, out_file) 
out_file.close()

pprint(json_str)