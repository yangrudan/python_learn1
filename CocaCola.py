class CocaCola:
    formula = ['caffeine', 'sugur', 'water', 'soda']
    def __init__(self):
        self.local_logo = '可口可乐'

    def drink(self):
        print('Energy!')

coke = CocaCola()
coke.drink()
print(coke.local_logo)
print(coke.drink() == CocaCola.drink(coke))


class TestA:
 attr = 1
obj_a = TestA()
TestA.attr = 42
print(obj_a.attr)
print(TestA.__dict__)
print("###############")
print(obj_a.__dict__)