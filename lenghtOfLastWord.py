class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces and split
        words = s.rstrip().split(" ")
        return len(words[-1])
