#https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ln=len(nums)
        if ln==1:
            if nums[0]>=left and nums[0]<=right:
                return 1
            else:
                return 0
        
        ans=0
        cnt=0
        for i in range(ln):
            m=nums[i]
            for j in range(i,ln):
                cnt+=1
                if nums[j]>m:
                    m=nums[j]
                if m>=left and m<=right:
                    # print(i,j,m)
                    ans+=1
                elif m>=right:
                    break
        print(cnt)
        return ans
