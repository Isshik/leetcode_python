# -*- encoding: utf-8 -*-


class Solution(object):

    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)


if __name__ == '__main__':
    S = Solution()
    num_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    out = S.maxSubArray(num_list)
    print(out)
