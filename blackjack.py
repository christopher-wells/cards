from casino import Player, Dealer, Box, Wager, Hand
from cards import Card, Deck, Shoe
from error_handling import InvalidBetError


class BlackjackGame:
    """
    BlackjackGame will follow a pre-defined set of rules.

    The Players can place wagers on any number of Boxes, up to 7 in total. There can be 1 Player on each Box.
    The Game will start with the active Boxes being dealt 1 Card each. The Dealer will be dealt 1 Card. The Players
    will be dealt a second Card, and depending on the variation:
    - (EU) The Dealer will not be dealt a second Card.
    - (US) The Dealer will be dealt a second Card that will not be shown.

    The Player in charge of the first Box will then decide on an action:
    - They can stand at any time, in which no more Cards will be added to the box total, and that will be the end
      of their turn.
    - They can take another Card in which the total will be added to their hand.
      - If the Box total is greater than 21, they void their hand, and the Box forfeits all its wagers.
    - They can double down for up to 2x their original wager; they will receive 1 card, and that will be the end of
      their turn.
      - The Player can only double down on the first 2 Cards; if any additional cards are taken, then there will
        be no possibility to double down.
        - Exceptions to this are when a Player has split their hand, detailed in the next section.
    - If the 2 cards are the same value (2 2, 3 3, J Q, etc.), they can split.
      - They must place another exact amount of their wager to split.
      - A split creates two separate Hands on the Box.
      - Split Hands can double down or split again where possible.
      - A maximum of 5 splits can be done (Consisting of 6 Hands on one Box).
    - If a total of 21 is reached on the first 2 cards, it is considered Blackjack.
      - Blackjack pays 1.5x (3 to 2) the wager.
      - No action can be taken on the hand, but if the Dealer is showing any AKQJ or 10 Card, then the Player must
        wait to see if the dealer gets blackjack as to whether they will be paid or just keep their wager.
    - If a total of 21 is reached on any number of cards after the initial 2, then the Player can no longer take any
      action on that Hand, and the game moves on to the next hand.

    The Dealer action is pre-defined and will not deviate from those rules:
    - The Dealer will first check the hand in case of Blackjack.
    - Assuming there is no Blackjack, the Dealer will continue to draw/add Cards to their hand until a total of at
      least 17 is reached.
    - If the hand goes over 21, then the Dealer's hand is void/bust, and all remaining Boxes will receive 1x their
      wager.
      - Exceptions to this are where there are boxes with double-down wagers. In which case, the wagers will be paid
        at up to 2x their value, matching the total wager of the Box.
    - Dealer Hands between 17-21 that beat the Hand total on a Player Box will take all of the wagers from that Box.
    - If the Dealer Hand total matches any Hand Total on any box will result in a draw/push. The wagers on that Box
      will be retained by the Players.

    Once all wagers have been settled, the game will begin again.

    Ace Card rules:
    - If either the Player or Dealer has an Ace in their Hand, then the total will be counted as 1 or 11 depending
      on the total of the Hand.
      - If the total is 10 or less, the Ace can be counted as either 1 or 11.
        - This can give soft totals and hard totals of a hand.
          Soft totals are where a hand can be of 2 values, and hard totals are where a hand has only 1 value. For
          example:
          - The hand total consists of a 5 and an A. This gives the hand total as 6 or 16. If another card is drawn
            to the hand, let's say it is a card with a value of 10. Instead of calling the hand total as 16 or 26,
            we will just use the hard total of 16.
          - The hand total consists of a 2 and an A. This gives the hand total as 3 or 13. If another card is drawn
            to the hand, let's say it is a card with a value of 2. We would then call the hand total as 5 or 15. If
            another card is drawn to the hand, let's say it is a card with a value of 10. Now the hand total would
            just be 15.
      - If the total is greater than 10, then the Ace will always be counted as 1, as to not void/bust the hand.

    """

    def __init__(self, number_of_decks) -> None:
        self.shoe = Shoe(number_of_decks)
        self.player = Player("Pope Gregory IX")
        self.dealer = Dealer()

        self.max_boxes = 7
        self.max_wagers_per_box = 1
        self.max_bet_per_box = 5000

        self.boxes = [
            Box(max_wagers=self.max_wagers_per_box, max_bet=self.max_bet_per_box)
            for box in range(self.max_boxes)
        ]

    def try_wager_on_box(self, player, amount, box_number):
        # check if box is free first
        if not self.boxes[box_number].active:
            self.boxes[box_number].active = True
        else:
            raise InvalidBetError("The Box is currently taken.")
        # if there is a spot free and it doesn't exceed any limits, allow the wager
        for box in self.boxes:
            if (
                box.wager_count < box.max_wagers
                and box.wager_total < box.max_bet
                and (amount + box.wager_total) < box.max_bet
            ):
                box.wagers.append(Wager(amount, player))
            else:
                raise InvalidBetError("The bet was invalid.")

    def initial_deal(self):
        # first card
        for box in self.boxes:
            if box.active:
                box.hand = Hand()
                self.shoe.deal_card_from_shoe(box.hand)
            else:
                # avoid None type in cards
                box.hand = Hand()
                box.hand.card = 0
        # dealer card
        self.dealer.active_hand = Hand()
        self.shoe.deal_card_from_shoe(self.dealer.active_hand)
        # second card
        for box in self.boxes:
            if box.active:
                self.shoe.deal_card_from_shoe(box.hand)

    def check_dealer_balance(self):
        # reset dealer balance
        if self.dealer.balance < 0:
            print("A change of dealer will begin now.")
            self.dealer = Dealer()
        else:
            pass
