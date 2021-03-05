# -*- encoding: utf-8 -*-

class Solution:
    def transpose(self, matrix):
        n = len(matrix)
        n1 = len(matrix[0])
        re_list = []
        for i in range(n1):
            nn = []
            for ii in range(n):
                nn.append(matrix[ii][i])
            re_list.append(nn)
        return re_list


if __name__ == '__main__':
    S = Solution()
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    S.transpose(matrix1)
