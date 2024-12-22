#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2: 
            return 2
        
        prev = 1
        cur = 2

        for index in range(2,n):
            prev, cur = cur, prev + cur

        return cur
        
# @lc code=end

