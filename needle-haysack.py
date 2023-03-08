import re
import math
def Lps(pattern):
    lps=[0]
    patternList=[c for c in pattern]
    j=1     #pointer to iterate the main pattern list
    i=int() #pointer to iterate the suffix
    k=int() #pointer to iterate the prefix
    value=int() #value of the longest pattern prefix which is also a suffix
    
    while patternList and j<len(patternList):
        value = 0
        i = 0
        k =1 #int(math.ceil(j/2)) 
        #print('---------------------pattern',pattern[:j])
        iteration=k #save original k pointer position for each j
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
                 
            #print('value ',value)

        lps.append(value)   
        j+=1
      
    return lps        
    
def KMP( haystack, needle):
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
    lps=Lps(needle)
    exist=0
    returned=int()
    while j<N and i<M:
        if pattern[j]==txtList[i]:
            j+=1
            exist+=1
            i+=1
        else:
            if j>0:
                j=lps[j-1]
                
            else:
                j=0 
                i+=1
        print('------i',i)
        print('exist',exist)
        print('j',j)   
    
    if j==len(pattern):
        return i-j
    else:
        return -1
       
    
 
        
        

haystack='mississippi'
needle='issippi'
        
print(KMP( haystack, needle))
#print(Lpc('AAABAAA'))