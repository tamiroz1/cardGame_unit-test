import random
from Card import Card

class DeckOfCards:
    def __init__(self):
        """Initialize a deck of cards."""
        self.cards=[] # Initialize an empty list to store cards
        for value in range (1,14):
            for suit in range(1,5):
                card = Card(value,suit)
                self.cards.append(card)  # Append each card to the deck

    def shuffle_deck(self):
        """Shuffle the deck of cards."""
        random.shuffle(self.cards) # Shuffle the list of cards randomly

    def deal_random_one(self):
        """Deal one random card from the deck and remove it."""
        if len(self.cards)==0:
            raise ValueError("The deck is empty. No cards available.")
        index = random.randint(0, len(self.cards) - 1)  # Get a random index
        return self.cards.pop(index)  # Remove and return the card at the random index



