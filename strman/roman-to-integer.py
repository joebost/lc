# 13
# https://leetcode.com/problems/roman-to-integer/

## 5/1/21
class Solution:
    def romanToInt(self, s: str) -> int:
        rtoi = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        replace = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        res = 0
        for x in replace.keys():
            if x in s:
                res += replace[x]
            s = s.replace(x, "")

        for x in s:
            res += rtoi[x]

        return res

## 5/1/21
class Solutionv2:
    def romanToInt(self, s: str) -> int:
        rtoi = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0
        for i in range(len(s) - 1):
            if rtoi[s[i]] < rtoi[s[i+1]]:
                res -= rtoi[s[i]]
            else:
                res += rtoi[s[i]]
        return res + rtoi[s[-1]]