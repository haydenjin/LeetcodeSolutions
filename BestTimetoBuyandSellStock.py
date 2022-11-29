class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        buyIndex = 0
        sellIndex = 1
        
        while sellIndex != len(prices):
            result = prices[sellIndex] - prices[buyIndex]
            if result > maxProfit:
                maxProfit = result    
            elif prices[buyIndex] >= prices[sellIndex]:
                buyIndex = sellIndex
                sellIndex += 1
            else:
                sellIndex += 1
        
        
        return maxProfit
