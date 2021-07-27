class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        minimumValue = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if(prices[i]<minimumValue):
                minimumValue= prices[i]
            else:
                if(maxProfit<prices[i]-minimumValue):
                    maxProfit = prices[i] - minimumValue
        return maxProfit 