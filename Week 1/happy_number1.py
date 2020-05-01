class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sums=[]
        total=n
        def digit(num):
            digits= []
            while num:
                digits.append(num%10)
                num=num//10
            return digits
            
        while True:
            l=digit(total)
            total=0
            for i in l:
                total+=i*i
            print(total)
            if total==1:
                return True
            elif total in sums:
                return False
            else:
                sums.append(total)

n=19
ans = Solution()
res = ans.isHappy(n)
print(res)
	
