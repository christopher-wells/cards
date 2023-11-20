class Hand:
    """
    A Hand consists of a number of Cards. The cards can have a total.
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
    A box is a position in a Game that contains wagers. In most games the
    maximum amount of wagers will be limited per box.
    """

    def __init__(self, max_wagers=0) -> None:
        self.max_wagers = max_wagers
        self.wagers = []
        self.active = False
        self.action = False
        self.hand = None


class Wager:
    """
    A wager is an amount that will be taken from the Players balance and used in
    a Box to play a Game. There can be a maximum bet amount that limits the
    amount placed in a wager.
    """

    def __init__(self) -> None:
        self.total = 0
        self.max_bet = 500


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.balance = 1000
        self.active_wagers = []
        self.previous_wager = 0
    
    def __str__(self) -> str:
        return f"{self.name} has £{self.balance} left."
        


class Dealer:
    def __init__(self) -> None:
        self.balance = 100000000
