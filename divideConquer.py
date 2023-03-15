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
def extractMax(nums):
    pass
def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(nums)
        i=1
        j=0
        k=0
        summ=nums[0]
        sums=[(nums[0],0,0)]
        delta=0
        if len(nums)<=1:
            return nums
        
        while i< len(nums)and j< len(nums) and k< len(nums):
            # delta=sums[-1]-sums[-2]
            print('hiiiiiiiii')
            print(nums[i])
            if summ <= 0 :
                #print(nums[i],nums[i+1])
                if nums[i]>nums[i-1]:
                    j=i
                    k=i
                    summ=nums[i]
                    sums.append((nums[i],j,k))
                    
   
            else:
                sums.append((summ,j,k))
                summ+=nums[i]
                k=i
       
            i+=1
            
        maxx=max(sums,key=operator.itemgetter(0))
        
        print(sums)
        print(maxx)
        
        return maxx[0]   
print(maxSubArray([-1,17,0,-17,2,3,4,5,2,3,-9,122,-3]))