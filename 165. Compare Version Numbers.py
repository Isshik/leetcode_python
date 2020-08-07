# -*- encoding: utf-8 -*-


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split(".")
        b = version2.split(".")
        list_dif = []
        flag_a = 0
        if len(a) >= len(b):
            list_len = len(a)
            for i in range(len(a) - len(b)):
                b.append("0")
        else:
            list_len = len(b)
            for i in range(len(b) - len(a)):
                a.append("0")
        for i in range(list_len):
            c = int(a[i]) - int(b[i])
            list_dif.append(c)
            if c == 0:
                pass
            if c > 0:
                return 1
            if c < 0:
                return -1
        return 0


if __name__ == '__main__':
    S = Solution()
    ver_in1 = "0.1"
    ver_in2 = "1.1"
    out = S.compareVersion(ver_in1, ver_in2)
    print(out)
