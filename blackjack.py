import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
numbers = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = ({'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11})

# First let's create the classes we'll be using

class Card:
    
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number
        self.value = values[number]
        
    def __str__(self):
        return self.number+" of "+self.suit
    
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for number in numbers:
                self.deck.append(Card(suit,number))
                
    def __str__(self):
        cards_in_deck = ''
        for card in self.deck:
            cards_in_deck += '\n'+card.__str__()
        return "This deck has: " + cards_in_deck 
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        one_card = self.deck.pop()
        return one_card

class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def deal_card(self,card):
        self.cards.append(card)
        self.value += values[card.number]
        if card.number == 'Ace':
            self.aces += 1

    def change_value(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
class Chips:
    
    def __init__(self, total):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet

# Next, let's define some functions

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('Please enter your bet: '))
        except:
            print('Please enter a number greater than 0: ')
        else:
            if chips.bet>chips.total:
                print(f'That is too much. You have {chips.total} chips')
            else:
                break
            
def hit(deck,hand):

    hand.deal_card(deck.deal())
    hand.change_value()
                      
def hit_or_stand(deck,hand):
    
    playing = True
    
    while True:
                      
        x = input('Hit or stand? Please enter either H or S: ')
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print('Player stands - dealer turn')
            playing = False
        else:
            print('Please enter either H or S: ')
            continue
        break        
                      
def show_some_cards(player,dealer):
        
    print('\n Dealer hand: ')
    print('First one hidden!')
    print(dealer.cards[1])
    
    print('\n Player hand: ',*player.cards,sep='\n')

def show_all_cards(player,dealer):
                      
    print('\n Dealer hand: ',*dealer.cards,sep='\n')
  
    print('\n Player hand: ',*player.cards,sep='\n')
                      
def player_busts(player,dealer,chips):
    
    print('Player busts! Dealer wins')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    
    print('Player wins!')
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    
    print('Dealer busts! Player wins')
    chips.win_bet()

def dealer_wins(player,dealer,chips):

    print('Dealer wins!')
    chips.lose_bet()
    
def push(player,dealer):
    
    print('PUSH!')

# Finally, let's run the game!

while True:
    
    print('Welcome to Blackjack!')
    
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.deal_card(deck.deal())
    player.deal_card(deck.deal())

    dealer = Hand()
    dealer.deal_card(deck.deal())
    dealer.deal_card(deck.deal())
    
    chips = Chips(total=100)
    take_bet(chips)
    
    show_some_cards(player,dealer)
    
    playing = True
    while playing:
        
        hit_or_stand(deck,player)
        show_some_cards(player,dealer)
    
        if player.value > 21: 
            player_busts(player,dealer,chips)
            break
        if player.value <= 21:
            while dealer.value < 21:
                hit(deck,dealer)
                show_all_cards(player,dealer)
                
                if player.value>dealer.value:
                    player_wins(player,dealer,chips)
                    playing = False
                elif player.value<dealer.value:
                    dealer_wins(player,dealer,chips)
                    playing = False
                elif dealer.value>21:
                    dealer_busts(player,dealer,chips)
                    playing = False
                else:
                    push(player,dealer)
                    
    print(f'\n Total chips: {chips.total}')
    new_hand = input('Play another hand? Enter Y or N: ')
    
    if new_hand[0].lower()=='y':
        playing = True
    elif new_hand[0].lower()=='n':
        print('Thanks for playing!')
        break
    else:
        print('Please enter either Y or N: ')
        continue
    break

