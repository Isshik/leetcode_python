# -*- encoding: utf-8 -*-


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return None
        i = 0
        while len(nums) != i + 1:
            a = nums[i]
            b = nums[i + 1]
            if a == b:
                nums.remove(nums[i + 1])
            else:
                i += 1
        return len(nums)


if __name__ == '__main__':
    S = Solution()
    nums_list = [1, 1, 2]
    out = S.removeDuplicates(nums_list)
    print(out)
