# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        for i in range(3):
            print(i)
            if i == 2:
                print("this is break")
                break
        else:
            print("正常走完else~~~~")  # for循环正常走完，就会走else
    print("End")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
