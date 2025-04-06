class Solution():
    def theMaximumAchievableX(self, num:int, t:int) -> int:
        return num + 2 * t
    
sol = Solution()
print(sol.theMaximumAchievableX(4,1))