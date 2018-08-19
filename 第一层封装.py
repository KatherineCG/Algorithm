# coding=utf-8
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Aname(self):
        print "名字是：%s" %(self.name)
    
    def Aage(self):
        print "年龄是：%d" %(self.age)

a = A('Alice', 10)
a.Aname()
a.Aage()