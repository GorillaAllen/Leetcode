class Solution:
    def maxArea(self, height) -> int:
        maximun = 0
        for i in range(len(height)-1):
            for j in range(i,len(height)):
                if min(height[i], height[j]) * (j-i) > maximun:
                    maximun = min(height[i], height[j]) * (j-i)
            
        return maximun