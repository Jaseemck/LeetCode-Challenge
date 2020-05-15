class Solution:
    def findMaxLength(self, nums):
        counter = {}
        counter[0] = -1
        
        max_count = 0
        count = 0
        
        for i in range(0, len(nums)):
            if nums[i] == 1: 
                count = count + 1
            else:
                count = count - 1
                
            if count in counter:
                max_count = max(max_count, i - counter[count])
            else:
                counter[count] = i

        return max_count

nums = [0,0,1,0,0,0,1,1]
ans = Solution()
res = ans.findMaxLength(nums)
print(res)
