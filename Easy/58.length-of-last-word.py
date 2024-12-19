#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = s.split(" ")
        pointer = -1

        while True:
            if not wordList[pointer]:
                pointer -= 1
            else:
                return len(wordList[pointer])
        
# @lc code=end

