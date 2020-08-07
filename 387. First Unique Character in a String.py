# -*- encoding: utf-8 -*-


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {c: s.count(c) for c in set(s)}
        # 找到并返回首个满足出现次数为一的字符
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i

        return -1


if __name__ == '__main__':
    S = Solution()
    in_str = "leetcode"
    out = S.firstUniqChar(in_str)
    print(out)
