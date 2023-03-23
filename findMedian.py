
'''
find median of two sorted lists
'''
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import math
'''
Using merge sort
'''

def merge(list1,list2):
    list1=list(list1)
    list2=list(list2)
    M=len(list1)
    N=len(list2)
    i=0
    j=0
    list3=list()
    while i<M and j<N:
        if list1[i]<list2[j]:
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list2[j])
            j+=1
    if i<M:
        list3.extend(list1[i:])
    if j<N:
        list3.extend(list2[j:])
    return list3
#print(merge([0,2,4,5,6],[1,3,4,7]))
def mergeSort(nums):
    nums=list(nums)
    if len(nums)<=1:
        return nums
    half=len(nums)//2
    leftHalf=mergeSort(nums[:half])
    rightHalf=mergeSort(nums[half:])
    
    return merge(leftHalf,rightHalf)

#print(mergeSort([10,9,7,6,5,3,2,0,-1,-10]))
def returnMid(list1):
    mid=int(len(list1)/2)
    if len(list1)%2==0:
        return (list1[mid]+list1[mid-1])/2
    else:
        return float(list1[mid])

def findMedianSortedArrays0(list1, list2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        [1,2,4,5]
        [3,6,8]
        """
        if len(list1)==len(list2)==0:
            return 0.0
        elif len(list1)==0 and len(list2)>0:
            return returnMid(list2)
        elif len(list2)==0 and len(list1)>0:
            return returnMid(list1)
        
        if list2[0]<list1[0]:
            list1,list2=list2,list1
        i=0
        while list1[i]<list2[0] and i<len(list1)-1:
            i+=1
        list1[i:i]=list2
        list1=list1[:i]+mergeSort(list1[i:])
        #print(list1)
        return returnMid(list1)
#print(findMedianSortedArrays([1,2], [3,4])) 


'''
Using quick sort
'''
#Responsible in dividing a list sector into two halfs left is < pivot and right is > pivot
#NOTE: the two halfs are not sorted themselves
def partition(nums,start=0,end=None):
    #assure end to be signed if none
    if end==None:
        nums=list(nums)
        end=len(nums)-1
    #declare pointers i from the begining of the array and j from the end-1 
    i,j=start,end-1
    #move both to the middle based on comparision of both pointed items to the pivot(the end)
    while i<j :
        
        if nums[i]<=nums[end]:
            i+=1
        elif nums[j]>nums[end]:
            j-=1
        else:
            nums[i],nums[j]=nums[j],nums[i]
        
    if nums[i]>nums[end]:
        nums[i],nums[end]=nums[end],nums[i]
        
        return i
    else:
        return end

    
#print(partition([0,1,2,9,8,7,6,5,4]))
def quickSort(nums,start=0,end=None):
    if end==None:
        end=len(nums)-1
    
    if start<end:
        pivot=partition(nums,start,end)
        quickSort(nums,start,pivot-1)
        quickSort(nums,pivot+1,end)
    return nums
#print(quickSort([9,8,7]))
def returnMed(list1):
    mid=int(len(list1)/2)
    if len(list1)%2==0:
        return (list1[mid]+list1[mid-1])/2
    else:
        return float(list1[mid])   
def findMedianSortedArrays(list1, list2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        [1,2,4,5]
        [3,6,8]
        """
        if len(list1)==len(list2)==0:
            return 0.0
        elif len(list1)==0 and len(list2)>0:
            return returnMed(list2)
        elif len(list2)==0 and len(list1)>0:
            return returnMed(list1)
        
        if list2[0]<list1[0]:
            list1,list2=list2,list1
        i=0
        while list1[i]<list2[0] and i<len(list1)-1:
            i+=1
        list1[i:i]=list2
        list1=list1[:i]+quickSort(list1[i:])
        #print(list1)
        return returnMed(list1)
print(findMedianSortedArrays([1,2], [3,4])) 
'''
Test complexity
''' 
def Otime(n):
    times=[]
    Ninputs=range(n)
    inputs1=[]
    inputs2=[]
    start0=time.time()
    while time.time()-start0<10:
        for i in range(n):
            
            for j in range(10*i):
                inputs1.append(random.randint(0,n))
                inputs2.append(random.randint(0,n))
            start=time.time()
            #findMedianSortedArrays(inputs1,inputs2) #function required for test
            end=time.time()
            elapsed=end-start
            times.append(elapsed*10)
            inputs1.clear()
            inputs2.clear()
        print('times',times)
        print('inputs',Ninputs)
    #x = np.linspace(0, 100)
    #plt.hist(inputs)
    plt.plot(Ninputs, times[:n]) # plot the x and y values
    plt.show() # show the plot
#Otime(1000)        