import unittest
from unittest.mock import MagicMock

from blackjack import BlackjackGame
from casino import Player, Dealer, Manager, Hand, Box, Wager
from cards import Card, Deck, Shoe


class TestBlackjackGame(unittest.TestCase):
    def setUp(self):
        self.mock_shoe = MagicMock(spec=Shoe)
        self.mock_shoe.shuffle_new_decks_into_shoe = MagicMock(return_value=None)
        self.game = BlackjackGame(number_of_decks=1)
        self.game.number_of_decks = self.mock_shoe

    def test_initialization(self):
        self.assertEqual(len(self.game.boxes), 7)
        self.assertIsInstance(self.game.player, Player)
        self.assertIsInstance(self.game.dealer, Dealer)
        self.assertIsInstance(self.game.number_of_decks, Shoe)

    def test_check_dealer_balance_reset(self):
        # assuming the dealer's balance is negative
        self.game.dealer.balance = -1000
        self.game.check_dealer_balance()
        self.assertIsInstance(self.game.dealer, Dealer)

    def test_check_dealer_balance_no_reset(self):
        # assuming the dealer's balance is positive
        self.game.dealer.balance = 1000
        self.game.check_dealer_balance()
        self.assertIsInstance(self.game.dealer, Dealer)

    def test_deal_card_from_shoe(self):
        mock_hand = MagicMock(spec=Hand)
        mock_hand.cards = []

        self.mock_shoe.deal_card_from_shoe = MagicMock(return_value=None)


if __name__ == "__main__":
    unittest.main()
