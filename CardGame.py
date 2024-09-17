from random import randint
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    def __init__(self, player1: str, player2: str, num_of_cards: int):
        """Initialize the card game with two players and a deck of cards."""
        if type(player1) is not str:
            raise TypeError("first name must be str")
        if type(player2) is not str:
            raise TypeError("second name must be str")
        if type(num_of_cards) is not int or not 10 <= num_of_cards <= 25:
            self.num_of_cards = 26
        else:
            self.num_of_cards = num_of_cards
        self.player1 = Player(player1, self.num_of_cards)
        self.player2 = Player(player2, self.num_of_cards)
        self.new_deck_of_cards = DeckOfCards()
        self.new_game_called = False #("new_game can only be called once during initialization")
        self.new_game() #change

    def new_game(self):
        """Start a new game by shuffling the deck and dealing cards to the players."""
        # Check if new_game has already been called
        if self.new_game_called:
            raise RuntimeError("new_game can only be called once during initialization")
        self.new_game_called = True # # Mark new_game as called
        self.new_deck_of_cards.shuffle_deck()
        # Determine randomly who deals first
        random_deal = randint(1, 2)
        if random_deal == 1:
            self.player1.set_hand(self.new_deck_of_cards)
            self.player2.set_hand(self.new_deck_of_cards)
        else:
            self.player2.set_hand(self.new_deck_of_cards)
            self.player1.set_hand(self.new_deck_of_cards)

    def get_winner(self):
        if len(self.player1.player_deck)>len(self.player2.player_deck):
            return self.player1
        if len(self.player1.player_deck)<len(self.player2.player_deck):
            return self.player2
        else: # means len is equal
            print("\n that was a good game ended tie!")

        return None






