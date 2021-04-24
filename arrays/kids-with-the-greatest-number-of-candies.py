# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List

class Solution:
  def kidWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    m = max(candies)
    return [x+extraCandies >= m for x in candies]