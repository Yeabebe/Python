class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        result = 0
        sign = 1

        #Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        #Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        #Read digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
        #Check for overflow before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        return sign * result
