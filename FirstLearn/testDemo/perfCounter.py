# what_he_does = ' plays '
# his_instrument = 'guitar'
# his_name = 'Robert Johnson'
# artist_intro = his_name + what_he_does + his_instrument
#
# print(artist_intro)
import time
a = []
t0 = time.perf_counter()
for i in range(1,20000):
  a.append(i)
print(time.perf_counter() - t0, "seconds process time")
t0 = time.perf_counter()
b = [i for i in range(1,20000)]
print(time.perf_counter() - t0, "seconds process time")