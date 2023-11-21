import unittest
from unittest.mock import MagicMock

from blackjack import BlackjackGame
from casino import Player, Dealer, Manager, Hand, Box, Wager
from cards import Card, Deck, Shoe
from error_handling import InvalidBetError


import unittest


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = Card("♥", "A", (1, 11))
        self.assertEqual(card.suit, "♥")
        self.assertEqual(card.name, "A")
        self.assertEqual(card.value, (1, 11))

    def test_card_string_representation(self):
        card = Card("♠", "10", 10)
        self.assertEqual(str(card), "10♠ - 10.")


class TestDeck(unittest.TestCase):
    def test_deck_creation(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_shuffle_deck(self):
        deck = Deck()
        original_order = list(deck.cards)
        deck.shuffle_deck()
        shuffled_order = deck.cards
        # assert that the order has changed
        self.assertNotEqual(original_order, shuffled_order)

    def test_print_deck(self):
        # redirect standard output to capture printed content
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        deck = Deck()
        deck.print_deck()

        # reset redirect.
        sys.stdout = sys.__stdout__
        printed_content = captured_output.getvalue().strip()
        self.assertTrue(len(printed_content) > 0)


class TestShoe(unittest.TestCase):
    def test_shoe_creation_default_deck_total(self):
        shoe = Shoe()
        self.assertEqual(shoe.deck_total, 1)

    def test_shoe_creation_custom_deck_total(self):
        shoe = Shoe(deck_total=3)
        self.assertEqual(shoe.deck_total, 3)

    def test_shuffle_cards_in_shoe(self):
        shoe = Shoe()
        shoe.shuffle_new_decks_into_shoe()
        # ensure the cards are still present
        self.assertEqual(len(shoe.cards), 52)

    def test_deal_card_from_shoe(self):
        shoe = Shoe()
        shoe.shuffle_new_decks_into_shoe()
        hand = Hand()  # assume you have a Hand class
        shoe.deal_card_from_shoe(hand)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(len(shoe.cards), 51)

    def test_shuffle_new_decks_into_shoe(self):
        shoe = Shoe(deck_total=2)
        shoe.shuffle_new_decks_into_shoe()
        # check if cards from two decks are present
        self.assertEqual(len(shoe.cards), 104)


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

    def test_initial_deal(self):
        self.game.shoe.shuffle_new_decks_into_shoe()
        # call the initial_deal method
        self.game.initial_deal()

        # check that the initial deal has been done as expected
        # - check if each active box has one card
        # - the dealer has one card
        # - each active box has received a second card
        for box in self.game.boxes:
            if box.active:
                self.assertEqual(len(box.hand.cards), 2)
            else:
                # inactive boxes should not have cards
                self.assertEqual(len(box.hand.cards), 0)
        # assuming the dealer receives one card initially
        self.assertEqual(len(self.game.dealer.active_hand.cards), 1)


if __name__ == "__main__":
    unittest.main()
