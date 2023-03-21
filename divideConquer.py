'''
Divide and conquer is a problem-solving strategy 
that involves breaking down a larger problem into 
smaller and simpler subproblems, 
solving them independently, 
and combining their solutions to 
get the final answer123. It is often used to find an 
optimal solution of a problem1. 
Some examples of algorithms that use 
divide and conquer are merge sort, quick sort, binary search, etc.

author: ammar

these functions are problems I practiced on leetcode
'''
import operator
import time
import random 
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as si
import math

def maxCrossSum(nums):
    mid=len(nums)//2
    rightSum=-10000000
    leftSum=-100000000
    tempSum=0
    for i in range(mid,-1,-1):
        tempSum+=nums[i]
        if leftSum<tempSum:
            leftSum=tempSum
    tempSum=0
    for i in range(mid+1,len(nums)):
        tempSum+=nums[i]
        if rightSum<tempSum:
            rightSum=tempSum
    return max(leftSum,rightSum,leftSum+rightSum)
def maxSubArray(nums):
    if len(nums)==1:
        return nums[0]
    mid=len(nums)//2
    left=nums[:mid]
    right=nums[mid:]
    leftSum=maxSubArray(left)
    rightSum=maxSubArray(right)
    middleSum=maxCrossSum(nums)
    return max(leftSum,rightSum,middleSum)
print(maxSubArray([0,-20,-66,-44,-90,-11,-222,1000,3333,-1]))    
    
def maxxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(nums)
        '''
        assume the following
        i is the main iterator
        j indicates for the beginning of considered sub array
        k idicates for the end of considered sub array
        '''
        i=1
        j=0
        k=0
        
        
        if len(nums)<=1:
            return nums
        summ=nums[0]
        sums=[(nums[0],0,0)]
        while i< len(nums)and j< len(nums) and k< len(nums):
            #if the sum is negative
            if summ <= 0 :
                '''
                if num is bigger than previous num 
                in the negative sum spectrum re-adjust j and k
                and consider point itself a record else just i++
                '''
                if nums[i]>nums[i-1]:
                    j=i
                    k=i
                    summ=nums[i]
                    sums.append((nums[i],j,k))
                     
                '''
                if sum is +ve save the last record and
                update k pointer with i
                '''
            else:
                sums.append((summ,j,k))
                summ+=nums[i]
                k=i
       
            i+=1
            
        maxx=max(sums,key=operator.itemgetter(0))
        
        #print(sums)
        print(maxx)
        
        return maxx[0]   
print(maxxSubArray([0,-20,-66,-44,-90,-11,-222,1000,3333,-1]))
