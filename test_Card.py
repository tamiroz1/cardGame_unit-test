from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card=Card(13,1) # King of diamond
    """TESTING FOR __init__"""
    def test_init_valid(self):
        """Test initializing a card with valid values."""
        self.assertEqual(self.card.value,13)
        self.assertEqual(self.card.suit,1)

    def test_value_out_of_range_high(self):
        """Test initializing a card with a value above the valid range."""
        with self.assertRaises(ValueError):
            Card(14, 3)

    def test_value_out_of_range_low(self):
        """Test initializing a card with a value below the valid range."""
        with self.assertRaises(ValueError):
            Card(0, 3)
    def test_suit_out_of_range_high(self):
        """Test initializing a card with a suit above the valid range."""
        with self.assertRaises(ValueError):
            Card(10, 5)

    def test_suit_out_of_range_low(self):
        """Test initializing a card with a suit below the valid range."""
        with self.assertRaises(ValueError):
            Card(10, 0)
    def test_invalid_value_type(self):
        """Test initializing a card with an invalid value type."""
        with self.assertRaises(TypeError):
            Card("5",2)

    def test_invalid_suit_type(self):
        """Test initializing a card with an invalid suit type."""
        with self.assertRaises(TypeError):
            Card(6,"2")

    """TESTING FOR __gt__"""
    def test_gt_higher_value(self):
        """Testing if a card with a higher value is considered greater."""
        card = Card(13, 1)  # King of Diamonds
        other_card = Card(10, 2)  # 10 of Spades
        self.assertTrue(card > other_card)

    def test_gt_lower_value(self):
        """Testing if a card with a lower value is not considered greater."""
        card = Card(13, 1)  # King of Diamonds
        other_card = Card(2, 3)  # 2 of Hearts
        self.assertFalse(other_card > card)

    def test_gt_equal_value_higher_suit(self):
        """Testing if a card with equal value but lower suit is not considered greater."""
        card = Card(13, 2)  # King of spades
        other_card = Card(13, 1)  # King of diamonds
        self.assertTrue(card > other_card)

    def test_gt_equal_value_lower_suit(self):
        """Testing if a card with equal value but lower suit is considered greater."""
        card = Card(13, 1)  # King of Diamonds
        other_card = Card(13, 2)  # King of spades
        self.assertFalse(card > other_card)

    def test_gt_equal_value_equal_suit(self):
        """Testing if two identical cards are not considered greater."""
        card = Card(13, 1)  # King of Diamonds
        other_card = Card(13, 1)  # King of Diamonds
        self.assertFalse(card > other_card)

    def test_gt_ace_higher_than_king(self):
        """Testing if Ace is considered greater than King."""
        card = Card(13, 1)  # King of Diamonds
        other_card = Card(1, 4)  # Ace of Clubs
        self.assertTrue(other_card > card)

    def test_gt_invalid_testing(self):
        """Testing with a non-card object raises TypeError."""
        card = Card(13, 4)  # King of clubs
        with self.assertRaises(TypeError):
            if card > 3:
                print("bad test")

    """TESTING FOR __eq__"""
    def test_equal_cards(self):
        """Test that two cards with the same value and suit are equal."""
        card1 = Card(10, 1)
        card2 = Card(10, 1)
        self.assertEqual(card1,card2)
        self.assertTrue(card1 == card2)

    def test_unequal_cards_different_value(self):
        """Test that two cards with different values are not equal."""
        card1 = Card(10, 1)
        card2 = Card(9, 1)
        self.assertFalse(card1==card2)

    def test_unequal_cards_different_suit(self):
        """Test that two cards with the same value but different suits are not equal."""
        card1 = Card(10, 1)
        card2 = Card(10, 2)
        self.assertNotEqual(card1, card2)
        self.assertFalse(card1==card2)

    def test_compare_with_non_card(self):
        """Test that comparing a card with a non-card raises a TypeError."""
        card = Card(10, 1)
        with self.assertRaises(TypeError):
            card == 10 or card==1








