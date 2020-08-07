# -*- encoding: utf-8 -*-

class Solution:
    def maxArea(self, height):
        max_area = 0
        area = 0
        left = 0
        right = len(height) - 1
        for i in range(len(height) - 1):
            if height[left] > height[right]:
                H = height[right]
                area = H * (right - left)
                right = right - 1
            else:
                H = height[left]
                area = H * (right - left)
                left = left + 1
            if area > max_area:
                max_area = area
        return max_area


if __name__ == '__main__':
    S = Solution()
    input_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    out = S.maxArea(input_list)
    print(out)
