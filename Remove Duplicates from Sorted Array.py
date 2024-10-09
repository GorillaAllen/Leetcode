#It does everything Leetcode requires. But leetcode won't accept it
import numpy as np

def removeDuplicates(nums):
    np_nums = np.array(nums)
    np_nums = np.unique(np_nums)
    nums = np_nums.tolist()
    return nums

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))