##importing random to shuffle the cards
import random
##initializing constant values
##creating list, these cards list does not consider 4 suits, in further programming this point will be considered 
CARDS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
##Black jack values of each card
BJ_VALUES = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,  '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}


class Card:

    def __init__(self, bjvalue):
        ##checking if the card exists in the list
        if(bjvalue in BJ_VALUES):
            self.bjvalue = bjvalue
        else:
            self.bjvalue = None
            print("Wrong card: ", bjvalue)

    ##returning the black jack value of the card
    def get_bjvalue(self):
        return self.bjvalue

    ##returning printable version of the cards value (str version)
    def __str__(self):
        return str(self.bjvalue)

                
class Deck:

    '''Shuffling the cards, dealing a card to the players hand and showing string of the deck'''

    def __init__(self):
        
        self.deck = []
        '''adding all cards 4 times because i use only the actual values of the cards and dont consider the 4 suits in the initial list'''

        for i in range(4):
            for bjvalue in BJ_VALUES:
                self.deck.append(Card(bjvalue))

    def deal(self):
        '''dealing out a card and take it out from the deck '''
        return self.deck.pop()

    def shuffle(self):
        '''shuffling the cards in the deck'''
        random.shuffle(self.deck)

    def __str__(self):
        cards = ''
        for card in self.deck:
            cards += str(card) + " "
        return cards.strip()



class PlayerHand:
    '''adding cards to the players hand, showing the cards, showing full hand if the player wants '''

    def __init__(self):
        ##this is the list of cards a player has
        self.playerHand = []

    def add_card(self, card):
        ##adds a card to the players hand
        self.playerHand.append(card)

    def get_value(self):
        value = 0
        ace = 0

        for card in self.playerHand:
            ''' adding the black jack value of the card to the players full hand'''
            value += BJ_VALUES[card.get_bjvalue()]
            ##checking if the card is Ace
            if str(card.get_bjvalue()) == 'Ace':
                ace += 1


            for i in range(ace):
                ##according to the rules, if the total hand value is less than 11, Ace will be 10 
                if value <= 11:
                    value += 10

        return value

    def print_cards(self):
        ''' Printing cards to be visible to all players, excepting the first card'''
        for i in range(1, (len(self.playerHand))):
            print(self.playerHand[i], end=' ')
        print()

    def seePlayerHand(self):
        '''asking the player if he wants to see his full hand '''
        global turn
        see = input(turn + ", would you like to see your full hand? Say 'yes' to check your cards, or say 'no' to continue")

        ##player input error handling 
        while see.lower() != 'yes' and see.lower() != 'no':
            see = input(turn + ", please, type 'yes' or 'no' !")

        if see.lower() == 'yes':
            ##showing the full hand if 'yes'
            print(turn + "'s full hand value: ", self.get_value(), sep="")
            print()
            
            
            
            
            
        


   
    def check_values_over(self):
        ##Checking if the value in players hand is over 21
        global turn, playerOver, player1, player2

        ##if hand over 21
        if self.get_value() > 21:
            playerOver = True
            if turn == 'Player 1':
                print("Player 1's hand equals ", self.get_value())
                print("Player 2's hand equals ", player2.get_value())
                print(turn + " , your hand is over 21, you lost. Player 2 wins !!!")

            if turn == 'Player 2':
                print("Player 1's hand equals ", player1.get_value())
                print("Player 2's hand equals ", self.get_value())
                print(turn + " , your hand is over 21, you lost. Player 1 wins !!!")


    
   
    def __str__(self):
        ## returning string value of the players hand
        cards = ''
        for card in self.playerHand:
            cards += str(card) + " "
            return cards.strip()
                
                

    


class GameLogic:

    

    def playerTurn(self, player, playerHandValue):
        ##hit or no options 
        global player1No, player2No

        print('Turn: ' + player)

        playerHandValue.seePlayerHand()

        
        ##asking the player if he wants to hit or stay 
        hitOrNo = input(player + ": Would you like to hit or no? Please, say 'hit' if you want to get a new card, else say 'no' to continue")


        ##player input error handling 
        while hitOrNo.lower() != 'hit' and hitOrNo.lower() != 'no':
            hitOrNo = input(player + ": Please type 'hit' or 'no' to continue the game\n")
             


        if hitOrNo.lower() == 'hit':
            ##hit chosen, adding a card from the deck 
            playerHandValue.add_card(deck.deal())
            print("\n One card added to ", player, sep="")

            print(player + "'s cards: ", end=' ', sep="")
            ##showing the cards 
            playerHandValue.print_cards()
            playerHandValue.seePlayerHand()



        elif hitOrNo.lower() == 'no':
            ##if the player does not want to hit, continue 
            
            if player == 'Player 1':
                    player1No = True
            if player == 'Player 2':
                    player2No = True

        return





    def checkOutcome(self, player1, player2):
        ##showing each players' hand value
        print("Player 1's hand value equals to ", player1.get_value())
        print()
        print("Player 2's hand value equals to: ", player2.get_value())


        if player1.get_value() == player2.get_value():
            ##same value
            print("Both players have the same hand value There is a tie", sep='')
        elif player1.get_value() == 21:
            ##Black Jack for player 1
            print("Player 1's hand value is 21!! Thats BlackJack! Player 1 wins!")
        elif player2.get_value() == 21:
            ##Black Jack for player 1
            print("Player 2's hand value is 21!! Thats BlackJack! Player 2 wins!")

        else:
            ##checking whoose hand value is higher 
            print("\n***Player 1 Wins!***" if player1.get_value() > player2.get_value() else "\n***Player 2 Wins!***")


class AdvancedGameLogic(GameLogic):
    ##for future new expanded logic implementation, inhereting from the class GameLogic

    pass
    

        
##variables

deck = Deck()
player1No = False
player2No = False
playerOver = False
turn = 'Player 1'
player1 = PlayerHand()
player2 = PlayerHand()
logic = GameLogic()


def main():

    global player1No, player2No, playerOver, turn, deck, player1, player2, logic

    ##shuffling the deck
    deck.shuffle()

    for i in range(2):
        ##giving 2 cards to each player
        player1.add_card(deck.deal())
        player2.add_card(deck.deal())

    print("Welcome to Black Jack! Each of you have got two random cards from a 54 deck. Each player can choose to get a new card or continue the game without adding a card. The one who will have hand value of 21 wins. Othervise the player with closer value to 21 wins. If both players choose not to hit and have the same value, its a tie. Good Luck!")
    ##letting the players know that cards were dealt

    while (not player1No or not player2No) and not playerOver:
        ##if no one exceeds 21 and while both did not choose not to hit already, the game continues 
        print("Player 1's cards, excepting one card: ", end='')
        player1.print_cards()
        print("Player 2's cards, excepting one card: ", end='')
        player2.print_cards()
        print()

        if turn == 'Player 1':
            logic.playerTurn(turn, player1)
            player1.check_values_over()
        else:
            logic.playerTurn(turn, player2)
            player2.check_values_over()

        ##next turn
        if turn == 'Player 1' and not player2No:
            turn = 'Player 2'
        elif turn == 'Player 2' and not player1No:
            turn = 'Player 1'

    if not playerOver:
        ## if both players did not want to hit, check the outcome to finish the game
        logic.checkOutcome(player1, player2)

main()
        

    
    





        
        
        
        




                
