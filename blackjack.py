#BlackJack 

#LOGIC -    
# One deck of cards
# Dealer is dealing 2 cards to player and 2 cards to themselves
# If Dealer hits 21 on first go then Player loses
# If Dealer hits 21 and player hits 21 on first go then no one wins
# If player has less than 21 they can choose to hit for more cards or keep their hand
# If Player hand is more than 21 then the Player loses
# If Dealer hand hits higher then 21 then the Player wins
# If the Dealers hand is closer to 21 than the player then the player loses

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card():
    """
    Card class, Suite, Rank, Value
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    """
    Deck Class
    """
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():
    """
    docstring
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # list of single card object
            self.all_cards.append(new_cards)


    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

#GAME SETUP
player = Player("One")
dealer = Player("Dealer")

new_deck = Deck()
new_deck.shuffle()

for x in range(2):
    player.add_cards(new_deck.deal_one())
    dealer.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")
    print(player.all_cards[0].value, player.all_cards[1].value) 

    if dealer.all_cards[0].value + dealer.all_cards[1].value == 21 and player.all_cards[0].value + player.all_cards[1].value == 21:
        print("Duel Blackjack. Tie Game!")
        print(player.all_cards[0].value, player.all_cards[1].value)
        print(dealer.all_cards[0].value, dealer.all_cards[1].value)
        game_on = False
        break

    if player.all_cards[0].value + player.all_cards[1].value == 21:
        print("Player hit 21. Blackjack!")
        print(player.all_cards[0].value, player.all_cards[1].value)   
        game_on = False
        break

    if dealer.all_cards[0].value + dealer.all_cards[1].value == 21:
        print("Dealer hits Blackjack! Player loses")
        print(dealer.all_cards[0].value, dealer.all_cards[1].value)
        game_on = False
        break
    
    if player.all_cards[0].value + player.all_cards[1].value < 21:
        result = input("Would you like to hit?")
        if result == "YES":
            player.add_cards(new_deck.deal_one())
            print(player.all_cards[0].value, player.all_cards[1].value, player.all_cards[-1].value) 
            if player.all_cards[0].value + player.all_cards[1].value + player.all_cards[-1].value == 21:
                print("Player hit 21. Player wins.")
                game_on = False
                break
            if player.all_cards[0].value + player.all_cards[1].value + player.all_cards[-1].value > 21:
                print("Player busts. Dealer wins.")
                game_on = False
                break
            if player.all_cards[0].value + player.all_cards[1].value + player.all_cards[-1].value < 21:
                result_two = input("Would you like to hit?")
                if result_two == "YES":
                    player.add_cards(new_deck.deal_one())
                    print(player.all_cards[0].value, player.all_cards[1].value, player.all_cards[2].value, player.all_cards[-1].value)
                    if player.all_cards[0].value + player.all_cards[1].value + player.all_cards[2].value + player.all_cards[-1].value == 21:
                        print("Player hit 21. Player wins.")
                        game_on = False
                        break
                    if player.all_cards[0].value + player.all_cards[1].value + player.all_cards[2].value + player.all_cards[-1].value > 21:
                        print("Player busts. Dealer wins.")
                        game_on = False
                        break
                else:
                    print("Tallying score")
                    if (player.all_cards[0].value + player.all_cards[1].value + player.all_cards[-1].value- 21) < (dealer.all_cards[0].value + dealer.all_cards[1].value - 21):
                        print("Dealer is closer to 21, Dealer wins.")
                        print(dealer.all_cards[0].value, dealer.all_cards[1].value)
                        game_on = False
                        break
            if player.all_cards[0].value + player.all_cards[1].value + player.all_cards[-1].value > 21:
                print("Player busts. Dealer wins.")
                game_on = False
                break 
        else:
            print("Tallying score")
            if (player.all_cards[0].value + player.all_cards[1].value - 21) < (dealer.all_cards[0].value + dealer.all_cards[1].value - 21):
                print("Dealer is closer to 21, Dealer wins.")
                print(dealer.all_cards[0].value, dealer.all_cards[1].value)
                game_on = False
                break
            else:
                print("Player is closer to 21, Player wins!")
                print(player.all_cards[0].value, player.all_cards[1].value)
                print(dealer.all_cards[0].value, dealer.all_cards[1].value)
                break
