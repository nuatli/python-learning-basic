'''
#CARD
#SUIT,RANK,VALUE
'''
from values import *


class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of "+self.suit
    
    
    

'''
two_hearts = Card("Hearts","Two")
print(two_hearts.suit)
print(two_hearts)
print(two_hearts.rank)
print(values[two_hearts.rank])
''' 