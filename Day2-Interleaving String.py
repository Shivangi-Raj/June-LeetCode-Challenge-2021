# Day2- https://leetcode.com/problems/interleaving-string/
# Solution - Simple Dynamic Programming Solution. 

def solve(s1,s2,s3,ln1,ln2,ln3,d):
    if ln1==0 and ln2==0 and ln3==0:
        return True
    if ln3==0:
        return False
    if ln1==0:
        if s3[0:ln3]==s2[0:ln2]:
            return True
        else:
            return False
    if ln2==0:
        if s3[0:ln3]==s1[0:ln1]:
            return True
        else:
            return False    
    if (ln1,ln2,ln3) in d.keys():
        return d[ln1,ln2,ln3]
    if s1[ln1-1]==s3[ln3-1] and s2[ln2-1]!=s3[ln3-1]:
        a=solve(s1,s2,s3,ln1-1,ln2,ln3-1,d)
        d[ln1,ln2,ln3]=a
        return a
    elif s1[ln1-1]!=s3[ln3-1] and s2[ln2-1]==s3[ln3-1]:
        a=solve(s1,s2,s3,ln1,ln2-1,ln3-1,d)
        d[ln1,ln2,ln3]=a
        return a
    elif s1[ln1-1]==s3[ln3-1] and s2[ln2-1]==s3[ln3-1]:
        a1=solve(s1,s2,s3,ln1-1,ln2,ln3-1,d)
        a2=solve(s1,s2,s3,ln1,ln2-1,ln3-1,d)
        d[ln1,ln2,ln3]=a1 or a2
        return d[ln1,ln2,ln3]
    else:
        d[ln1,ln2,ln3]=False
        return False


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ln1=len(s1)
        ln2=len(s2)
        ln3=len(s3)
        if (ln1+ln2)!=ln3:
            return False
        if ln1==0 and ln2==0 and ln3==0:
            return True
        d={}
        ans=solve(s1,s2,s3,ln1,ln2,ln3,d)
        return ans
