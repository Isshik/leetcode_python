# -*- encoding: utf-8 -*-


# TODO 检测超时
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        the_num = 0
        list_len = len(s)
        for i in range(list_len):
            now_num = s[i]
            if i + 1 < list_len:
                next_num = s[i + 1]
                if now_num != next_num:
                    the_num += 1

                else:
                    same_num = 2
                    q = i + 2
                    while same_num <= list_len - q:
                        next_num = s[q]
                        if next_num == now_num:
                            same_num += 1
                            q += 1

                        else:
                            the_num_list = []
                            for w in range(same_num):
                                the_num_list.append(s[q + w])
                            the_len = len(set(the_num_list))
                            if the_len == 1:
                                the_num += 1
                                break
                            else:
                                break

        return the_num


if __name__ == '__main__':
    S = Solution()
    in_str = "00110011"
    the_number = S.countBinarySubstrings(in_str)
    print(the_number)
