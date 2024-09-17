from unittest import TestCase
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player
from unittest.mock import patch
from unittest import mock


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("tamir", 25)
        self.deck=DeckOfCards()

    def test_valid_init(self):
        """Test valid initialization."""
        self.assertEqual(self.player.name, "tamir")
        self.assertEqual(self.player.num_of_cards, 25)
        self.assertEqual(self.player.player_deck, [])

    def test_invalid_init_type_name(self):
        """Test initialization with invalid name type."""
        with self.assertRaises(TypeError):
            player1 = Player(45, 16)

    def test_invalid_init_type_numOfCards(self):
        """Test initialization with invalid num_of_cards type."""
        player1 = Player("ami", [45, 45, 2323])
        self.assertEqual(player1.num_of_cards, 26)
        self.assertTrue(player1.num_of_cards == 26)

    def test_init_valid_upper_then_26(self):
        """Test initialization with num_of_cards greater than 26."""
        player1 = Player("ami", 27)
        self.assertEqual(player1.num_of_cards, 26)
        self.assertTrue(player1.num_of_cards == 26)

    def test_init_valid_upper_lower_then_10(self):
        """Test initialization with num_of_cards less than 10."""
        player1 = Player("ami", 9)
        self.assertEqual(player1.num_of_cards, 26)
        self.assertTrue(player1.num_of_cards == 26)

    def test_setHand_valid(self):
        """Test that the player's hand is set correctly with a valid deck."""
        self.player.set_hand(self.deck)
        self.assertEqual(len(self.player.player_deck), 25)
        """check the deck is down by 25(deck player hand)"""
        self.assertEqual(len(self.deck.cards),52-len(self.player.player_deck))

    def test_setHand_invalid_type_deck(self):
        """Test that TypeError is raised when an invalid deck type is passed."""
        deck = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.player.set_hand(deck)

    def test_setHand_unique_deck(self):
        """Check if the list of cards in the hand is unique."""
        unique = True
        self.player.set_hand(self.deck)
        for i in range(len(self.player.player_deck)):
            for j in range(i + 1, len(self.player.player_deck)):
                if self.player.player_deck[i] == self.player.player_deck[j]:
                    unique = False
                    break
        self.assertTrue(unique)

    def test_setHand_with_empty_deck(self):
        """Test that an error is raised when setting hand with an empty deck."""
        self.deck.cards = []
        with self.assertRaises(ValueError):
            self.player.set_hand(self.deck)

    def test_setHand_mock_deal_one(self):
        """Test set_hand using a mock for deal_one."""
        with patch('DeckOfCards.DeckOfCards.deal_random_one') as mock_deal_one:
            mock_deal_one.return_value = self.deck.cards.pop(0) #no shaffule first card is ace diamond Card(1,1)
            self.player.set_hand(self.deck)
            self.assertEqual(self.player.player_deck[0],Card(1,1))
            self.assertEqual(self.player.player_deck[0].value,1)
            self.assertNotIn(Card(1,1),self.deck.cards) #test the card left the  origenal deck

    def test_get_card_valid_remove_and_return_Card(self):
        """test get card remove a card from player deck and return a card"""
        self.player.set_hand(self.deck)
        self.assertEqual(len(self.player.player_deck),25)
        self.assertIsInstance(self.player.get_card(),Card) #return card
        self.assertEqual(len(self.player.player_deck), 24) #card also remove

    def test_get_card_valid_return_using_mock(self):
        with patch('Player.randint') as mock_randint:
            mock_randint.return_value=0
            self.player.player_deck=[1,2,3,4,5,6]
            self.assertEqual(self.player.get_card(),1)

    def test_add_card_valid_add(self):
        self.player.player_deck=[Card(1,1)]
        self.player.add_card(Card(1,2))
        self.assertEqual(len(self.player.player_deck),2)
        self.assertEqual(self.player.player_deck[1],Card(1,2))

    def test_add_card_invalid_card_type(self):
        card=["not card"]
        with self.assertRaises(TypeError):
            self.player.add_card(card)

    def test_add_card_invalid_duplicate(self):
        card=Card(1,1)
        self.assertEqual(len(self.player.player_deck),0) #no card added
        self.player.add_card(card)
        self.assertEqual(len(self.player.player_deck),1)
        self.player.add_card(card) #add the same card
        self.assertEqual(len(self.player.player_deck),1) #same len because same card not add







