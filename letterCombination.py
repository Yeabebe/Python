from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping digits to letters
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index: int, path: str):
            # If path is complete
            if index == len(digits):
                result.append(path)
                return
            # Get the letters corresponding to the current digit
            possible_letters = digit_to_char[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result

sol = Solution()
print(sol.letterCombinations("43"))
