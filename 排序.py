# coding=utf-8
from __future__ import print_function

class Sort:
    # 插入排序
    def insert_sort(self, list):
        if list == None:
            return
        count = len(list)
        for i in range(1, count):
            key = list[i]
            j = i - 1
            while j >= 0:
                if list[j] > key:
                    list[j + 1] = list[j]
                    list[j] = key
                j -= 1
        return list
    
    #希尔排序
    def shell_sort(self, list):
        if len(list) == 0:
            return -1
        #设定步长
        step = 2
        group = len(list) / step
        while group > 0:
            for i in range(group, len(list)):
                while i >= group and list[i] < list[i-group]:
                    list[i], list[i - group] = list[i-group], list[i]
                    i -= group
            group = group / step
        return list
    
    #冒泡排序
    def bubble_sort(self, list):
        if len(list) == 0:
            return -1
        for i in range(0, len(list)):
            for j in range(i+1, len(list)):
                if list[i] > list[j]:
                    list[i], list[j] = list[j], list[i]
        return list
    
    #快速排序
    def quicksort(self, list, start, end):
        if start >= end:
            return list
        key = list[start]
        low = start
        high = end
        while start < end:
            while start < end and list[end] >= key:
                end -= 1
            while start < end and list[end] < key:
                list[start] = list[end]
                start += 1
                list[end] = list[start]
        list[start] = key
        self.quicksort(list, low, start)
        self.quicksort(list, start+1, high)
        return list
    
    #直接选择排序
    def selectsort(self, list):
        if len(list) <= 0:
            return
        length = len(list)
        for i in range(0, length):
            min = i
            for j in range(i+1, length):
                if list[j] < list[min]:
                    min = j
            list[i], list[min] = list[min], list[i]
        return list
    
    #堆排序
    def adjust_heap(self, list, i, size):
        lchild = i * 2 + 1
        rchild = i * 2 + 2
        max = i
        if i < size / 2:
            if lchild < size and list[lchild] > list[max]:
                max = lchild
            if rchild < size and list[rchild] > list[max]:
                max = rchild
            if max != i:
                list[max], list[i] = list[i], list[max]
                self.adjust_heap(list, max, size)
    
    def build_heap(self, list, size):
        for i in range(0, (size/2))[::-1]:
            self.adjust_heap(list, i, size)
    
    def heap_sort(self, list):
        size = len(list)
        self.build_heap(list, size)
        for i in range(0, size)[::-1]:
            list[i], list[0] = list[0], list[i]
            self.adjust_heap(list, 0, i)
        return list
    
    #归并排序
    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    def merge_sort(self, list):
        if len(list) <= 1:
            return list
        num = len(list) / 2
        left = self.merge_sort(list[:num])
        right = self.merge_sort(list[num:])
        return self.merge(left, right)
    
    #基数排序
    
    
sort = Sort()
list = [5, 4, 3, 2, 1]
insert_sortlist = sort.insert_sort(list)
merge_sortlist = sort.merge_sort(list)
shell_sortlist = sort.shell_sort(list)
bubble_sortlist = sort.bubble_sort(list)
quick_sortlist = sort.quicksort(list, 0, 4)
select_sortlist = sort.selectsort(list)
heap_sortlist = sort.heap_sort(list)
print(heap_sortlist)
