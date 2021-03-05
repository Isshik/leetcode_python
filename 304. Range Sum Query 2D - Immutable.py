# -*- encoding: utf-8 -*-
class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pp = self.matrix[row1:row2 + 1]
        re_int = 0
        for i in range(len(pp)):
            now_list = pp[i]
            now_list = now_list[col1:col2 + 1]
            re_int += sum(now_list)
        return re_int


if __name__ == '__main__':
    given_matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    S = NumMatrix(given_matrix)
    param_1 = S.sumRegion(1, 1, 2, 2)
    print(param_1)
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
