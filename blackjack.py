#Write a program to play a game blackjack (text only – no graphics). Assume that the computer is the dealer and the player is the user.
#Some Assumptions:
#Suits (Clubs, Diamonds, Hearts, Spades) will be ignored
#Assume that there are only 13 different cards: ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
import random

#set up deck of cards variable that will be referenced throughout
fulldeck= ['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A']

#function for drawing the first two cards (original hand)
def starting_hand():
    hand=[]
    for i in range(2):
        card=fulldeck.pop(random.randint(0,len(fulldeck)))
        hand.append(card)
    return(hand)

#function for drawing cards one at a time
def drawcard():
        card=fulldeck.pop(random.randint(0,len(fulldeck)))
        return(card)

#function that adds the cards accordingly from a given hand
def add_values(hand):
    value=0
    for i in hand:
        if type(i)==int:
            value+=i
        elif i=='J' or i=='Q' or i=='K':
            value+=10
        elif i=='A':
            if ((value+11) > 21)==True:
                value+=1
            elif ((value+11)> 21)==False:
                value+=11
    return(value)

#function that scores for blackjack specifically
def blackjack(firsthand,secondhand):
    if firsthand==['A',10] or firsthand==[10,'A']:
        print('You got blackjack, you win!')
        exit()
    elif secondhand==['A',10] or secondhand==[10,'A']:
        print('Aw, the dealer got blackjack. Sorry, you lose!')
        exit()
    pvalue=add_values(firsthand)
    dvalue=add_values(secondhand)
    if pvalue==21:
        print('Congrats, you got blackjack, you win!')
    elif dvalue==21:
        print('The dealer got blackjack, sorry you lose!')
    else:
        pass

#function that scores overall      
def scoring(player,dealer):
    if player==21:
        print('Congrats, you got blackjack, you win!')
    elif dealer==21:
        print('The dealer got blackjack, sorry you lose!')
    elif player>22:
        print('Sorry,you lose!')
    elif dealer>22:
        print('The dealer lost, you win!')
    elif player==dealer:
        print('Tie values, you lose!')
    elif player>dealer:
        print('You scored higher. You win!')
    elif player<dealer:
        print('The dealer scored higher. You lose!')

#program that combines other functions to allowe user to play blackjack!
def play_blackjack():
    print("Hi, let's play a game of blackjack! You draw first")
    playerhand=starting_hand()
    pvalue=add_values(playerhand)
    print('Your hand is'+str(playerhand)+'\nNow the dealer will draw')
    dealhand=starting_hand()
    dvalue=add_values(dealhand)
    blackjack(playerhand,dealhand)
    print('You are currently valued at '+str(pvalue))
    choice=input('Would you like to [d]raw another card or [p]ass?')
    if choice=='d':
        playerhand.append(drawcard())
        while dvalue<=16:
            dealhand.append(drawcard())
            dvalue=add_values(dealhand)
        print(playerhand, dealhand)
        pvalue=add_values(playerhand)
        print("Your score is " + str(pvalue) +" and the dealer's is "+str(dvalue))
        scoring(pvalue,dvalue)
    elif choice=='p':
        while dvalue<=16:
            dealhand.append(drawcard())
            dvalue=add_values(dealhand)
        print(playerhand, dealhand)
        pvalue=add_values(playerhand)
        print("Your score is " + str(pvalue) +" and the dealer's is "+str(dvalue))
        scoring(pvalue,dvalue)

play_blackjack()
