from cards import Card, Deck, Shoe


class Game:
    """The Game will follow a pre-defined set of rules.

    The Players can place wagers on any number of Boxes, up to 7 in total. There
    can be up to 3 Players on each Box. The Game will start with the active
    Boxes being dealt 1 Card each. The Dealer will be dealt 1 Card.

    The Players will be dealt a second Card and depending on the variation:
    - (EU) The Dealer will not be dealt a second Card. 
    - (US) The Dealer will be dealt a second Card that will not be shown.

    The Player that is in charge of the first Box will then decide on an action:
    - They can stand at any time, in which no more Cards will be added to the
    box total and that will be the end of their turn. - They can take another
    Card in which the total will be added to their hand.
        - If the Box total is greater than 21, they void their hand and the Box
          forfeits all it's wagers.
    - They can double-down for up to 2x their original wager, they will recieve
      1 card and that will be the end of their turn.
        - The Player can only double-down on the first 2 Cards, if any
          additional cards are taken then there will be no possibility to double
          down.
            - Exceptions to this are when a Player has split their hand.
              Detailed in the next section.
    - If the 2 cards are the same value (2 2, 3 3, J Q e.t.c.) they can split.
        - They must place another exact amount of their wager to split.
        - A split creates two seperate Hands on the Box.
        - Split Hands can double-down or split again where possible.
        - A Maximum of 5 splits can be done (Consisting of 6 Hands on one Box).
    - If a total of 21 is reached on the first 2 cards it considered Blackjack.
        - Blackjack pays 1.5x(3 to 2) the wager.
        - No action can be taken on the hand but if the Dealer is showing any
          AKQJ or 10 Card then the Player must wait to see if the dealer gets
          blackjack as to whether they will be paid or just keep their wager.
    - If a total of 21 is reached on any number of cards after the initial 2
      then the Player can no longer take any action on that Hand and the game
      moves on to the next hand. The dealer action is pre-defined and will not
      deviate from those rules.
    - The dealer will first check the hand in case of Blackjack.
    - Assuming there is no Blackjack, the Dealer will continue to draw/add
      Cards to their hand until a total of at least 17 is reached.
    - If the hand goes over 21 then the Dealers hand is void/bust and all
      remaining Boxes will recieve 1x their wager.
    - Exceptions to this are where there are boxes with double-down wagers. In
      which case, the wagers will be paid at up to 2x their value, matching the
      total wager of the Box.
    - Dealer Hands between 17-21 that beat the Hand total on a Player Box will
      take all of the wagers from that Box.
    - If the Dealer Hand total matches any Hand Total on any box will result in
      a draw/push. The wagers on that Box will be retained by the Players.

    Once all wagers have been settled, the game will begin again.

    Ace Card rules: - If either the Player or Dealer has an Ace in their Hand
    then the total will be counted as 1 or 11 depending on the total of the
    Hand.
        - If the total is 10 or less, the Ace can be counted as either 1 or 11.
        - If the total is greater than 10 then the Ace will always be counted as
          1, as to not void/bust the hand.
    """

    def __init__(self, number_of_decks) -> None:
        self.number_of_decks = Shoe(number_of_decks)
        self.player = Player()
        self.dealer = Dealer()
        self.first_box = Box()


class Hand:
    """A Hand consists of a number of Cards. The total of the Hand can not be
    more than 21 or the Hand becomes void/bust."""

    def __init__(self) -> None:
        self.cards = []
        self.total = 0

    def calculate_hand_total(self, cards) -> int:
        self.total = 0
        for card in self.cards:
            self.total += card.value
        return self.total


class Box:
    """A Box consists of a number of Wagers (Up to 3) and a Hand of Cards."""

    def __init__(self) -> None:
        self.wagers = []
        self.action = False
        self.hand = None


class Wager:
    """A wager is an amount that will be taken from the Players balance.
    There will be a maximum of 3 wagers per box."""

    self.total = 0


class Player:
    def __init__(self) -> None:
        self.balance = 1000
        self.active_wagers = []
        self.previous_wager = 0


class Dealer:
    def __init__(self) -> None:
        self.balance = 100000000
