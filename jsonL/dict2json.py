from decimal import Decimal
import json
from pprint import pprint

import numpy as np
result = np.linspace(0, 512*1.2, 512).tolist()  # 精度不好看

data = {
    "array_name": "array-1",
    "sensor_num": 512,
    "connector_pos": 32,
    "sampling_rate": 5000,
    "detection_azimuth" : [0,180],
    "operation_band": [10,625],
    "3d_array_position": [ [round(i*1.2,2)  for i in range(512)],
             [0]*512,
             [0]*512]

}


out_list = [data] * 2

json_str = json.dumps(out_list)

out_file = open("myfile.json", "w") 
json.dump(out_list, out_file) 
out_file.close()

pprint(json_str)