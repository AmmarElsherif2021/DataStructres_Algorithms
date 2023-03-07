import re
import math
def Lpc(pattern):
    lpc=[0]
    patternList=[c for c in pattern]
    print('th epattern list __',patternList)
    i=int()
    iQ=list()
    kQ=list()
    
    j=1
    k=int()
    value=int()
    
    while patternList and j<len(patternList):
        value = 0
        i = 0
        k =1 #int(math.ceil(j/2))
        print('---------------------pattern',pattern[:j])
        iteration=k
        while k<=j : 
            
            if patternList[i]==patternList[k]:
                value+=1
                i+=1
                k+=1
                
            else:
                value=0
                i=0
                iteration+=1
                k=iteration
                 
            print('value ',value)
            
            
           
            
            
           
           
        
        lpc.append(value)
       
        j+=1
      
    return lpc        
    
def strStr( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    you need to make KMP algorithm
    """
    txtList=[c for c in haystack]
    pattern=[c for c in needle]
    i=0
    j=0
    M=len(txtList)
    N=len(pattern)
    lps=Lpc(needle)
    exist=0
    while j<N and i<M:
        if pattern[j]==txtList[i]:
            j+=1
            exist+=1
        else:
            if j>0:
                j=lps[j-1]
                exist=lps[j-1]
            else:
                j=0 
                exist=0
        
        if exist==len(pattern):
            
            print('index -->',i-exist+1)
        i+=1
    
    return i-exist+1
        
        

haystack='ABA ABAA ABABA'
needle='BAB'
        
strStr( haystack, needle)
#print(Lpc('AAABAAA'))