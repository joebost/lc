# 1108
# https://leetcode.com/problems/defanging-an-ip-address/

## 4/17/21
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))