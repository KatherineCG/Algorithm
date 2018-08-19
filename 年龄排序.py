class Solution:
    def SortAges(self, ages, length):
        if ages == None or length <= 0:
            return
        oldestage = 99
        AgeTimes = [0] * 100
        for i in range(length):
            age  = ages[i]
            if age < 0 or age > oldestage:
                raise Exception
            AgeTimes[age] += 1
        index = 0
        for i in range(len(AgeTimes)):
            for j in range(AgeTimes[i]):
                ages[index] = i
                index += 1
        return ages
test = Solution()
ages = [30, 40, 0, 40, 14, 30, 20, 10, 0]
age = test.SortAges(ages, 9)
for i in range(len(age)):
    print age[i]