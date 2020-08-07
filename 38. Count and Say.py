# -*- encoding: utf-8 -*-


class Solution:
    def countAndSay(self, n):
        w = 1
        if n == 1:
            return "1"
        for s in range(n - 1):
            listA = []
            Str_last = ""
            w = str(w)
            for i, q in enumerate(w):
                if i > 0 and q not in listA:
                    Str_last = Str_last + str(len(listA)) + str(listA[0])
                    listA = []

                if i == len(w) - 1:
                    listA.append(q)
                    Str_last = Str_last + str(len(listA)) + str(listA[0])
                listA.append(q)

            w = Str_last
        return Str_last


if __name__ == '__main__':
    S = Solution()
    input_num = 4
    out = S.countAndSay(input_num)
    print(out)
