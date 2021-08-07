#https://leetcode.com/problems/k-inverse-pairs-array/

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k==0:
            return 1
        dp=[[0]*(k+1) for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=1
        
        for i in range(1,n+1):
            for j in range(1,k+1):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                if j>=i:
                    dp[i][j]-=dp[i-1][j-i]
        
        ans=dp[n][k]%1000000007
        return ans
