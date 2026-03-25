class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        s1, s2 = 0, 0
        while s2 < len(prices)-1:
            s2 += 1
            if prices[s1] > prices[s2]:
                s1 = s2
            profit = max(profit, prices[s2]-prices[s1])
        return profit



