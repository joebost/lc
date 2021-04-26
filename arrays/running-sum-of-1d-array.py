# 1480
# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List

## 4/17/21
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      sumList = [nums[0]]
      for i in range(1, len(nums)):
        sumList.append(sumList[i-1] + nums[i])
      return sumList