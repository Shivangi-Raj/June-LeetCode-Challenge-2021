#https://leetcode.com/problems/number-of-matching-subsequences/


# Concept is to take a dictionary store all the word with the help of 1st character ,. Traverse the string
# from collection import defaultdic
class Solution:    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d={}
        cnt=0
        for item in words:
            if item[0] in d.keys():
                st=d[item[0]]
                st.append(item)
                d[item[0]]=st
            else:
                d[item[0]]=[item]
        ln=len(s)
        for i in range(ln):
            if s[i] in d.keys():
                li=d[s[i]]
                del d[s[i]]
                for item in li:
                    if len(item)==1:
                        cnt+=1
                        continue
                    if item[1] in d.keys():
                        st=d[item[1]]
                        st.append(item[1:])
                        d[item[1]]=st 
                    else:
                        d[item[1]]=[item[1:]] 
        return cnt
