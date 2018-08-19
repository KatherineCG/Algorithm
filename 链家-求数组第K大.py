class Solution():
    def kthbiggest(self, array1, array2, array3, n, k):
        array = array1 + array2 + array3
        array.sort()
        if n < 0 or n > 100000:
            return -1
        if array1 == [] and array2 == [] and array3 == []:
            return -1
        if k > 3*n or k < 1:
            return -1
        if len(array1) != n or len(array2) != n or len(array3) != n:
            return -1
        return array[k-1]
test = Solution()
input = raw_input()
for i in range(len(input)):
    if input[i] == ' ':
        break
n = int(input[:i])
k = int(input[i+1:])
array1 = raw_input()
array1 = array1.split(' ')
array1 = map(int, array1)
array2 = raw_input()
array2 = array2.split(' ')
array2 = map(int, array2)
array3 = raw_input()
array3 = array3.split(' ')
array3 = map(int, array3)
print test.kthbiggest(array1, array2, array3, n, k)