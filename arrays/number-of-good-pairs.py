# 1512
# https://leetcode.com/problems/number-of-good-pairs/

from typing import List

## 4/23/21
class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:
    m = {}
    r = 0
    for x in nums:
      if x in m:
        r += m[x]
        m[x] += 1
      else:
        m[x] = 1
    return r