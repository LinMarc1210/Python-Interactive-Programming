# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# helper of card print
def card_print(string_list):
    ans = ""
    for l in string_list:
        ans += (str(l[0]) + str(l[1]) + " ")
    return ans

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
        card_loc = [CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit)]
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def draw_back(self, canvas, pos):
        card_loc = [CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]]
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# define hand class 
class Hand:
    def __init__(self):
        self.hand = []
        
    def add_card(self, card):
        self.hand.append(card)
        
    def get_hand(self):
        return self.hand
        
    def get_value(self):
        sum = 0
        for l in self.hand:
            sum += VALUES[str(l.get_rank())]
        return sum
    
    def __str__(self):
        ans = ""
        for l in self.hand:
            ans += str(l) + " "
        return "Hand contains " + ans
    
    def draw(self, canvas, pos):
        for l in self.hand:
            l.draw(canvas, pos)
            pos[0] += CARD_SIZE[0] + 20

 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i,j))
               
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_card(self):
        return self.deck.pop()
        
    def __str__(self):
        ans = ""
        for l in self.deck:
            ans += str(l) + " "
        return "Deck contains " + ans


#define event handlers for buttons
def deal():
    global message, outcome, in_play, deck, player, dealer, score

    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    message = ""
    outcome = "Hit or Stand ?"
    
    in_play = True

def hit():
    global message, in_play, deck, player, dealer, score, outcome
    # if the hand is in play, hit the player
    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
            # if busted, assign a message to outcome, update in_play and score
            if player.get_value() > 21:
                score -= 1
                in_play = False
                message = "You busted. You lose..."
                outcome = "New deal?"
            
def stand():
    global message, in_play, deck, player, dealer, score, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            score += 1
            message = "Dealer busted. You win!"
            outcome = "New deal?"
        elif dealer.get_value() == player.get_value():
            score -= 1
            message = "Tie. Dealer wins!"
            outcome = "New deal?"
        elif dealer.get_value() > player.get_value():
            score -= 1
            message = "Dealer's bigger. Dealer wins!"
            outcome = "New deal?"
        else:
            score += 1
            message = "You are bigger, You win!"
            outcome = "New deal?"
            
    # assign a message to outcome, update in_play and score
    in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BLACKJACK", [130, 60], 60, "Black")
    canvas.draw_text("Player", [20, 370], 30, "Black")
    canvas.draw_text("Dealer", [20, 170], 30, "Black")
    canvas.draw_text(outcome, [200, 370], 30, "White")
    canvas.draw_text(message, [200, 170], 30, "White")
    canvas.draw_text("Score: " + str(score), [400, 570], 40, "Maroon")
    
    player.draw(canvas, [20, 400])
    dealer.draw(canvas, [20, 200])
    if in_play:
        dealer.get_hand()[0].draw_back(canvas, [20, 200])


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