#!/usr/bin/env python
# coding: utf-8
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}



class Card():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit




class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for every_suit in suits:
            for every_rank in ranks:
                created_card = Card(every_suit, every_rank)
                
                self.all_cards.append(created_card)
                
    def shuffle_deck(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()





class Player():
    
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def remove_one(self):
        return self.hand.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)
    
    def __str__(self):
        return f'{self.name} has {len(self.hand)} cards.'






player_one = Player("One")
player_two = Player ("Two")

new_deck = Deck()
new_deck.shuffle_deck()

for x in range (26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())



game_on = True




round_num = 0

while game_on:
    
    round_num += 1
    print(f'Round {round_num}')
    
    if len(player_one.hand) == 0:
        print('Player One has lost. Player Two has won the war!')
        game_on = False
        break
        
    if len(player_two.hand) == 0:
        print('Player Two has lost. Player One has won the war!')
        game_on = False
        break
        
    #Start of new round. These are cards in play.
    p1_cards = []
    p1_cards.append(player_one.remove_one())
    
    p2_cards = []
    p2_cards.append(player_two.remove_one())
    
    print (f'P1:{p1_cards[-1]} vs P2:{p2_cards[-1]}')
    
    comparison_on = True
    while comparison_on:
        if p1_cards[-1].value < p2_cards[-1].value:
            
            player_two.add_cards(p1_cards)
            player_two.add_cards(p2_cards)
            
            print(f'Player Two wins the round and takes {len(p1_cards)+len(p2_cards)} cards.')
            
            comparison_on = False
        
        elif p2_cards[-1].value < p1_cards[-1].value:
            
            player_one.add_cards(p1_cards)
            player_one.add_cards(p2_cards)
            
            print(f'Player One wins the round and takes {len(p1_cards)+len(p2_cards)} cards.')
            
            comparison_on = False
            
        else:
            print('War!')
            if len(player_one.hand)<10:
                #print('Player One has insufficent cards to go to war.\nPlayer Two wins')
                for i in range (len(player_one.hand)-1):
                    p1_cards.append(player_one.remove_one())
                #game_on = False
                #break
                
            elif len(player_two.hand)<10:
                for i in range (len(player_two.hand)-1):
                    p2_cards.append(player_two.remove_one())
                #print('Player One has insufficent cards to go to war.\nPlayer Two wins')
                #game_on = False
                #break
            else:
                for num in range (10):
                    p1_cards.append(player_one.remove_one())
                    p2_cards.append(player_two.remove_one())
