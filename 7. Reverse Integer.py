# -*- encoding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        if -2 ** 31 < x < 2 ** 31 - 1:
            if x > 0:
                x = str(x)
                r = []
                for i in range(len(x)):
                    r.append(x[len(x) - i - 1])
                r = "".join(r)
                r = int(r)
                if -2 ** 31 < r < 2 ** 31 - 1:
                    return r
                else:
                    return 0
            else:
                x = abs(x)
                x = str(x)
                r = []
                for i in range(len(x)):
                    r.append(x[len(x) - i - 1])
                r = "".join(r)
                r = int(r)
                r = r * -1
                if -2 ** 31 < r < 2 ** 31 - 1:
                    return r
                else:
                    return 0
        else:
            return 0


if __name__ == '__main__':
    S = Solution()
    input_mes = 120
    out = S.reverse(input_mes)
    print(out)
