#https://leetcode.com/problems/generate-parentheses/

def generate(ln,s,ans,cnt,n,c):
    if ln==0 and cnt==0 and c==n:
        a="".join(s)
        ans.append(a) 
        return
    if cnt==0:
        s.append("(")
        generate(ln-1,s,ans,cnt+1,n,c+1)
    elif c==n:
        s.append(")")
        generate(ln-1,s,ans,cnt-1,n,c) 
    else:
        s.append("(")
        generate(ln-1,s,ans,cnt+1,n,c+1)
        s.pop()
        s.append(")")
        generate(ln-1,s,ans,cnt-1,n,c)
    s.pop()
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
        ln=2*n
        ans=[]
        s=["("]
        cnt=1
        c=1
        generate(ln-1,s,ans,cnt,n,c)
        return ans
