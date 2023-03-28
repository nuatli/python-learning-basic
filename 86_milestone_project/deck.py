import random
from card import Card

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
suits = ('Hearts','Diamonds','Spades','Clubs')

class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks :
                #Create the Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()
        
                
'''
new_deck = Deck()
new_deck.shuffle()
#print(new_deck.all_cards)
first_card = new_deck.all_cards[-1]                
for card_object in new_deck.all_cards:
    print(card_object)
'''