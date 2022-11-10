def boxPrint(symbol, width, height):
 if len(symbol) != 1:
   raise Exception('Symbol must be a single character string.')
 if width <= 2:
   raise Exception('Width must be greater than 2.')
 if height <= 2:
  raise Exception('Height must be greater than 2.')
 print(symbol * width)
 for i in range(height - 2):
   print(symbol + (' ' * (width - 2)) + symbol)
 print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
   try:
     boxPrint(sym, w, h)
   except Exception as err:
     print('An exception happened: ' + str(err))

from math import sqrt
def is_prime(n):
    '''判断素数的函数'''
    assert n > 0
    print("============")
    for factor in range(2, int(sqrt(n))+1):
        if n % factor == 0:
            return False
    return True if n !=1 else False

is_prime(9)