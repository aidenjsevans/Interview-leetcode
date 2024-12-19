#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = "".join([str(digit) for digit in digits])
        numPlusOne = str(int(num) + 1)

        numArr = [int(digit) for digit in numPlusOne]

        return numArr

        
# @lc code=end

