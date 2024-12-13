import unittest
from cards import create_deck, calculate_score, deal_card

class TestBlackjack(unittest.TestCase):
    def test_create_deck(self):
        deck = create_deck()
        self.assertEqual(len(deck), 54)  # 52 cards + 2 Jokers
        self.assertIn("Joker", deck)

    def test_calculate_score_with_aces(self):
        hand = ["A of Hearts", "A of Spades", "10 of Diamonds"]
        self.assertEqual(calculate_score(hand), 22)  # Adjusted Aces

    def test_calculate_score_with_jokers(self):
        hand = ["Joker", "10 of Diamonds"]
        self.assertEqual(calculate_score(hand), 20)  # Joker doubles score

    def test_deal_card(self):
        deck = create_deck()
        card = deal_card(deck)
        self.assertNotIn(card, deck)
        self.assertEqual(len(deck), 53)

if __name__ == "__main__":
    unittest.main()
