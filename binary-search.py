# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:00:20 2023

@author: ammar
"""
import math
import random
'''(1)  Alice has some cards with numbers written on them.
 She arranges the cards in decreasing order,
 and lays them out face down in a sequence on a table.
 She challenges Bob to pick out the card containing a given number
 by turning over as few cards as possible. 
 Write a function to help Bob locate the card.
'''
def pickCard(cards,reqNum):
    if cards:
        cards.sort(reverse=True)
        #using binary search tree
        #make a tree level counter
        level=1
        #make a pointer to the middle index of given scope in the list
        pointer=int(len(cards)/2)
        print('visited -->',cards[pointer])
        print('pointer -->  ',pointer)
        while cards[pointer] != reqNum and level< math.log(len(cards),2) :
            level+=1
            #pointed card is greater/less than reqNum move pointer
            if reqNum<cards[pointer]:
                pointer=(pointer+math.ceil(len(cards)/(2**level)))%len(cards)
                
                
            else:
                pointer=(pointer-math.ceil(len(cards)/(2**level)))%len(cards)
              
                
            print('visited -->',cards[pointer])
            print('pointer -->  ',pointer)
        return (int(cards[pointer]==reqNum),cards[pointer])
    else:
        return (0,0) #if empty
    
  
if __name__=='__main__':
    '''
    to apply this test you must ensure the existance of the target in the list 
    while the cards list item nums are randomly generated!
    you can check the last three visited leaf indices 
    
    '''
    cardsList=list()
    for i in range(10000):
        cardsList.append(random.randint(0,170000))
    cardsList.sort(reverse=True)
    print(pickCard(cardsList, 1121))
    
