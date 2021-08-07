#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


class Solution:
    def removeDuplicates(self, s: str) -> str:
        ln=len(s)
        if len==1:
            return s
        stack=[]
        for i in range(ln):
            if len(stack)!=0:
                if s[i]==stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        if len(stack)==0:
            return ""
        ans="".join(stack)
        return ans
        
