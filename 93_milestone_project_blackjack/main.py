from Deck import *
from Hand import *
from Chips import *
import random
import os


playing = True

balance = 100

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        print('\n****************************************************')
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break
os.system("cls")
while True:
    # Print an opening statement
    print('Welcome to BlackJack! \nGet as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.')
    print('Your balance is ',balance )
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips(balance)  
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
        if player_hand.value <= 21:
            
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)    
        
            # Show all cards
            show_all(player_hand,dealer_hand)
            
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
                break
             
            elif dealer_hand.value > player_hand.value:
                if(player_hand.value > 21 ):
                    dealer_wins(player_hand,dealer_hand,player_chips)
                    break
            
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
                break
            
            elif dealer_hand.value ==  21:
                if player_hand.value == 21:
                    push(player_hand,dealer_hand)
                elif player_hand.value < 21:
                    dealer_wins(player_hand,dealer_hand,player_chips)
                break    
            else:
                push(player_hand,dealer_hand)
                break
            
        balance = player_chips.total
    # Inform Player of their chips total 

    print("\nPlayer's winnings stand at",player_chips.total)
    balance = player_chips.total
    if balance == 0:
        print("Thanks for playing! Your money is not enough for continue")
        break
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        os.system("cls")
        continue
    else:
        print("Thanks for playing!")
        break

'''


'''