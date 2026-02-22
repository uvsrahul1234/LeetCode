class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force T:O(N2) S:O(1)
        n = len(prices)
        diff = 0
        for i in range(n):
            for j in range(i+1, n):
                diff = max(diff, prices[j] - prices[i])
        
        return diff
