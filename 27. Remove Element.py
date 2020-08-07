# -*- encoding: utf-8 -*-


class Solution:
    def removeElement(self, nums, val):
        i = 0
        while len(nums) != i:
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)


if __name__ == '__main__':
    S = Solution()
    num_list = [3, 2, 2, 3]
    val = 3

    out = S.removeElement(num_list, val)
    print(out)
