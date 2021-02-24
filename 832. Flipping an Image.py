# -*- encoding: utf-8 -*-
class Solution:
    def flipAndInvertImage(self, A):
        B = []
        for li in A:
            lii = [ele for ele in reversed(li)]
            lii = [int(ele == 0) for ele in lii]
            B.append(lii)
        return B

if __name__ == '__main__':
    Input = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    Output = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    S = Solution()
    S.flipAndInvertImage(Input)
