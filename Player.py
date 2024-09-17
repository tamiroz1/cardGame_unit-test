from Card import Card
from DeckOfCards import DeckOfCards
from random import randint
class Player:
    def __init__(self, name:str, num_of_cards):
        """Initialize a player with a name and number of cards."""
        if type(name) is not str:
            raise TypeError("name must be str")
        if type(num_of_cards) is not int or not 10 <= num_of_cards <= 25:
            print("next time enter number between 10-26,default set to 26")
            self.num_of_cards=26
        else:
            self.num_of_cards=num_of_cards
        self.name = name
        self.player_deck=[]

    def __str__(self):
        """Return a string representation of the player and their deck."""
        # יצירת רשימה של תיאורי הקלפים המפורטים
        cards_description = ', '.join(str(card) for card in self.player_deck)
        return f"{self.name} with the following cards: {cards_description}"

    def set_hand(self,deck:DeckOfCards):
         """Set the player's hand with cards from a deck."""
         if type(deck) is not DeckOfCards:
             raise TypeError("You must enter deck of cards here!!")
         if len(deck.cards)==0:
             raise ValueError("no cards in deck")
         for i in range (self.num_of_cards):
             card=deck.deal_random_one()
             self.player_deck.append(card)

    def get_card(self):
        """Get and remove a random card from the player's deck."""
        random_index=randint(0,len(self.player_deck)-1)
        return self.player_deck.pop(random_index)

    def add_card(self,card:Card):
        """Add a card to the player's deck."""
        if type(card) is not Card:
            raise TypeError("I can only add cards")
        if card not in self.player_deck:  # preventing duplicates
            self.player_deck.append(card)



