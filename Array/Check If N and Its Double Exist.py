'''
Given an array of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 
Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
'''

class Solution:
    def checkIfExist(self,nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] == nums[j]*2 or nums[i] == nums[j]*0.5):
                    print('True')
        print('False')   

solution = Solution()
solution.checkIfExist([7,1,14,11])