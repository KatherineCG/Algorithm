class A:
    __x = 1
    def __test(self):
        print 'private test'
print A.__dict__
#print A.__x
print A._A__x
a = A()
print a.__dict__
print a._A__x
a._A__test()
#A._A__test(111)