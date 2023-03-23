'''
Given two integer arrays preorder and inorder 
where preorder is the preorder traversal of a binary tree and inorder is 
the inorder traversal of the same tree,
construct and return the binary tree.

example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

'''
import math
class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.left=left
        self.right=right
        self.value=value
    
    def getNode(self):
        return self.value
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
def buildTree(preorder,inorder):
    if inorder:
        i=inorder.index(preorder[0])
        del preorder[0]
        root=TreeNode(inorder[i])
        root.left=buildTree(preorder,inorder[:i])
        root.right=buildTree(preorder,inorder[i+1:])
        
        return root
output=[]
tree=buildTree([3,9,20,15,7],[9,3,15,20,7])
while tree.getNode():
    output.append(tree.getNode())
    output.append(tree.getLeft())
    output.append(tree.getRight())
print(output)
    