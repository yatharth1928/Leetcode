class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        maxi=0

        for x in prices:
            if x<buy:
                buy=x
            else:
                profit=x-buy
                maxi=max(profit,maxi)
        return maxi

        