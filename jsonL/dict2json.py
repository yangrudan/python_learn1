from decimal import Decimal
import json
from pprint import pprint

import numpy as np
result = np.linspace(0, 512*1.2, 512).tolist()  # 精度不好看

data = {
    "array name": "阵1",
    "sampling rate": 5000,
    "detection azimuth" : [0,180],
    "operational band": [10,625],
    "array position": [ [round(i*1.2,2)  for i in range(512)],
             [0]*512,
             [0]*512]

}


out_list = [data] * 2

json_str = json.dumps(out_list)
pprint(json_str)