# -*- encoding: utf-8 -*-


class Solution:
    def maximumGap(self, nums) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_nu = -1
        for i in range(len(nums)):
            if i == 0:
                pass
            num_c = nums[i] - nums[i - 1]
            if num_c > max_nu:
                max_nu = num_c
        return max_nu


if __name__ == '__main__':
    S = Solution()
    in_list = [3, 6, 9, 1]
    out = S.maximumGap(in_list)
    print(out)