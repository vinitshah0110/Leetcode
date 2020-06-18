'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
followed by all the odd elements of A.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
'''

class Solution:
    def sortArrayByParity(self, A):
        even_list = list()
        odd_list = list()
        for item in A:
            if item%2 == 0:
                even_list.append(item)
            else:
                odd_list.append(item)
        print(even_list + odd_list)

solution = Solution()
solution.sortArrayByParity([3,1,2,4])