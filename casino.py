class Hand:
    """
    A Hand consists of a number of Cards. The Cards can have a total.
    """

    def __init__(self) -> None:
        self.cards = []
        self.total = 0

    def calculate_hand_total(self, cards) -> int:
        self.total = 0
        for card in self.cards:
            self.total += card.value
        return self.total


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

        self.active = False
        self.action = False

        self.hand = None
        self.invalid_bet = False

    def __str__(self) -> str:
        return f"A box containing {len(self.wagers)} wagers."

    def calculate_if_max_bet_exceeded(self) -> bool:
        box_total = 0
        for wager in self.wagers:
            box_total += wager.total
        if box_total > self.max_bet:
            self.invalid_bet = True
            return self.invalid_bet
        else:
            self.invalid_bet = False
            return self.invalid_bet


class Wager:
    """
    A Wager is an amount that will be taken from the Players balance and used in
    a Box to play a Game.
    """

    def __init__(self) -> None:
        self.total = 0


class Player:
    """
    The Player class. Can add Wagers to different Boxes and play Games.
    If auto_player then will follow one or more strategies to play Games.
    """

    def __init__(self, name, auto_player=False) -> None:
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
