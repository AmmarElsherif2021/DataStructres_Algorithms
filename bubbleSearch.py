'''
Bubble search method
'''
#import test
def bubble(inList):
    #declare pointers vars i,j
    N=len(inList)
    i=int()
    j=N
    
    #tempo. handler
    temp=int()
    while j>=0 :
        i=0
        while i<j-1:
            if inList[i]>inList[i+1]:
                temp=inList[i]
                inList[i]=inList[i+1]
                inList[i+1]=temp
            i+=1
        j-=1
    return inList

print(bubble([1,88,2,-1,10,99,77,3,56]))
'''
for test in tests:
    print(bubble(test['input'])==test['output'])
'''