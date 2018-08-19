class Solution():
    def movingCount(self, threshold, rows, cols):
        board = [[0 for i in range(cols)] for j in range(rows)]
        global acc
        acc = 0
        def block(r,c):
            s = sum(map(int, str(r) + str(c)))
            return s < threshold
        def traverse(r,c):
            global acc
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if board[r][c] != 0:
                return
            if board[r][c] == -1 or not block(r,c):
                board[r][c] = -1
                return
            board[r][c] = 1
            acc += 1
            traverse(r-1, c)
            traverse(r+1, c)
            traverse(r, c-1)
            traverse(r, c+1)
        traverse(0, 0)
        return acc
test = Solution()
print test.movingCount(3,3,3)