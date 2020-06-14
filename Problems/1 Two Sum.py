""" 
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

class Solution:
    def twoSum(self,nums, target):
        mapping = {}
        for item, value in enumerate(nums):
            diff = target - value

            if diff in mapping:
                num_list = [item, mapping[diff]]
                num_list.sort()
                print(num_list)

            else:
                mapping[value] = item

solution = Solution()
solution.twoSum([2,7,11,15], 9)


'''
Answer:
item = 0 and value = 2
diff = 7
else part:
mapping[2] = 0

item = 1 and value = 7
diff = 2
if part:
item = 1 and mapping[2] = 0
num_list = [1,0]
sort()
num_list = [0,1]
'''
