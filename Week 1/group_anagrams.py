class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        anagrams = defaultdict(list)
        for s in strs:
            anagrams[str(sorted(s))].append(s)

        return list(anagrams.values())

n=["eat", "tea", "tan", "ate", "nat", "bat"]
ans=Solution()
res=ans.groupAnagrams(n)
print(res)
