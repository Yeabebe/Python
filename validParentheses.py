class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping:  # it is a closing bracket
                top_element = stack.pop() if stack else '#'  # '#' means no match
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)  
                
        return not stack  
