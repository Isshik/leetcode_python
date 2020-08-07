# -*- encoding: utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, q in enumerate(nums):
            another = target - q
            if another in hashmap:
                b = nums.index(another)
                return i, b
            hashmap[q] = i


if __name__ == '__main__':
    S = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    out = S.twoSum(nums, target)
    print(out)