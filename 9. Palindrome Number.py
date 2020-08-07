# -*- encoding: utf-8 -*-


class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        x = str(x)
        flag = 0
        if len(x) == 1:
            return True
        if len(x) % 2 == 0:
            for i in range(int(len(x) / 2)):
                if x[i] == x[len(x) - i - 1]:
                    flag = 0
                else:
                    return False
        else:
            for i in range(int((len(x) - 1) / 2)):
                if x[i] == x[len(x) - i - 1]:
                    flag = 0
                else:
                    return False
        if flag == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    S = Solution()
    input_num = 121
    out = S.isPalindrome(input_num)
    print(out)
