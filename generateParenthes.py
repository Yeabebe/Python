class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # If the current string has used all parentheses, add to result
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add "(" if we still have opening parentheses left
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ")" if it won't make the string invalid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
