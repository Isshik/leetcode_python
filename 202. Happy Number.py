# -*- encoding: utf-8 -*-


class Solution:
    def isHappy(self, n):
        r = 0
        hamath = 0
        while n != 1:
            n = str(n)
            for i in range(len(n)):
                hamath = hamath + int(n[i]) * int(n[i])
            n = hamath
            hamath = 0
            r = r + 1
            if r > 10:
                return False
        else:
            return True


if __name__ == '__main__':
    S = Solution()
    in_num = 19
