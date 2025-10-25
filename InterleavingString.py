class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If lengths don't match, it's impossible
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True  # Empty strings interleave to form empty string

        # Fill the first row (using only s2)
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the first column (using only s1)
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Fill the rest of the DP table
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):

                from_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = from_s1 or from_s2

        return dp[len(s1)][len(s2)]
