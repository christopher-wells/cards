import unittest
from unittest.mock import MagicMock

from blackjack import BlackjackGame
from casino import Player, Dealer, Manager, Hand, Box, Wager
from cards import Card, Deck, Shoe
from error_handling import InvalidBetError


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
    
    def test_try_wager_on_box_valid_wager(self):
        player = Player("John")
        amount = 50
        box_number = 0

        # make the wager
        self.game.try_wager_on_box(player, amount, box_number)

    def test_try_wager_on_box_box_taken(self):
        player = Player("Alice")
        amount = 30
        box_number = 1

        # make the first wager
        self.game.try_wager_on_box(player, amount, box_number)

        # try to make another wager on the same box, it should raise an InvalidBetError
        with self.assertRaises(InvalidBetError):
            self.game.try_wager_on_box(player, amount, box_number)

    def test_try_wager_on_box_invalid_bet(self):
        player = Player("Bob")
        amount = 10000
        box_number = 2

        # try to make an invalid wager, it should raise an InvalidBetError
        with self.assertRaises(InvalidBetError):
            self.game.try_wager_on_box(player, amount, box_number)

    def test_try_wager_on_box_multiple_boxes(self):
        player = Player("Charlie")
        amount = 25

        # make wagers on multiple boxes
        for box_number in range(len(self.game.boxes)):
            self.game.try_wager_on_box(player, amount, box_number)


if __name__ == "__main__":
    unittest.main()
