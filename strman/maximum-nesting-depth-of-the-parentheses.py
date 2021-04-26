# 1614
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

## 4/25/21
class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        curDepth = 0
        for c in s:
          if c == '(':
            curDepth += 1
          if c == ')':
            curDepth -= 1
          maxDepth = max(maxDepth, curDepth)
        return maxDepth