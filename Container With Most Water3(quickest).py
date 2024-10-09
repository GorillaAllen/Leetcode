class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height)-1
        maximun = 0
        while left != right:
            if (right - left) * min(height[left], height[right]) > maximun:
                maximun = (right - left) * min(height[left], height[right])
            
            if height[left] >= height[right]:
                right -= 1
            else: left += 1
        
        return maximun


