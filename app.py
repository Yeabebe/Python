from typing import List
class Solution:
    def convert_temp(self, celsius: float) -> List[float]:
        K = celsius + 273.15
        F = celsius * 1.80 + 32.00
        return [K, F]
    
sol = Solution()
print(sol.convert_temp(60))