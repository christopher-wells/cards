class DiscardHolder:
    """
    All previous cards from a blackjack Hand will go here.
    The shuffle will be done from these cards at the end of the shoe.
    """

    def __init__(self) -> None:
        self.cards = []

    def __str__(self) -> str:
        return f"A Discard pile containing {len(self.cards)} cards."


class Hand:
    """
    A Hand consists of a number of Cards. The Cards can have a total.
    """

    def __init__(self) -> None:
        self.cards = []
        self.total = 0

    def __str__(self) -> str:
        return f"A hand containing {len(self.cards)} cards."

    def calculate_hand_total(self, cards) -> int:
        self.total = 0
        for card in self.cards:
            self.total += card.value
        return self.total

    def return_cards_to_discard_holder(self, discard_holder) -> None:
        for card in self.cards:
            discard_holder.cards.append(card)
            self.cards.remove(card)


class Box:
    """
    A box is a position in a Game that contains Wagers. In most games the
    maximum amount of Wagers will be limited per box.
    There can be a maximum bet amount that limits the amount placed in a wager.
    """

    def __init__(self, max_wagers=0, max_bet=0) -> None:
        self.max_wagers = max_wagers
        self.max_bet = max_bet

        self.wagers = []
        self.wager_count = 0
        self.wager_total = 0

        self.active = False
        self.action = False

        self.hand = None
        self.invalid_bet = False

    def __str__(self) -> str:
        return f"A box containing {len(self.wagers)} wagers."


class Wager:
    """
    A Wager is an amount that will be taken from the Players balance and used in
    a Box to play a Game.
    """

    def __init__(self, amount, owner) -> None:
        if amount > 0:
            self.amount = amount
        else:
            self.amount = 1
        self.owner = owner

    def __str__(self) -> str:
        return f"{self.owner}'s Wager of £{self.amount}."


class Player:
    """
    The Player class. Can add Wagers to different Boxes and play Games.
    If auto_player then will follow one or more strategies to play Games.
    """

    def __init__(self, name="Player", auto_player=False) -> None:
        self.name = name
        self.balance = 10000
        self.auto_player = auto_player

        self.active_wagers = []
        self.previous_wager = 0

        self.active_boxes = []
        self.active_hands = []

    def __str__(self) -> str:
        return f"{self.name} has £{self.balance} left."


class Dealer:
    """
    The Dealer class. Will follow pre-defined rules for the Games and pay or
    take the Wagers.
    """

    def __init__(self) -> None:
        self.balance = 100000000
        self.active_hand = None


class Manager:
    """
    Does nothing.
    """

    pass
