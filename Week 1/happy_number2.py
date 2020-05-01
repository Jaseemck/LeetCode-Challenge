class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)

            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n //= 10
            n = _sum

        return n == 1

n=19
ans = Solution()
res = ans.isHappy(n)
print(res)
