# coding=utf-8
from collections import deque
#L = deque([49,38,65,97,76,13,27,49])
L = deque([1, 2, 3])
L.appendleft(0)
def element_exchange(numbers,low,high):

    temp = numbers[low]

    # j 是low的左孩子节点(cheer!)
    i = low
    j = 2*i

    while j<=high:
        # 如果右节点较大，则把j指向右节点
        if j<high and numbers[j]<numbers[j+1]:
            j = j+1
        if temp<numbers[j]:
            # 将numbers[j]调整到双亲节点的位置上
            numbers[i] = numbers[j]
            i = j
            j = 2*i
        else:
            break
    # 被调整节点放入最终位置
    numbers[i] = temp
    print (numbers)

def top_heap_sort(numbers):

    length = len(numbers)-1
    print len(numbers)

    # 指定第一个进行调整的元素的下标
    # 它即该无序序列完全二叉树的第一个非叶子节点
    # 它之前的元素均要进行调整
    # cheer up！
    first_exchange_element = length/2

    #建立初始堆
    print first_exchange_element
    for x in range(first_exchange_element):
        element_exchange(numbers,first_exchange_element-x,length)
        print('##')

    # 将根节点放到最终位置，剩余无序序列继续堆排序
    # length-1 次循环完成堆排序
    for y in range(length-1):
        temp = numbers[1]
        numbers[1] = numbers[length-y]
        numbers[length-y] = temp
        element_exchange(numbers,1,length-y-1)

if __name__=='__main__':
    top_heap_sort(L)
    for x in range(1,len(L)):
        print L[x],