'''
Bubble search method
complexity = O(n**2) => bad
'''
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import math
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

#print(bubble([1,88,2,-1,10,99,77,3,56]))

'''
insertion sort
'''
def insertion_sort(nums):
    nums = list(nums)
    #print('nums unmodified',nums)
    for i in range(len(nums)):
        #print('i =',i)
        cur = nums.pop(i)
        #print('cur =',cur)
        j = i-1
        #print('j=',j)
        while j >=0 and nums[j] > cur:
            j -= 1
            #print('j is >=0 =>',j)
        nums.insert(j+1, cur)
        #print('nums modified',nums)
    return nums            
#print(insertion_sort([22,11,3,1,77,5,-9,0,5,66]))

'''
DEVIDE -> CONQUER -> COMBINE
* Merge search --

'''
'''
# a function to merge two lists while they are completly sorted 
else it compares each two flags in the 2 lists

'''
def merge(X:list,Y:list)->list:
    X=list(X)
    Y=list(Y)
    N=len(X)
    M=len(Y)
    Z=[]
    i,j=0,0 #iterator pointers for x,y lists
    while i<N and j<M:
        if type(X[i]) == int and type(Y[j]) == int and X[i]<=Y[j]:
            Z.append(X[i])
            i+=1
            
        else:
            Z.append(Y[j])
            j+=1
    
    Z.extend(X[i:])
    Z.extend(Y[j:])
    #print('z -->',Z)
    return Z
'''
sort usng recursive mergesort functions
-space complexity is high
'''   
def mergeSort(nums):
    nums=list(nums)
    if len(nums)<=1:
        return nums
    print('starter nums ',nums)
    N=len(nums)
    half=math.ceil(N/2)
    
    leftHalf=mergeSort(nums[:half])
    print('lefthalf',leftHalf)
    rightHalf=mergeSort(nums[half:])
    print('righthalf',rightHalf)
    
    
    sortedNums=merge(leftHalf,rightHalf)
    return sortedNums
        
        
#print(mergeSort([22,11,3,1,77,5,-9,0,5,66]))        

'''
Quick sort 

cobined of partition() and quickSort()

'''        
def partition(nums, start=0,end=None):
    if end is None:
        nums=list(nums)
        end=len(nums)-1
    
    l,r=start,end-1
    while r>l:
        if nums[l]<=nums[end]:
            l+=1
        elif nums[r]>nums[end]:
            r-=1
        else:
            nums[l],nums[r]=nums[r],nums[l]
    
    if nums[l]>nums[end]:
        nums[l],nums[end]=nums[end],nums[l]
        return l
    else:
        return end

def quickSort(nums,start=0,end=None):
    if end is None:
        nums=list(nums)
        end=len(nums)-1
    
    if start<end:
        pivot = partition(nums, start, end)
        quickSort(nums, start, pivot-1)
        quickSort(nums, pivot+1, end)
    return nums



print('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[')
print(quickSort([4,3,88,90,-3,2,1,8,333]))        
 
'''
Test time complexity and plot em
///////////////////////////////
'''
def get_var_name(var):
  for name, value in globals().items():
    if value is var:
      return name
  return None
def Otime(n,function):
    times=[]
    Ninputs=range(n)
    inputs=[]
    start0=time.time()
    while time.time()-start0<10:
        for i in range(n):
            
            for j in range(10*i):
                inputs.append(random.randint(0,n))
            start=time.time()
            function(inputs)
            end=time.time()
            elapsed=end-start
            times.append(elapsed*10)
            inputs.clear()
        print('times',times)
        print('inputs',Ninputs)
    #x = np.linspace(0, 100)
    #plt.hist(inputs)
    funcName=get_var_name(function)
    plt.plot(Ninputs, times[:n],label=f'{funcName}') # plot the x and y values
    plt.legend()
    plt.show() # show the plot
'''
Otime(100,insertionظ_sort)
Otime(100,bubble)
Otime(100,mergeSort)
'''        
    
    