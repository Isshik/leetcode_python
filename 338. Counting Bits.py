# -*- encoding: utf-8 -*-
class Solution:
    def countBits(self, num: int):
        re_list = []
        for i in range(num + 1):
            app = 0
            ll = i
            while ll != 0:
                l1 = ll // 2
                if l1 * 2 != ll:
                    app += 1
                ll = ll // 2
            re_list.append(app)
        return re_list


if __name__ == '__main__':
    S = Solution()
    num1 = 5
    S.countBits(num1)
