# coding=utf-8
import time

def consumer(name):
    print("%s 准备吃包子了！" %name)
    while True:
        baozi = yield                    # yield 通过 send()方法接收值
        print("包子[%s]来了，被[%s]吃了" %(baozi,name))
        
def producer(name):
    c1 = consumer('A')
    c2 = consumer('B')
    c3 = consumer('C')
    next(c1)
    next(c2)
    next(c3)

    print("%s 开始准备做包子了！" % name)

    for i in range(5):
        time.sleep(1)
        print('做了3个包子')
        c1.send(i)
        c2.send(i)
        c3.send(i)

producer('hh')