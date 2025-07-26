from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Take the first word as a reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
        
        return strs[0]


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
