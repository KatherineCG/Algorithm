
# -*- coding: utf-8 -*-
import sys
def out_money(totle):
    while totle > 0:
        totle -= 1
        yield 1                             # yield 返回一个值
ATM = out_money(3)   #ATM generator中的值为：1 1 1，即如果存在next，next(ATM)=1
while True:
    try:
        print("取到钱 %s 万" % next(ATM))
        print("花掉花掉!")
    except StopIteration:
        print ("没钱了")
        sys.exit()