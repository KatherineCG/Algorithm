# coding=utf-8
def AddFrom1ToN(n):
    if n == 0:
        return 0
    else:
        return n + AddFrom1ToN(n - 1)
def AddFrom1ToN1(n):
    sum = 0
    for i in  range(1, n + 1):
        sum = sum + i
    return sum

def factorial(n) :
  if n == 1 :
    return 1
  return n * factorial(n - 1)

print factorial(4)
#print AddFrom1ToN(1000)
print AddFrom1ToN1(1000)