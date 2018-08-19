# coding=utf-8
from __future__ import print_function
import bisect


my_list = [2, 7, 4, 6, 3, 8, 4]

# 对my_list排序
my_list.sort()
print(my_list)  # [2, 3, 4, 4, 6, 7, 8]

print(bisect.bisect_left(my_list, 1))  # 2
print(bisect.bisect_right(my_list, 4))  # 4
print(bisect.bisect(my_list, 4))  # 4

print(bisect.bisect_right(my_list, 6, 2, len(my_list)))  # 5  # beg代表开始位置，end代表结束位置
