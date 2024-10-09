def twoSum(nums, target):
    target= target / 2
    larger = []
    even = []
    smaller = []
    for i in range(len(nums)):
        if nums[i] > target:
            larger.append(i)
            larger.append( nums[i] - target)
        if nums[i] < target:
            smaller.append(i)
            smaller.append(target - nums[i])
        if nums[i] == target:
            even.append(i)
            even.append(nums[i])
            if len(even) == 4:
                return [even[0],even[2]]
    # print(larger, smaller, even)
    for i in range(1,len(larger),2):
        for j in range(1,len(smaller),2):
            if larger[i] == smaller[j]:
                return [larger[i-1], smaller[j-1]]
               
print(twoSum([2,7,11,15],9))
            
