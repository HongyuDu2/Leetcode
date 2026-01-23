class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 0
        hold = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1] and hold == 0:
                buy = prices[i]
                hold = 1
            if prices[i] > prices[i+1] and hold == 1:
                sell = prices[i]
                profit += sell - buy
                hold = 0
        if hold == 1:
            profit += prices[-1] - buy
        return profit