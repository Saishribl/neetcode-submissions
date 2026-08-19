class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = 1
        maxP = 0

        while high < len(prices):
            if prices[low] < prices[high]:
                profit = prices[high] - prices[low]
                if profit > maxP:
                    maxP = profit
            else:
                low = high
            high+=1
        return maxP