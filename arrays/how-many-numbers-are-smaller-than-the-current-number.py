# 1365
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from typing import List

# rt n^2 s n
## 4/24/21
class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
      val = nums[i]
      res.append(0)
      for j in range(len(nums)):
        if nums[j] < val:
          res[i]+=1
    return res

# rt nlogn, s 2n
## 4/24/21
class Solutionv2:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    sorted = nums.copy()
    sorted.sort()
    res = [0] * len(nums)
    for i in range(len(nums)):
      res[i] = sorted.index(nums[i])
    return res