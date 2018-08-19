# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        if listNode == None:
            return res
        p = listNode.next
        newlist = listNode
        while p != None:
            temp = p.next
            p.next = newlist
            newlist = p
            p = temp
        listNode.next = None
        while newlist != None:
            res.append(newlist.val)
            newlist = newlist.next
        return res
test = Solution()
A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)
A.next = B
B.next = C
C.next = D
D.next = E
print test.printListFromTailToHead(A)