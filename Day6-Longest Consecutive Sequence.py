#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        # temp=set(nums)
        ln=len(nums)
        # print(ln)
        if ln==0:
            return 0
        ans=0
        
        for w in nums:
            if w-1 in nums:
                continue
            else:
                c=1
                j=w+1
                while j in nums:
                    c+=1
                    j+=1
                if c>ans:
                    ans=c 
        return ans
