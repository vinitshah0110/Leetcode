"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

import itertools
class Solutions:
    def permute(self, nums):
        string = itertools.permutations(nums)
        result = [list(item) for item in string]
        print(result)

solution = Solutions()
solution.permute([1,2,3])