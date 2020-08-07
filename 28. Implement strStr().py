# -*- encoding: utf-8 -*-


class Solution:
    def strStr(self, haystack, needle):
        if len(haystack) == len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        haystack = list(haystack)
        a = len(needle)
        b = len(haystack)
        Q = 0
        while a - 1 != b:
            c = ""
            for i in range(a):
                c = c + haystack[i]
            if c == needle:
                return Q
            else:
                haystack.remove(haystack[0])
                Q += 1
                b = len(haystack)
        else:
            return -1


if __name__ == '__main__':
    S = Solution()
    haystack = "hello"
    needle = "ll"
    out = S.strStr(haystack, needle)
    print(out)
