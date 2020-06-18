'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
'''

class Solution:
    def findmax(self, nums):
        count, result = 0,0
        for number in nums:
            if number == 0:
                count = 0
            else:
                count += 1
                result = max(count, result)
        print(result)

solution = Solution() 
solution.findmax([1,1,0,1,1,1])