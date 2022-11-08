import string

path = 'D:\\yangrudan\\Walden.txt'
with open(path,'r',encoding='utf-8') as text:
 words = text.read().split()
 print(words)
 for word in words:
     print('{}-{} times'.format(word,words.count(word)))

