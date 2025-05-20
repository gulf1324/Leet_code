class Solution:
    def maxArea(self, height: list[int]) -> int:
        right = len(height) - 1
        left = 0
        area = (right-left)* min(height[right],height[left])
        while left < right:
            if height[right] < height[left]:
                right -=1
            else :
                left += 1
            if area < (right-left)* min(height[right],height[left]):
                area = (right-left)* min(height[right],height[left])
        return area
################################################################################
s= Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
# >>> 49