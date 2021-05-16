# 1281
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


## 5/16/21
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        prod = 1
        summ = sum([int(c) for c in s])
        for c in s:
          num = int(c)
          prod *= num

        return prod - summ

## 5/16/21
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, summ = 1, 0
        while n != 0:
          prod *= (n % 10)
          summ += (n % 10)
          n = int(n / 10)
        return prod - summ