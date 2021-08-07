#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]   
        ans=[[1],[1,1]]
        cnt=3
        for i in range(3,numRows+1):
            v=ans[-1]
            ln=len(v)
            c=[1]*cnt
            for j in range(1,ln):
                c[j]=v[j]+v[j-1]
            cnt+=1
            ans.append(c)        
        return ans
