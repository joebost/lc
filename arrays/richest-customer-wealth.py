# https://leetcode.com/problems/richest-customer-wealth/
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(x) for x in accounts])

class Solutionv2:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
