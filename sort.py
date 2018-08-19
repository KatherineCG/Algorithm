# coding=utf-8
class Solution:
    
    #冒泡排序
    def bubblesort(self, array):
        if not array:
            return []
        length = len(array)
        for i in range(length):
            for j in range(i+1, length):
                if array[i] > array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
        return array
    
    #选择排序
    def selectsort(self, array):
        if not array:
            return []
        length = len(array)
        for i in range(length):
            min = i
            for j in range(i+1, length):
                if array[j] < array[i]:
                    min = j
            if min != i:
                temp = array[i]
                array[i] = array[min]
                array[min] = temp
        return array
    
    #插入排序
    def insertsort(self, array):
        if not array:
            return []
        length = len(array)
        for i in range(1, length):
            j = i
            key = array[i]
            while j >= 0 and array[j-1] > key:
                array[j] = array[j-1]
                j -= 1
            array[j] = key
        return array
    
    #希尔排序
    def shell_sort(self, array):
        if not array:
            return []
        gap = len(array)
        while gap >= 1:
            gap = gap // 2
            for i in range(gap, len(array)): #从gap开始循环：gap是几，最开始排序的元素的位置就是几
                key = array[i]
                j = i
                while j >= 0 and array[j-gap] > key:
                    array[j] = array[j-gap]
                    j -= gap
                array[j] = key
        return array
    
    #归并排序
    def mergesort(self, array1, array2):
        if not array1:
            return array2
        elif not array2:
            return array1
        i, j = 0, 0
        len1 = len(array1)
        len2 = len(array2)
        res = []
        while i < len1 and j < len2:
            if array1[i] < array2[j]:
                res.append(array1[i])
                i += 1
                continue
            else:
                res.append(array2[j])
                j += 1
                continue
        if i != len1:
            res += array1[i:]
        else:
            res += array2[j:]
        return res
    
    #快速排序
    def quicksort(self, array, start, end):
        if end <= start:
            return []
        low = start
        high = end
        key = array[start]
        while end > start:
            if array[end] > key:
                end -= 1
            else:
                array[end] = array[start]
                start += 1
                array[start] = end
        array[start] = key
        self.quicksort(array, low, start)
        self.quicksort(array, start+1, high)
        return array
    
    #堆排序
    '''
    构建大顶堆，从最后一个堆开始，即i = len/2，直到i = 0,保证每一个堆都是大顶堆
    用堆顶元素和左右元素相比较，如果堆顶元素小，则交换
    如果发生交换，则以交换位置为堆顶元素，再次调整为大顶堆
    '''
    def buildMaxHeap(self, array, length):
        for i in range(0, length/2)[::-1]:
            self.adjustheap(array, i, length)
            
    def adjustheap(self, array, i, length):
        left = i * 2 + 1
        right = i * 2 + 2
        max = i
        if left < length and array[left] > array[max]:
            max = left
        if right < length and array[right] > array[max]:
            max = right
        if max != i:
            array[i], array[max] = array[max], array[i]
            self.adjustheap(array, max, length)
            
    def heapsort(self, array):
        if not array:
            return []
        length = len(array)
        self.buildMaxHeap(array, length)
        for i in range(0, length)[::-1]:
            array[0], array[i] = array[i], array[0]
            self.adjustheap(array, 0, i)
        return array
    
    #基数排序
    def radixsort(self, array, maxDigit):
        if not array:
            return []
        mod = 10
        dev = 1
        length = len(array)
        #求最大的数的位数，确定第一轮循环次数
        num = 0
        while maxDigit != 0:
            num += 1
            maxDigit = maxDigit / mod
        for i in range(num):
            #二位数组：计数排序，每次循环置空
            tempradix = [[] for i in range(10)]
            for j in range(length):
                #求确定个十百位的值
                key = (array[j] % mod) / dev
                tempradix[key].append(array[j])
            #每次基数排序后重新得到的数列
            array = []
            for k in range(10):
                array += tempradix[k]
            mod *= 10
            dev *= 10
        return array
    
    #计数排序
    def countingsort(self, array, maxValue):
        if not array:
            return []
        bucket = {}
        length = len(array)
        for i in range(length):
            if array[i] in bucket:
                bucket[array[i]] += 1
            else:
                bucket[array[i]] = 1
        array = []
        for i in range(maxValue+1):
            if i in bucket and bucket[i] > 0:
                array.append(i)
                bucket[i] -= 1
        return array
        
    #桶排序
    def bucketsort(self, array, bucketsize):
        if not array:
            return []
        minValue = array[0]
        maxValue = array[0]
        length = len(array)
        
        #求数组的最大值和最小值
        for i in range(length):
            if array[i] < minValue:
                minValue = array[i]
            elif array[i] > maxValue:
                maxValue = array[i]
        
        #桶的数量（最大值-最小值）/桶容量
        bucketCount = (maxValue - minValue) / bucketsize + 1
        #桶为二维数组
        buckets = [[] for i in range(bucketCount)]
        #映射函数：将元素分配到桶内，元素所在桶的序号为：（元素-最小值）/桶容量
        for i in range(length):
            buckets[(array[i]-minValue)/bucketsize].append(array[i])
        
        array = []
        for i in range(len(buckets)):
            #一个桶内的元素快速排序
            buckets[i].sort()
            for j in range(len(buckets[i])):
                array.append(buckets[i][j])
        return array
    
test = Solution()
array = [3,11,45,24,82,58,36,97]
array1 = [1,3,5,7]
array2 = [2,4,6,8]
#print test.bubblesort(array)
#print test.selectsort(array)
#print test.insertsort(array)
#print test.quicksort(array, 0, len(array)-1)
#print test.shell_sort(array)
#print test.mergesort(array1, array2)
#print test.heapsort(array)
#print test.countingsort(array, 8)
#print test.bucketsort(array, 5)
print test.radixsort(array, 97)