"""
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note: Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed 
integer overflows.
"""

class Solution:
    def reverse(self, x):
        number = str(abs(x))
        number = number[::-1]

        if abs(int(number)) > 2147483648: #case 4
            print(0)
        
        elif x < 0: #case 3
            print(-1 * int(number))

        elif abs(int(x)) > 2147483647: #case 2
            print('')
        
        else: #case 1
            print(1 * int(number))


solution = Solution()
solution.reverse(123)
solution.reverse(-123)


"""
Test Cases:
1. If x is positive then print reverse integer
2. If x is positive and out of range then print nothing.
3. If x is neagtive then print negative reverse integer
4. If reverse number is out of range then print 0 
"""