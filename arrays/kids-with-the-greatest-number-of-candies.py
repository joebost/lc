# 1431
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List

## 4/17/21
class Solution:
  def kidWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    m = max(candies)
    return [x+extraCandies >= m for x in candies]