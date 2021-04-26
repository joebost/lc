# 1470
# https://leetcode.com/problems/shuffle-the-array/
from typing import List

## 4/23/21
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
      l = []
      for i in range(n):
          l.append(nums[i])
          l.append(nums[n+i])
      return l