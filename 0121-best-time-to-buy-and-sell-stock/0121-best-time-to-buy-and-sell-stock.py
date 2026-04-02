class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        s1, s2 = 0, 0
        for s2 in range(0, len(prices)):
            if prices[s2] > prices[s1]:
                profit = max(profit, prices[s2]-prices[s1])
            else:
                s1 = s2
        return profit




