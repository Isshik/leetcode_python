# -*- encoding: utf-8 -*-

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = i = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                count += 1
            else:
                i += 1

        nums.extend([0] * count)

        return nums


if __name__ == '__main__':
    Input = [0, 1, 0, 3, 12]
    S = Solution()
    re = S.moveZeroes(Input)
    print(re)
