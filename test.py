'''
This is a test file for algorithms i made for this repo
'''
import random
import numpy as np
import matplotlib as plt
import time

'''Test cases
'''
test0={
       'input':{[1,4,2,3,6,7,4,3,2]},
       'output':[1, 2, 2, 3, 3, 4, 4, 6, 7]
       }
test1={
       'input':[5],
       'output':[5]
       }
test2={
       'input':[3,4,5,6,2,33,4,5,99,67,4,53,45,23,2,33,44],
       'output':[2, 2, 3, 4, 4, 4, 5, 5, 6, 23, 33, 33, 44, 45, 53, 67, 99]
       }
test3={
       'input':[],
       'output':[]
       }
test4={
       'input':[1,2,3,4,5,6,7,8],
       'output':[1,2,3,4,5,6,7,8]
       }
test5={
       'input':[8,7,6,5,4,3,2,1],
       'output':[1,2,3,4,5,6,7,8]
       }
test6={
       'input':[11,32,53,994,45,66,67,18],
       'output':[11, 18, 32, 45, 53, 66, 67, 994]
       }
test7={
       'input':[11,11,11,11,11],
       'output':[11,11,11,11,11]
       }

'''
Test complixty
'''
def Otime(n):
    times=[]
    Ninputs=range(n)
    inputs=[]
    start0=time.time()
    while time.time()-start0<10:
        for i in range(n):
            
            for j in range(10*i):
                inputs.append(random.randint(0,n))
            start=time.time()
            #insertion_sort(inputs) #function required for test
            end=time.time()
            elapsed=end-start
            times.append(elapsed*10)
            inputs.clear()
        print('times',times)
        print('inputs',Ninputs)
    #x = np.linspace(0, 100)
    #plt.hist(inputs)
    plt.plot(Ninputs, times[:n]) # plot the x and y values
    plt.show() # show the plot

