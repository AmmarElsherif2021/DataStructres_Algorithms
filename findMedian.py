
'''
find median of two sorted lists
'''
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import math

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
print(merge([0,2,4,5,6],[1,3,4,7]))
def mergeSort():
    pass
def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
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
            merge(inputs1,inputs2) #function required for test
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
Otime(100)        