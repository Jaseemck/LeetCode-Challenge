class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while(stones):
            if(len(stones)==1):
                return(stones[0])
            stones.sort(reverse=True)
            y=stones[0]
            x=stones[1]
            stones.remove(x)
            stones.remove(y)
            if(x!=y):
                stones.append(y-x)
        return 0

stones = [2,7,4,1,8,1]
ans = Solution()
res = ans.lastStoneWeight(stones)
print(res)
                
            
