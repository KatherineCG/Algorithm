# coding=utf-8
import Queue
class TreeNode():
    def __init__(self, data, lchild = None, rchild = None):
        self.val = data
        self.lchild = lchild
        self.rchild = rchild
class Solution():
    def TraversalCreate(self, data, n):
            if len(data) > 0:
                if n < len(data):
                    if data[n] != '#':
                        l = n * 2 + 1
                        r = n * 2 + 2
                        root = TreeNode(data[n], self.TraversalCreate(data, l), self.TraversalCreate(data, r))
                        return root
                    else:
                        return None
                else:
                    return None
            else:
                return None
    def PreOrder(self, root, RetList):
        RetList.append(root.val)
        if root.lchild != None:
            self.PreOrder(root.lchild, RetList)
        if root.rchild != None:
            self.PreOrder(root.rchild, RetList)
        return RetList
    def InOrder(self, root, RetList):
        if root.lchild != None:
            self.InOrder(root.lchild, RetList)
        RetList.append(root.val)
        if root.rchild != None:
            self.InOrder(root.rchild, RetList)
        return RetList

    # 二叉树输出：层次遍历
    def traverse(self, node):
        res = []
        q = Queue.Queue()
        if root:
            q.put(root)
        while not q.empty():
            level = []
            length = q.qsize()
            for i in range(length):
                node = q.get()
                level.append(node.val)
                if node.lchild:
                    q.put(node.lchild)
                if node.rchild:
                    q.put(node.rchild)
            res.append(level)
        return res
test = Solution()
#data = ['1','2','3','4','5','#','#','#','#','6','7']
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#tree = TreeNode(data[0])
root = test.TraversalCreate(data, 0)
print (test.PreOrder(root, []))
print (test.InOrder(root, []))
print (test.traverse(root))
