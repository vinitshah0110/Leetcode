'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
'''

class Solution:
    def removeElement(self,nums,val) -> int:
        for _ in range(nums.count(val)):
            nums.remove(val)
        print(nums) 

solution = Solution()
solution.removeElement([3,2,2,3],3)