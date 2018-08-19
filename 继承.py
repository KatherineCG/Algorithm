# coding=utf-8
class Animal:

    def eat(self):
        print "%s 吃 " %self.name

    def drink(self):
        print "%s 喝 " %self.name

    def shit(self):
        print "%s 拉 " %self.name

    def pee(self):
        print "%s 撒 " %self.name

class Cat(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '猫'

    def cry(self):
        print '喵喵叫'

class Dog(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '狗'

    def cry(self):
        print '汪汪叫'

# ######### 执行 #########

c1 = Cat('猫one')
c1.eat()

c2 = Cat('猫two')
c2.drink()

d1 = Dog('狗one')
d1.eat()