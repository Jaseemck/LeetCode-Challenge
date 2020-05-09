from collections import deque 
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def stk(string):
            s = deque()
            for i in string:
                if i!="#":
                    s.append(i)
                elif s:
                    s.pop()
            return str(s)
        if stk(S)==stk(T):
            return True
        return False
       
first = "ab#c"
second = "#ad#c"
ans = Solution()
res = ans.backspaceCompare(first,second)
print(res)
