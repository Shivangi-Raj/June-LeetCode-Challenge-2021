#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def tree(preorder,ind,inorder):
    if len(inorder)==0:
        return None
    t=TreeNode(preorder[ind])
    i=inorder.index(preorder[ind])
    t.left=tree(preorder,ind+1,inorder[:i])
    ind2=ind+len(inorder[:i])+1
    t.right=tree(preorder,ind2,inorder[i+1:])
    return t


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            t=TreeNode(preorder[0])
            return t
        t=TreeNode(preorder[0])
        i=inorder.index(preorder[0])
        t.left=tree(preorder,1,inorder[:i])
        ind2=len(inorder[:i])+1
        t.right=tree(preorder,ind2,inorder[i+1:])
        return t
        
        
