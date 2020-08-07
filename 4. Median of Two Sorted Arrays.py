# -*- encoding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        len_nums = len(nums)
        if len_nums % 2 == 0:
            mid_math = int(len(nums) / 2)
            re_mid = (nums[mid_math] + nums[mid_math - 1]) / 2
        else:
            mid_math = int((len(nums) - 1) / 2)
            re_mid = (nums[mid_math])
        return re_mid


if __name__ == '__main__':
    S = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    out = S.findMedianSortedArrays(nums1, nums2)
    print(out)
