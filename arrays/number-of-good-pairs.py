from typing import List

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