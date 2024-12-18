#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        targetDict = {}

        for index, num in enumerate(nums):
            
            if num not in targetDict:
                targetDict[target - num] = index
            else:
                indices.append(targetDict[num])
                indices.append(index)
        
        return indices

# @lc code=end

