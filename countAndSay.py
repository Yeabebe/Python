class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        result = "1"
        
        for _ in range(2, n + 1):
            new_result = ""
            count = 1  # count consecutive digits
            
            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    new_result += str(count) + result[j - 1]
                    count = 1
            # Add last group
            new_result += str(count) + result[-1]
            
            result = new_result
        
        return result
