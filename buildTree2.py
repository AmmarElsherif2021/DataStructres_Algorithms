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
    
    level=0
        
    def getVal(self):
        return self.val
    def getNode(self):
        return [self.val,self.right,self.left]
    def getLevel(self):
        return self.level
    def setLevel(self,level):
        self.level=level

class Solution:
    
    def mirror(self,Node):
        if Node ==None:
            return
        else:
            temp = Node
            self.mirror(Node.left)
            self.mirror(Node.right)
            temp = Node.left
            Node.left = Node.right
            Node.right = temp
    
    def createTree(self,preorder,inorder):
        global tree
        tempNode=list()
        while inorder:
            index=inorder.index(preorder[0])
            del preorder[0]
            root=Node(inorder[index])
            
            
            root.left=Node()
            root.right=Node()
            
            
            root.left=self.createTree(preorder,inorder[:index])
            
            root.right=self.createTree(preorder,inorder[index+1:])
            
                
            
               
            
            #try to reverse left and right
            #root.left,root.right=root.right,root.left
            
            
            return root
    treeList=[]
    def traverse(self,root):
        
        if root.left:
            root.left.setLevel(root.getLevel()+1)
        if root.right:
            root.right.setLevel(root.getLevel()+1)   
        tempNotion=root.getNode()
        
        #tempNotion.append(root.getLevel())
        
        if tempNotion[1]:
            tempNotion[1]=tempNotion[1].getVal()
        if tempNotion[2]:
            tempNotion[2]=tempNotion[2].getVal()
        tempNotion[1],tempNotion[2]=tempNotion[2],tempNotion[1]
        
        print(tempNotion)
        self.treeList.append(tempNotion)
        
        if root.left:
            self.traverse(root.left)
        if root.right:
            self.traverse(root.right)
    
    treeDict={}
    def traverseTree(self,root):
        
        
         
    
    def buildTree(self,preorder,inorder):
        root=self.createTree(preorder,inorder)
        self.traverse(root)
        print(self.treeList)
        #self.mirror(root)
        s=[]
        
        for node in self.treeList:
            #node[1],node[2]=node[2],node[1]
            #s.append(node[0])
            
            for i in range(3):
                s.append(node[i])
  
        return s
        
        
        
        
solution=Solution()
s1=solution.buildTree([3,9,20,15,5,7,1],[9,3,15,5,20,7,1])
print(s1)