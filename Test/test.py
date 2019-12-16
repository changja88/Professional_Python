import bisect
import random


HAYSTACK = [12, 1, 4, 6, 8, 12, 34, 78, 1, 3, 476, 23, 6748]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

my_list = []
bisect.insort(my_list,HAYSTACK)
# print(my_list)




test_list = []
for i in range(7):
    new_item = random.randrange(14)
    bisect.insort(test_list,new_item)


