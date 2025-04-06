class Solution:
    def strStr(self, hystack: str, needle: str) -> int:
        if needle in hystack:
            return hystack.index(needle)
        else:
            return -1
        
sol = Solution()
print(sol.strStr("hello", "ll"))