
fn = ('赵','钱','孙','李','周','吴','郑','王')
ln1 = ('明','华','楠','白')
ln2 = ('思明','韶华','楠楠','秋白')

import random
class FakeUser:
    def fake_name(self,amount = 1,one_word = False,two_words = False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
            yield full_name
            n += 1

    def fake_gender(self,amount = 1):
        n = 0
        while n <= amount:
            gender = random.choice(['男', '女', '未知'])
            yield gender
            n += 1


class SnsUser(FakeUser):
    def get_followers(self,amount = 1,few = True,a_lot = False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1, 50)
            elif a_lot:
                followers = random.randrange(200, 10000)
            yield followers
            n += 1

user_a = FakeUser()
user_b = SnsUser()
for name in user_a.fake_name(30):
    print(name)
for gender in user_a.fake_gender(30):
    print(gender)