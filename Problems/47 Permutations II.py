"""
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

import itertools
class Solutions:
    def permuteunique(self, nums):
        string = itertools.permutations(nums)
        result = list()
        for item in string:
            if item not in result:
                result.append(item)
        result.sort()
        print(result)

solution = Solutions()
solution.permuteunique([1,1,2])