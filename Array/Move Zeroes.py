'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the 
non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution:
    def moveZeroes(self,nums):
        nums.sort(key=lambda item: [item==0])
        print(nums)

solution = Solution()
solution.moveZeroes([0,1,0,3,12])