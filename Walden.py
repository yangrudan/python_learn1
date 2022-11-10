import string

path = 'D:\\yangrudan\\Walden.txt'
f = None
try:
    f = open(path, 'r', encoding='utf-8')
    words = f.read().split()
    print(words)
    for word in words:
        print('{}-{} times'.format(word,words.count(word)))
except FileNotFoundError:
    print("无法打开指定的文件")
except LookupError:
    print("指定了未知的编码")
except UnicodeDecodeError:
    print("读取文件时解码错误")
finally:
    if f:
        f.close()




