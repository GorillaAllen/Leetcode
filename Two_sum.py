class Solution(object):
    def twoSum(self, nums, target):
        if min(nums) < 0:
            minA = min(nums)
            for i in range(len(nums)):
                nums[i] = nums[i] - minA
            target = target - minA - minA    
    
        for i in range(0, len(nums)):
            if nums[i] > target:
                continue
            for j in range(i+1, len(nums)):
                if nums[j] > target :
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
