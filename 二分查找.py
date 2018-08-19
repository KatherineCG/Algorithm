# coding=utf-8
import bisect
class Find:
    #二分查找
    def binary_serch(self, list, key):
        low = 0
        high = len(list)
        result = []
        if high <= 0:
            return -1
        while low <= high:
            mid = (low + high) / 2
            if list[mid] == key:
                x = mid
                while list[x] == key:
                    result.append(x)
                    x -= 1
                while list[mid+1] == key:
                    result.append(mid+1)
                    mid += 1
                return result
            elif list[mid] > key:
                #查找左半边
                high = mid - 1
            elif list[mid] < key:
                #查找右半边
                low = mid + 1
        return -1
find = Find()
list = [1, 1, 1, 1, 1, 2]
print find.binary_serch(list, 1)
print bisect.bisect(list, 4)