# coding=utf-8
class Animal:
    def run(self):
        print 'animal is running'
        #raise AttributeError('子类必须实现这个方法')
class Dog(Animal):
    def run(self):
        print 'dog is running'
    def run(self, name):
        print '%s is running' %(name)
class Cat(Animal):
    def run(self):
        print 'cat is running'
class Pig(Animal):
    def run(self):
        print 'pig is running'

dog = Dog()
cat = Cat()
pig = Pig()

#定义统一的接口
def func(obj): #obj这个参数没有类型限制，可以传入不同类型的值
    obj.run() #调用的逻辑都一样，执行的结果却不一样

#func(dog)
func(cat)
func(pig)
dog.run()