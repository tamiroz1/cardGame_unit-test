
class Card:
    # רשימות שמות עבור הסוויטים והערכים של הקלפים
    SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
    VALUES = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, value: int, suit: int):
        """
        אתחול אובייקט Card עם ערך (value) וסוויט (suit).
        """
        if not isinstance(value, int):
            raise TypeError("value must be int")
        if not isinstance(suit, int):
            raise TypeError("suit must be int")
        if not 1 <= value <= 13:
            raise ValueError("value must be between 1-13")
        if not 1 <= suit <= 4:
            raise ValueError("suit must be between 1-4")
        self.value = value
        self.suit = suit

    def _get_comparable_value(self):
        """
        מחזיר את הערך להשוואה.
        אס (Ace) מקבל ערך 14 כדי להיחשב הקלף הגבוה ביותר.
        """
        return 14 if self.value == 1 else self.value

    def __str__(self):
        return f"{self.VALUES[self.value - 1]} of {self.SUITS[self.suit - 1]}"


    def __gt__(self, other):
        """
        השוואה בין שני קלפים כדי לבדוק אם הקלף הנוכחי גדול יותר.
        משווה קודם את הערכים של הקלפים, ואם הם שווים, משווה את הסוויטים.
        """
        if not isinstance(other, Card):
            raise TypeError("I can only compare card to card")

        # מחשבים את ערכי ההשוואה עבור כל קלף
        my_value = self._get_comparable_value()
        other_value = other._get_comparable_value()

        # משווים קודם לפי הערך של הקלפים, ואם שווים - לפי הסוויט
        return (my_value, self.suit) > (other_value, other.suit)

    def __eq__(self, other):
        """
        בדיקה אם שני קלפים שווים, כלומר יש להם גם אותו ערך וגם אותו סוויט.
        """
        if not isinstance(other, Card):
            raise TypeError("I can only compare card to card")
        return self.value == other.value and self.suit == other.suit
