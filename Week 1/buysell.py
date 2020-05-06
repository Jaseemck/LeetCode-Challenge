class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        for i in range(len(prices)-1):
            max_profit+=max(prices[i+1]-prices[i],0)
        return max_profit

n=[7,1,5,3,6,4]
ans = Solution()
res = ans.maxProfit(n)
print(res)
