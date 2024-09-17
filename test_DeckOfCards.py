from unittest import TestCase
from Card import Card
from DeckOfCards import DeckOfCards



class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_deck_contains_all_cards(self):
        """Check the init - if the deck created contains all the unique cards from 1 to 13 in each suit"""
        for value in range(1, 14):
            for suit in range(1, 5):
                card=Card(value, suit)
                self.assertIn(card,self.deck.cards)


    def test_init_len(self):
        """Check if the deck is initialized with 52 cards"""
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_unique_cards(self):
        """check if the list of card is unique, cant use set on list pf objects"""
        unique = True
        cards = self.deck.cards
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                if cards[i] == cards[j]:
                    unique = False
                    break
        self.assertTrue(unique)

    def test_cards_shuffle(self):
        """Test if the shuffle method changes the order of the cards"""
        original_deck = self.deck.cards.copy()
        self.deck.shuffle_deck()
        self.assertNotEqual(original_deck, self.deck.cards)

    def test_deal_one_return_card(self):
        """Test that deal_one method returns a Card object and reduces deck size by one"""
        self.assertEqual(len(self.deck.cards), 52)
        dealt_card = self.deck.deal_random_one()
        self.assertIsInstance(dealt_card, Card)
        self.assertEqual(len(self.deck.cards), 51)
        self.assertNotIn(dealt_card, self.deck.cards)

    def test_deal_one_no_cards(self):
        """check if no card in list raises error"""
        self.deck.cards=[] #reset list to empty (in the class)
        with self.assertRaises(ValueError):
            self.deck.deal_random_one()

    def test_deck_contains_only_card_objects(self):
        """Test if all the cards in deck are object Card"""
        for card in self.deck.cards:
            self.assertIsInstance(card,Card)
