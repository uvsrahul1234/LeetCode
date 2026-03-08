class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Sliding Window T:O(N) S:O(1)
        l, r = 0, 1
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
        
        # Brute Force T:O(N2) S:O(1)
        # n = len(prices)
        # diff = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         diff = max(diff, prices[j] - prices[i])
        
        # return diff

