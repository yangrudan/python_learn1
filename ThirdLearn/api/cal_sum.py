"""
Copyright (c) Zhejiang Lab. All right reserved.
"""
"""
[(2, '水果', 'apple', '2023-10-06', 13.0), (5, '水果', 'apple', '2023-11-08', 14.0), (6, '水果', 'apple', '2023-11-08', 0.0)]
"""


def cal_sum(input_data):
    result = 0
    for data in input_data:
        result += data[-1]

    return result

if __name__ == '__main__':
    r = cal_sum([(2, '水果', 'apple', '2023-10-06', 13.0), (5, '水果', 'apple', '2023-11-08', 14.0), (6, '水果', 'apple', '2023-11-08', 0.0)])
    print(r)