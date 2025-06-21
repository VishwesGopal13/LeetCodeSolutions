class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        maxprofit=0
        for price in prices:
            profit=price-minimum
            maxprofit=max(maxprofit,profit)
            minimum=min(minimum,price)
        return maxprofit