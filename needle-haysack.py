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
    r=-1
    
    matches=re.finditer(needle, haystack)
    if matches:
        while r ==-1:
            for match in matches:
                r=match.start()
    return r
        

print(Lpc('AAABAAA'))