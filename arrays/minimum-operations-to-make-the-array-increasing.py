# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
      prev = nums[0]
      ops = 0
      for i in range(1, len(nums)):
        ops += max(0, prev-nums[i]+1)
        nums[i] += max(0, prev-nums[i]+1)
        prev = nums[i]
      return ops