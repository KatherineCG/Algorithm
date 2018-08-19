import Queue
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
class BinaryTree:
    def PreOrder(self, tree, res):
        if not tree:
            return []
        res.append(tree.val)
        self.PreOrder(tree.left, res)
        self.PreOrder(tree.right, res)
        return res
    def InOrder(self, tree, res):
        if not tree:
            return []
        self.InOrder(tree.left, res)
        res.append(tree.val)
        self.InOrder(tree.right, res)
        return res
    def PostOrder(self, tree, res):
        if not tree:
            return []
        self.PostOrder(tree.left, res)
        self.PostOrder(tree.right, res)
        res.append(tree.val)
        return res
    def preorder(self, bintree):
        if not bintree:
            return []
        res = []
        tree = []
        p = bintree
        while p or tree:
            while p:
                tree.append(p)
                res.append(p.val)
                p = p.left
            if tree:
                p = tree.pop()
                p = p.right
        return res
    def inorder(self, bintree):
        if not bintree:
            return []
        res = []
        tree = []
        p = bintree
        while p or tree:
            while p:
                tree.append(p)
                p = p.left
            if tree:
                p = tree.pop()
                res.append(p.val)
                p = p.right
        return res
    def postorder(self, bintree):
        if not bintree:
            return []
        tree = []
        res = []
        tree.append(bintree)
        while tree:
            p = tree.pop()
            res.insert(0, p.val)
            if p.left:
                tree.append(p.left)
            if p.right:
                tree.append(p.right)
        return res
    def traverse(self, tree):
        if not tree:
            return []
        res = []
        q = Queue.Queue()
        q.put(tree)
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
                        if data[j:] == ['#' for x in range(j, len(data))]:
                            break
                        data.insert(l + 2 * (j - n), '#')
                        data.insert(r + 2 * (j - n), '#')
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
test = BinaryTree()
treeinput = [1,2,3,4,5,6,7]
tree = test.CreateBinaryTree(treeinput, 0)

print test.traverse(tree)
print test.PreOrder(tree, [])
print test.preorder(tree)
print test.InOrder(tree, [])
print test.inorder(tree)
print test.PostOrder(tree, [])
print test.postorder(tree)
