#coding=utf-8
#按照 j+1 ,j-1, i+1 ,i-1的 顺序进行试探，
# 因为本文发现，若i-1,i+1顺序改变后，试探结果失败。
class Solution:
    # 函数功能：找到初始位置
    def hasPath(self, matrix, rows, cols, path):
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    self.flag = False
                    self.find_path(list(matrix),rows,cols,path[1:],i,j)
                    if self.flag:
                        return True
        #  判断这个函数是否是True, 若是则返回 True
        return False

    def find_path(self,matrix,rows,cols,path,i,j):
    # 因为要试探，所以需要传进位置参数i,j

        if not path:  #首先判断是否全部走完
            self.flag = True
            return
        #将走过的位置标记为0，所以前面需要将字符串矩阵改成可变对象list
        matrix[i*cols+j] = '0'
        if j+1 < cols and matrix[i*cols+j+1] == path[0]:
            self.find_path(matrix,rows,cols,path[1:],i,j+1)
        if j-1 >= 0 and matrix[i*cols+j-1] == path[0]:
            self.find_path(matrix,rows,cols,path[1:],i,j-1)
        if i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            self.find_path(matrix, rows, cols, path[1:], i + 1, j)
        if i-1 >= 0 and matrix[(i-1)*cols+j] == path[0]:
            self.find_path(matrix,rows,cols,path[1:],i-1,j)

# 调用测试
_matrix = 'abcesfcsadee'
_path = 'see'
o = Solution()
print o.hasPath(_matrix, 3, 4, _path)