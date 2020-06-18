'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
'''


class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        while i < len(nums):
            if nums.count(nums[i]) > 1:
                nums.remove(nums[i])
            else:
                i += 1
        print(nums)   

solution = Solution()
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])