class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            
            # compute sum of squares of digits
            total = 0
            while n:
                digit = n % 10
                total += digit * digit
                n //= 10
            
            n = total
        
        return True