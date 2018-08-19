# coding=utf-8
class ListNode():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class LinkList():
    def __init__(self):
        self.head = ListNode
    
    #初始化单链表
    def CreateLinkList(self, data):
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            p.next = ListNode(i)
            p = p.next
    
    #打印单链表
    def PrintLinkList(self):
        p = self.head
        while p!= None:
            print p.data
            p = p.next
    
    #获取单链表长度
    def LengthLinkList(self):
        length = 0
        p = self.head
        while p!=None:
            length += 1
            p = p.next
        return length
    
    #判断单链表是否为空
    def IsEmpty(self):
        if self.LengthLinkList() == 0:
            return True
        else:
            return False
    
    #在单链表后插入数据
    def AppendLinkList(self, item):
        if self.IsEmpty():
            self.head = ListNode(item)
        else:
            p = self.head
            while p != None:
                p = p.next
            p.next = ListNode(item)
            
    #获取单链表指定位置的数据
    def GetItem(self, index):
        if self.IsEmpty():
            print ("单链表为空")
            return
        if index < 0 or index > self.LengthLinkList():
            print ("索引超过单链表长度")
            return
        p = self.head
        count = 0
        while count != index:
            count += 1
            p = p.next
        return p.data
    
    #获取单链表指定元素的索引
    def Find(self, item):
        if self.IsEmpty():
            print ("单链表为空")
            return
        p = self.head
        count = 0
        while p != None:
            if p.data == item:
                return count
            count += 1
            p = p.next
        print ("单链表中不存在" + repr(item))
    
    #在单链表指定位置插入元素
    def InsertIntoLinkList(self, index, item):
        if self.IsEmpty():
            print ("单链表为空")
            return
        if index < 0 or index > self.LengthLinkList():
            print ("索引超过单链表长度")
            return
        if index == 0:
            self.head = ListNode(item, self.head)
        else:
            p = self.head
            count = 0
            while count < index-1:
                count += 1
                p = p.next
            p.next = ListNode(item, p.next)
    
    #删除单链表指定位置的元素
    def Delete(self, index):
        if self.IsEmpty():
            print ("单链表为空")
            return
        if index < 0 or index >= self.LengthLinkList():
            print ("索引超过单链表长度")
            return
        if index == 0:
            self.head = self.head.next
        else:
            p = self.head
            count = 0
            while count < index - 1:
                count += 1
                p = p.next
            p.next = p.next.next
    
    #更新单链表指定位置元素
    def Update(self, index, item):
        if self.IsEmpty():
            print ("单链表为空")
            return
        if index < 0 or index >= self.LengthLinkList():
            print ("索引超过单链表长度")
            return
        if index == 0:
            self.head.data = item
        else:
            p = self.head
            count = 0
            while count != index:
                count += 1
                p = p.next
            p.data = item
    
    #清空单链表
    def ClearLinkList(self):
        self.head = None
            

data = raw_input().split(' ')
data = list(data)
test = LinkList()
test.CreateLinkList(data)
test.Update(3,0)
test.PrintLinkList()
