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

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


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
        self.cards = []	# create Hand object

    def __str__(self):
        ans = 'Hand contains'
        for i in range(len(self.cards)):
            ans = ans + ' ' + str(self.cards[i])
        return ans# return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ans = 0
        value = [one.get_rank() for one in self.cards]
        if value.count('A') >= 1:
            ans = sum([VALUES[one] for one in value])
            if ans + 10 <= 21:
                ans += 10
        else:
            ans = sum([VALUES[one] for one in value])
        return ans
    def draw(self, canvas, pos):
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, pos)
            pos[0] += 100# draw a hand on the canvas, use the draw method for cards
       

        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)# create a Deck object

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.cards)	# use random.shuffle() to shuffle the deck
    
    def deal_card(self):
        return self.cards.pop()	# deal a card object from the deck
    
    def __str__(self):
        ans = 'Deck contains '
        for i in range(len(self.cards)):
            ans = ans + ' ' + str(self.cards[i])
        return ans # return a string representing the deck


#define event handlers for buttons
def deal():
    global outcome, in_play, mydeck, playerhand, dealerhand, score

    # your code goes here
    mydeck = Deck()
    mydeck.shuffle()
    outcome = ''
    playerhand = Hand()
    dealerhand = Hand()
    playerhand.add_card(mydeck.deal_card())
    playerhand.add_card(mydeck.deal_card())
    dealerhand.add_card(mydeck.deal_card())
    dealerhand.add_card(mydeck.deal_card())
    if in_play:
        outcome = "You just gave up! New Game."
        score -= 1
#    print 'Player: ', playerhand, ' Dealer: ', dealerhand
    
    in_play = True

def hit():
    global playerhand, in_play, mydeck, outcome, score
    if (in_play):
        playerhand.add_card(mydeck.deal_card())
        if playerhand.get_value() > 21:
            outcome =  "You have busted"
            score -= 1
            in_play = False
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global playerhand, dealerhand, in_play, mydeck, outcome, score
    if (in_play):
        if playerhand.get_value() > 21:
            outcome = "You have busted"
        else:
            while dealerhand.get_value() < 17:
                dealerhand.add_card(mydeck.deal_card())
            print dealerhand
            if dealerhand.get_value() > 21:
                outcome =  "Dealer has busted"
                score += 1
            elif dealerhand.get_value() >= playerhand.get_value():
                outcome = "Dealer wins"
                score -= 1
            else:
                outcome = "You wins"
                score += 1
                
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    in_play = False
    
# draw handler    
def draw(canvas):
    global outcome
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Dealer", (100, 180), 20, "Black")
    canvas.draw_text("Player", (100, 380), 20, "Black")
       
    if (in_play) :
        promt = 'Hit or stand?'
    else:
        promt = 'New game?'
    canvas.draw_text(promt,  (200, 150), 30, "Black") 
    canvas.draw_text("Blackjack!",  (20, 50), 50, "Black") 
    canvas.draw_text("Score: " + str(score),  (400, 50), 30, "Black") 
    playerhand.draw(canvas, [100, 400])
    dealerhand.draw(canvas, [100, 200])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_SIZE[0]/2, 200 + CARD_SIZE[1]/2], CARD_SIZE)
    canvas.draw_text(outcome,  (50, 550), 30, "Black") 
# initialization frame

playerhand = Hand()
dealerhand = Hand()

frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric
