# coding=utf-8
import re
class ListNode():
    def __init__(self, data, next = None):
        self.val = data
        self.next = next
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pMergeHead = pHead1
        while pHead1 != None and pHead2 != None:
            if pHead1.val <= pHead2.val:
                if pHead1.next and pHead1.next.val >= pHead2.val:
                    pHead1_next = pHead1.next
                    pHead2_next = pHead2.next
                    pHead1.next = pHead2
                    pHead2.next = pHead1_next
                    pHead1 = pHead1_next
                    pHead2 = pHead2_next
                elif pHead1.next == None:
                    pHead1.next = pHead2
                    break
                else:
                    pHead1 = pHead1.next
            else:
                pHead2 = pHead2.next
        if pHead2 != None:
            pHead1 = pHead2
        return pMergeHead

test = Solution()
pHead1input = raw_input()
pHead2input = raw_input()
def HandleInput(array):
    #array = re.sub('[[]]', '', array).split(',')
    pHead = ListNode(int(array[1]))
    p = pHead
    for ch in array[3::2]:
        p.next = ListNode(int(ch))
        p = p.next
    return pHead
if pHead1input == '[]' and pHead2input == '[]':
    print '[]'
else:
    if pHead1input == '[]' and pHead2input != '[]':
        pMergeHead = HandleInput(pHead2input)
    elif pHead1input != '[]' and pHead2input == '[]':
        pMergeHead = HandleInput(pHead1input)
    else:
        pHead1 = HandleInput(pHead1input)
        pHead2 = HandleInput(pHead2input)
        if pHead1.val <= pHead2.val:
            pMergeHead = test.Merge(pHead1, pHead2)
        else:
            pMergeHead = test.Merge(pHead2, pHead1)
    output = '['
    while pMergeHead != None:
        output = output + repr(pMergeHead.val)
        if pMergeHead.next != None:
            output = output + ','
        pMergeHead = pMergeHead.next
    print output + ']'
