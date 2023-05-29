letters_amazon = '''
We spent serval years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as 
the commercial engines, but at one-tench of the cost.We were
not surprised when this worked.
'''


def str_strip(input_str):
    find_str = lambda x, q: x[x.find(q) - 18:x.find(q) + 18] if q in x else -1
    print(find_str(input_str, 'SQL'))
    return find_str(input_str, 'SQL')


if __name__ == '__main__':
    str_strip(letters_amazon)