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
    
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getValue(self):
        return self.value
    def getNode(self):
        dna=[self.value]
        if self.left:
            dna.append(self.getLeft().getValue())
        else:
            dna.append('Null')
        if self.right:
            dna.append(self.getRight().getValue())
        else:
            dna.append('Null')
        return dna
    
def buildTree(preorder,inorder):
    nodesArr=[]
    def initTree(preorder,inorder):
        preorder2=preorder
        if inorder:
            temp=TreeNode()
            #tree=[0]*((2**len(inorder))-1)
            i=inorder.index(preorder[0])
            
            
            
            
            root=TreeNode(inorder[i])
            del preorder[0] 
            nodesArr.append(root)
            try:
                root.left=initTree(preorder,inorder[:i])
            except:
                root.left=initTree(preorder,[])
            try:
                root.right=initTree(preorder,inorder[i+1:])
            except:
                root.right=None
            
            return root


    def fillList(preorder,inorder):
        temp=initTree(preorder,inorder)
        print(nodesArr)
        nested=list()
        for node in nodesArr:
            nested.append(node.getNode())
        while nested[-1][-1]=='Null' and nested[-1][-2]=='Null':
            del nested[-1]
        while len(nested)>1:
            for node in nested[1]:
                if node not in nested[0]:
                    nested[0].append(node)
                if node =='Null':
                    nested[0].append(node)
            del nested[1]
        return(nested[0])
    
    return fillList(preorder,inorder)
print(buildTree([1,2,3,4,5],[4,2,5,3,1]))
    

    