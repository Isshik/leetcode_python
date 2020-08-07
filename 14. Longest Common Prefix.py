# -*- encoding: utf-8 -*-


class Solution:

    def longestCommonPrefix(self, strs) -> str:
        str_flag = ""
        if len(strs) == 0:
            return str_flag
        if len(strs) == 1:
            str_flag = str_flag + strs[0]
            return str_flag
        shortest = len(strs[0])
        for i in range(len(strs)):
            nowLong = len(strs[i])
            if shortest >= nowLong:
                shortest = nowLong
        if shortest == 0:
            return str_flag

        pub_start = []
        for i in range(shortest):
            for w in range(len(strs)):
                if w == 0:
                    pub_start.append(strs[w][i])
                else:
                    now = strs[w][i]
                    if now == pub_start[i]:
                        pass
                    else:
                        return str_flag
            str_flag = str_flag + pub_start[i]
        return str_flag


if __name__ == '__main__':
    S = Solution()
    input_list = ["flower","flow","flight"]
    out = S.longestCommonPrefix(input_list)
    print(out)
