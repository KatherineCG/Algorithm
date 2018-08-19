# coding=utf-8
import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    def preorder(self, pRoot):
        if pRoot == None:
            return
        tree = []
        res = []
        p = pRoot
        while p != None or tree != []:
            while p:
                res.append(p.val)
                tree.append(p)
                p = p.left
            if tree != []:
                p = tree.pop()
                p = p.right
        return res
    def inorder(self, pRoot):
        if pRoot == None:
            return []
        tree = []
        res = []
        p = pRoot
        while p != None or tree != []:
            while p != None:
                tree.append(p)
                p = p.left
            if tree != []:
                p = tree.pop()
                res.append(p.val)
                p = p.right
        return res
    
    #两个栈实现
    def postorder(self, pRoot):
        if pRoot == None:
            return []
        tree = []
        res = []
        p = pRoot
        tree.append(p)
        while tree != []:
            p = tree.pop()
            res.insert(0,p.val)
            if p.left:
                tree.append(p.left)
            if p.right:
                tree.append(p.right)
        return res
    #后序遍历一个栈实现
    def PostOrder(self, pRoot):
        if pRoot == None:
            return []
        tree = []
        res = []
        tree.append(pRoot)
        p = pRoot
        while tree != []:
            #cur 为栈顶结点
            cur = tree[len(tree)-1]
            if cur.left and p != cur.left and p != cur.right:
                tree.append(cur.left)
            elif cur.right and p != cur.right:
                tree.append(cur.right)
            else:
                cur = tree.pop()
                p = cur
                res.append(cur.val)
        return res
    def traverse(self, pRoot):
        if pRoot == None:
            return []
        q = Queue.Queue()
        res = []
        if pRoot:
            q.put(pRoot)
        while not q.empty():
            level = []
            length = q.qsize()
            for i in range(length):
                p = q.get()
                level.append(p.val)
                if p.left:
                    q.put(p.left)
                if p.right:
                    q.put(p.right)
            res.append(level)
        return res
    def Deserialize(self, s):
        # write code here
        pRoot = self.CreateBinaryTree(s, 0)
        return pRoot
    def CreateBinaryTree(self, data, n):
        if len(data) > 0:
            flag = False
            for i in range(n, len(data)):
                if data[i] != '#':
                    flag = True
                    break
            if flag:
                l = 2 * n + 1
                r = 2 * n + 2
                j = n + 1
                if j < len(data):
                    while data[j] == '#':
                        if data[j:] == ['#' for x in range(j, len(data))] :
                            break
                        data.insert(l + 2*(j-n), '#')
                        data.insert(r + 2*(j-n), '#')
                        j += 1
                if data[n] != '#':
                    pRoot = TreeNode(data[n])
                    pRoot.left = self.CreateBinaryTree(data, l)
                    pRoot.right = self.CreateBinaryTree(data, r)
                    return pRoot
                else:
                    return None
            else:
                return None
        else:
            return None
test = Solution()
s = raw_input().split(',')
pRoot = test.Deserialize(s)
print test.traverse(pRoot)
print test.preorder(pRoot)
print test.inorder(pRoot)
print test.postorder(pRoot)
print test.PostOrder(pRoot)