"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
        
#2∗(a+b+c)−(a+a+b+b+c)=c
n = int(input("Enter number of elements : "))  
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
ans = Solution()
res = ans.singleNumber(a)
print(res)
