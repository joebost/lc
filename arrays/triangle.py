from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * len(triangle[-1])
        for level in triangle[::-1]:
            if len(level) == len(dp):
                dp = level
            else:
                for i in range(len(level)):
                    maxIndex = len(level)
                    dp[i] = min(dp[i]+level[i], dp[min(i+1, maxIndex)]+level[i])

        return dp[0]