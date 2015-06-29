# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
busted = False
tie = False
penalty = False
deck = []
player_hand = []
dealer_hand = []
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


#################################################
# Student should insert the implementation of the Card class here

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []


    def __str__(self):
        hand_string = ''
        for i in range(len(self.hand)):
            card = self.hand[i]
            hand_string = hand_string + ' ' + card.get_suit() + card.get_rank()
        return str(hand_string)	# return a string representation of a hand
            

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        global VALUES
        total = 0
        has_ace = False
        for i in range(len(self.hand)):
            card = self.hand[i]
            rank = card.get_rank()
            if rank == 'A':
                has_ace = True               
            value = VALUES[rank]
            total = total + value
        if (has_ace is True and (total + 10) < 22):
            total = total + 10
        return total
            
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.hand)):
            card = self.hand[i]
            card.draw(canvas, [(pos[0] * i), pos[1]])

# define deck class 
class Deck:
    def __init__(self):
        global SUITS, RANKS
        self.deck = []		# create a Deck object 
        for i in range(4):
            for j in range(13):
                self.deck.append(Card(SUITS[i], RANKS[j]))

        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck) 
        return(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        card = self.deck.pop(0)
        return(card)
    
    def __str__(self):
        deck_string = ''
        for i in range(len(self.deck)):
            deck_string = deck_string + ' ' + str(self.deck[i])
        return str(deck_string)	# return a string representing the deck    
        


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, busted, score, tie, penalty
    deck = Deck()
    deck.shuffle()
    outcome = ""
    busted = False
    tie = False
#    print "\nOriginal deck contains: ", deck
    if in_play == True:
        score -= 1
        penalty = True
        print 'Penalty for New Deal Mid Round'
    else:
        in_play = True
    player_hand = Hand()
    dealer_hand = Hand()
    card = deck.deal_card()
    player_hand.add_card(card)
    card = deck.deal_card()
    dealer_hand.add_card(card)
    card = deck.deal_card()
    player_hand.add_card(card)
    card = deck.deal_card()
    dealer_hand.add_card(card)
    print "\nPlayer Hand is: ", player_hand, " Value is: ", player_hand.get_value()
#    print "Dealer Hand is: ", dealer_hand, " Value is: ", dealer_hand.get_value()
    print "Dealer is showing:", card 

def hit():
    global outcome, score, busted, in_play, penalty
    if in_play is False:			# Disable the Hit button when NOT in play.
        return
    penalty = False    
    if player_hand.get_value() <= 21:
        card = deck.deal_card()
        player_hand.add_card(card)
        print "Player Hand is: ", player_hand, " Value is: ", player_hand.get_value()
        if player_hand.get_value() > 21:
            print '\nYou have busted'
            busted = True
            print "\nDealer Hand is: ", dealer_hand, " Value is: ", dealer_hand.get_value()
            print 'The Dealer Wins!'
            outcome = 'd'
            score -= 1
            in_play = False
    
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global outcome, score, busted, in_play, tie, penalty
    j = 0
    penalty = False    
    if in_play is False:          # Disable the Stand button when NOT in play.
        return
    while dealer_hand.get_value() < 17:
        card = deck.deal_card()        
        dealer_hand.add_card(card)        
        print "\nDealer Hand is: ", dealer_hand, " Value is: ", dealer_hand.get_value()
        print "Player Hand is: ", player_hand, " Value is: ", player_hand.get_value()
        for i in range(175000):
            j += 1             # Do something to kill some time
                               # to give the impression of dealing cards.
    
    # assign a message to outcome, update in_play and score        
    print "\nDealer Hand is: ", dealer_hand, " Value is: ", dealer_hand.get_value()
    if (dealer_hand.get_value() > 21):
        print 'Dealer has busted.'
        busted = True
        in_play = False
    if (dealer_hand.get_value() >= player_hand.get_value() 
        and dealer_hand.get_value() <= 21):
        print '\nThe Dealer Wins!'
        outcome = 'd'
        score -= 1
        in_play = False
        if (dealer_hand.get_value() == player_hand.get_value()):
            tie = True
            print 'Tie score goes to the dealer.'
    else:
        print '\nThe Player Wins!'
        outcome = 'p'
        score += 1
        in_play = False

        
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, busted, in_play, penalty
    canvas.draw_text('Blackjack', [56, 75], 64, 'Aqua')
    canvas.draw_text('Score ' + str(score), [360, 75], 38, 'Black')
    canvas.draw_text('Dealer ', [36, 180], 36, 'Black')
    if in_play is True:
        canvas.draw_text('Player - Hit or Stand?  Value is: ' + str(player_hand.get_value()), [36, 380], 36, 'Black')
        if penalty is True:
            canvas.draw_text('Player - Hit or Stand?  Value is: ' + str(player_hand.get_value()), [36, 380], 36, 'Black')
            canvas.draw_text('Penalty for New Deal Mid Round', [36, 550], 36, 'Black')
    player_hand.draw(canvas, [80, 410])
    # card back to be added
    dealer_hand.draw(canvas, [80, 210])
    if in_play is True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [36.5, 260], CARD_SIZE)
    if outcome == 'd' and busted is False and in_play is False:
        if tie is True:
            canvas.draw_text('The Dealer Wins on a Tie!', [36, 550], 36, 'Black')
        else:
            canvas.draw_text('The Dealer Wins!', [36, 550], 36, 'Black')
        canvas.draw_text('Player - Hand was ' + str(player_hand.get_value()) + ' - New Deal?', [36, 380], 36, 'Black')
        canvas.draw_text('Dealer - Hand was ' + str(dealer_hand.get_value()), [36, 180], 36, 'Black')
    elif outcome == 'd' and busted is True and in_play is False:
        canvas.draw_text('You have busted - The Dealer Wins!', [12, 550], 36, 'Black')
        canvas.draw_text('Player - Hand was ' + str(player_hand.get_value()) + ' - New Deal?', [36, 380], 36, 'Black')
        canvas.draw_text('Dealer - Hand was ' + str(dealer_hand.get_value()), [36, 180], 36, 'Black')
    elif  outcome == 'p' and busted is False and in_play is False:
        canvas.draw_text('The Player Wins!', [36, 550], 36, 'Black')
        canvas.draw_text('Player - Hand was ' + str(player_hand.get_value()) + ' - New Deal?', [36, 380], 36, 'Black')
        canvas.draw_text('Dealer - Hand was ' + str(dealer_hand.get_value()), [36, 180], 36, 'Black')
    elif  outcome == 'p' and busted is True and in_play is False:
        canvas.draw_text('Dealer has busted - The Player Wins!', [2, 550], 36, 'Black')
        canvas.draw_text('Player - Hand was ' + str(player_hand.get_value()) + ' - New Deal?', [36, 380], 36, 'Black')
        canvas.draw_text('Dealer - Hand was ' + str(dealer_hand.get_value()), [36, 180], 36, 'Black')
    else:
        canvas.draw_text('                        ', [12, 550], 36, 'Green')








# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric