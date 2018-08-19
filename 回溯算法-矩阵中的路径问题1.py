class Solution:
    def hasPath(self, board, row, col, word):
        self.col, self.row = col, row
        board = [list(board[col * i:col * i + col]) for i in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    self.b = False
                    self.search(board, word[1:], [(i, j)], i, j)
                    if self.b:
                        return True
        return False
    def search(self, board, word, dict, i, j):
        if word == "":
            self.b = True
            return
        if j != 0 and (i, j - 1) not in dict and board[i][j - 1] == word[0]:
            self.search(board, word[1:], dict + [(i, j - 1)], i, j - 1)
        if i != 0 and (i - 1, j) not in dict and board[i - 1][j] == word[0]:
            self.search(board, word[1:], dict + [(i - 1, j)], i - 1, j)
        if j != self.col - 1 and (i, j + 1) not in dict and board[i][j + 1] == word[0]:
            self.search(board, word[1:], dict + [(i, j + 1)], i, j + 1)
        if i != self.row - 1 and (i + 1, j) not in dict and board[i + 1][j] == word[0]:
            self.search(board, word[1:], dict + [(i + 1, j)], i + 1, j)

_matrix = 'abcesfcsadee'
_path = 'see'
o = Solution()
print o.hasPath(_matrix, 3, 4, _path)