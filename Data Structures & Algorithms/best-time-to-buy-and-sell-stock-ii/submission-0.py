class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pricehas = set(prices)
        final = 0
        for i in range(1, len(prices)):
            if prices[i-1]<prices[i]:
                final -= prices[i-1]
                final += prices[i]
        return final