#https://leetcode.com/problems/reverse-linked-list-ii/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head,k):
    
    curr=head
    i=0
    prev=None
    nexts=None
    while(i<k and curr!=None):
        i+=1
        nexts=curr.next
        curr.next=prev
        prev=curr
        curr=nexts
    
    # print(head.val,prev.val,curr.val)
    head.next=curr
    return prev

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        k=right-left+1
        if head.next==None:
            return head
        i=1
        prev=None
        temp=head
        while(temp!=None and i<left):
            i+=1
            prev=temp
            temp=temp.next
        if temp==None:
            return head
        # print(prev.val,temp.val)
        if left==1:
            head=reverse(temp,k)
        else:
            prev.next=reverse(temp,k)
        return head
        