'''
build a tree using preorder and inorder 
inputs and return a traverse of the tree left to right
example:
Input: preorder = [3,9,20,15,5,7,1], inorder = [9,3,15,5,20,7,1]
Output: [3,9,20,null,null,15,7,null,5,null,1]

     3
    / \
   9   20
  /\   / \
 n  n 15  7
      /\  /\
     n 5  n 1
'''
class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def getVal(self):
        return self.val
    def getNode(self):
        return [self.val,self.right,self.left,]

class Solution:
    def createTree(self,preorder,inorder):
        tempNode=list()
        while inorder:
            index=inorder.index(preorder[0])
            del preorder[0]
            root=Node(inorder[index])
            root.left=self.createTree(preorder,inorder[:index])
        
            root.right=self.createTree(preorder,inorder[index+1:])
            
            tempNode=root.getNode()
            if tempNode[1]:
                tempNode[1]=tempNode[1].getVal()
            if tempNode[2]:
                tempNode[2]=tempNode[2].getVal()
            print(tempNode)
            return root
                
               
    def buildTree(self,preorder,inorder):
        root=self.createTree(preorder,inorder)
        
        
        
        pass
solution=Solution()
print(solution.createTree([3,9,20,15,5,7,1],[9,3,15,5,20,7,1]))