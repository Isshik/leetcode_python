# -*- encoding: utf-8 -*-


class Solution:
    def threeSumClosest(self, nums, target):
        for i in range(len(nums) - 2):
            firts_math = nums[i]
            for q in range(len(nums) - i - 1):
                secend_math = nums[q + i + 1]
                for w in range(len(nums) - i - q - 2):
                    third_math = nums[q + i + w + 2]
                    if i == q == w == 0:
                        math_sum = firts_math + secend_math + third_math
                        min_math = abs(math_sum - target)
                        re_math = math_sum
                    else:
                        math_sum = firts_math + secend_math + third_math
                        if abs(math_sum - target) < min_math:
                            re_math = math_sum
                            min_math = abs(math_sum - target)
                            if min_math == 0:
                                return re_math
        return re_math


if __name__ == '__main__':
    S = Solution()
    input_nums = [-1, 2, 1, -4]
    target = 1
    out = S.threeSumClosest(input_nums, target)
    print(out)
