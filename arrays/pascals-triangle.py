# 118
# https://leetcode.com/problems/pascals-triangle/
from typing import List

## 4/28/21
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      res = [[1]]
      for i in range(1, numRows):
        prev_row = res[-1]
        row = [1] * (i+1)
        for j in range(1, len(row)-1):
          row[j] = prev_row[j] + prev_row[j-1]
        res.append(row)
      return res