'''
Given an array, replace every element in that array with the greatest element among the elements to its right, and 
replace the last element with -1.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 
Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''

class Solution:
    def replaceElements(self, nums):
        arr = list()
        for item in range(1,len(nums)):
            arr.append(max(nums[item:]))
        arr.append(-1)
        print(arr)

solution = Solution()
solution.replaceElements([17,18,5,4,6,1])