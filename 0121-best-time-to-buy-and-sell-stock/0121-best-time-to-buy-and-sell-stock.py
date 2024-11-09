'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(0, len(prices)-1):
            distance = max(prices[i+1:])-prices[i]
            profit = max(profit, distance)
            
        return profit
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')  # 初始化为一个很大的数
        max_profit = 0
        
        for price in prices:
            # 更新到目前为止的最低价格
            min_price = min(min_price, price)
            # 计算当前价格卖出时的利润，更新最大利润
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
        