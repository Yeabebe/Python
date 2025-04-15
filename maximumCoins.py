class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort(reverse = True)
        n = len(piles) // 3
        total = 0

        for i in range(1, 2 * n, 2):
            total += piles[i]

        return total
        
