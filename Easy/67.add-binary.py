#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        binSum = ""
        carry = "0"

        maxLen = max(len(a), len(b))

        if maxLen == len(a):
            b = b.zfill(maxLen)
        else:
            a = a.zfill(maxLen)
        
        a = a[::-1]
        b = b[::-1]

        for index in range(len(a)):
            if carry == "0":
                
                if a[index] == "0" and b[index] == "0":
                    binSum += "0"
                elif a[index] == "1" and b[index] == "1":
                    binSum += "0"
                    carry = "1"
                else:
                    binSum += "1"
            
            else:
                
                if a[index] == "0" and b[index] == "0":
                    binSum += "1"
                    carry = "0"
                elif a[index] == "1" and b[index] == "1":
                    binSum += "1"
                else:
                    binSum += "0"
        
        if carry == "1":
            binSum += "1"
        
        binSum = binSum[::-1]

        return binSum
     
# @lc code=end
