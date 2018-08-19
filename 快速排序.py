import random
class Solution:
    
    def Partition(self, data, start, end):
        i = random.randint(start, end)
        key = data[i]
        data[i], data[start] = data[start], data[i]
        while start < end:
            while start < end and data[end] >= key:
                end -= 1
            while start < end and data[end] < key:
                data[start] = data[end]
                start += 1
                data[end] = data[start]
        data[start] = key
        return start
    
    def QickSort(self, data, start, end):
        if start == end:
            return
        index = self.Partition(data, start, end)
        if index > start:
            self.QickSort(data, start, index)
        if index < end:
            self.QickSort(data, index+1, end)
test = Solution()
data = [3, 1, 5, 6, 2, 0, 9]
test.QickSort(data, 0, 6)
for i in range(len(data)):
    print data[i]
