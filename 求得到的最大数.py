# coding=utf-8
def cmp(a, b):  #定义一个函数，交换a/b排序的最大值，由于ab输入的都是字符，所以直接相加也是字符
    ab = int(a+b)
    ba = int(b+a)
    return 1 if ab > ba else -1
num = input('')   #输入参数n，代表有几个数字
l=raw_input().split()  #输入一哥哥数字，并且用空格隔开
l.sort(cmp, reverse=True) #sort排序，利用自己定义的cmp方法
for i in range(0,num):
    result = result+str(int(l[i]))  #将结果的字符串链接到一起
print int(result)
