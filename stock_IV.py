from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # Case 1: unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # Case 2: DP for limited k
        dp = [[0, float('-inf')] for _ in range(k + 1)]

        for price in prices:
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + price)
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - price)

        return dp[k][0]
