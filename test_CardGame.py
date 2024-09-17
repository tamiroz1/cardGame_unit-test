from unittest import TestCase



from unittest import TestCase
from unittest.mock import patch, MagicMock
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player
from CardGame import CardGame

class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("Player1", "Player2", 15)

    def test_init_valid(self):
        """Test valid initialization."""
        self.assertEqual(self.game.player1.name, "Player1")
        self.assertEqual(self.game.player2.name, "Player2")
        self.assertEqual(self.game.player1.num_of_cards, 15)
        self.assertEqual(self.game.player2.num_of_cards, 15)
        self.assertIsInstance(self.game.new_deck_of_cards, DeckOfCards)
        self.assertTrue(self.game.new_game_called) #because new_game function was on in init

    def test_init_invalid_type_player1(self):
        """Test initialization with invalid player1 type."""
        with self.assertRaises(TypeError):
            CardGame(123, "Player2", 15)

    def test_init_invalid_type_player2(self):
        """Test initialization with invalid player2 type."""
        with self.assertRaises(TypeError):
            CardGame("Player1", 456, 15)

    def test_init_invalid_type_num_of_card(self):
        """Test initialization with invalid type num_of_card type."""
        game= CardGame("Player1", "Player2", "15")
        self.assertEqual(game.num_of_cards,26)
    def test_init_invalid_range_num_of_cards(self):
        """Test initialization with invalid range num_of_cards value."""
        game = CardGame("Player1", "Player2", 30)
        self.assertEqual(game.num_of_cards, 26)

    def test_new_game_called_once(self):
        """Test that new_game can only be called once."""
        with self.assertRaises(RuntimeError):
            self.game.new_game()

    def test_new_game_shuffles_deck(self):
        """Test that new_game shuffles the deck."""
        deck2=DeckOfCards()
        self.assertNotEqual(deck2.cards,self.game.new_deck_of_cards.cards)


    def test_new_game_deals_different_cards(self):
        """Test that new_game deals cards to players different cards."""
        for card in self.game.player1.player_deck:
            self.assertNotIn(card, self.game.player2.player_deck)

    def test_new_game_len_of_decks(self):
        """test that new game set the cards correctly"""
        deck=DeckOfCards()
        self.assertEqual(len(self.game.player1.player_deck),15)
        self.assertEqual(len(self.game.player2.player_deck),15)
        self.assertEqual(len(self.game.new_deck_of_cards.cards),len(deck.cards)-len(self.game.player1.player_deck)-len(self.game.player2.player_deck))
    def test_get_winner_player1_wins(self):
        """Test get_winner when player1 has more cards."""
        self.game.player1.player_deck = [1,2]
        self.game.player2.player_deck = [1]
        self.assertEqual(self.game.get_winner(), self.game.player1)

    def test_get_winner_player2_wins(self):
        """Test get_winner when player2 has more cards."""
        self.game.player1.player_deck = [1]
        self.game.player2.player_deck = [1,2]
        self.assertEqual(self.game.get_winner(), self.game.player2)

    def test_get_winner_tie(self):
        """Test get_winner when both players have equal number of cards."""
        self.game.player1.player_deck = [1]
        self.game.player2.player_deck = [1]
        self.assertEqual(self.game.get_winner(), None)


