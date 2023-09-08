"""
Copyright (c) Zhejiang Lab. All right reserved.
"""


import datetime


def cal_sum(input_data):
    result = 0
    for data in input_data:
        result += data[-1]

    return result


def get_early_later_month(time_str="2021-02-06"):
    """

    :param time_str:
    :return: 当前月的前一个月最后一天和后一个月第一天
    """
    date_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    format_str = "%Y-%m-%d"
    dt = datetime.datetime.strptime(time_str, format_str)

    if dt.year % 4 == 0:  # 考虑二月29天
        date_in_month[1] = 29
    else:
        date_in_month[1] = 28

    if dt.month + 1 != 13:
        dt_later = datetime.datetime(year=dt.year, month=dt.month + 1, day=1)
    else:
        dt_later = datetime.datetime(year=dt.year+1, month=1, day=1)

    if dt.month - 1 != 0:
        dt_early = datetime.datetime(year=dt.year, month=dt.month - 1, day=date_in_month[dt.month - 1 - 1])
    else:
        dt_early = datetime.datetime(year=dt.year-1, month=12, day=date_in_month[0])

    res_later = dt_later.strftime(format_str)
    res_early = dt_early.strftime(format_str)
    return res_early, res_later


if __name__ == '__main__':
    r = cal_sum([(2, '水果', 'apple', '2023-10-06', 13.0), (5, '水果', 'apple', '2023-11-08', 14.0),
                 (6, '水果', 'apple', '2023-11-08', 0.0)])
    print(r)
    res_early, res_later = get_early_later_month("2020-03-07")
    print(res_early, res_later)