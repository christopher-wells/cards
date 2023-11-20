from random import shuffle


class Card:
    """A single Card."""

    def __init__(self, suit, name, value) -> None:
        self.suit = suit
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"The {self.name} of {self.suit} - {self.value}."


class Deck:
    """A Deck of Cards."""

    def __init__(self) -> None:
        self.suits = ("Hearts", "Clubs", "Diamonds", "Spades")
        self.names = (
            "Ace",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Jack",
            "Queen",
            "King",
        )
        self.values = ((1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
        self.cards = []
        # create deck
        for suit in self.suits:
            for name, value in zip(self.names, self.values):
                self.cards.append(Card(suit, name, value))

    def __str__(self) -> str:
        return f"A Deck of Cards."

    def shuffle_deck(self) -> list:
        """Shuffle this Deck."""
        shuffle(self.cards)
        return self.cards
    
    def print_deck(self) -> None:
        "Print this Deck in list order."
        for card in self.cards:
            print(card)


class Shoe:
    """A Shoe class that contains one or more Decks.
    A Shoe is an object in a casino from which the cards are dealt."""

    def __init__(self, deck_total=1) -> None:
        if deck_total < 1:
            self.deck_total = 1
        else:
            self.deck_total = deck_total
        self.decks = [Deck() for deck in range(self.deck_total)]
        self.cards = []

    def __str__(self) -> str:
        return f"A Shoe containing {self.deck_total} Decks."
    
    def insert_decks_into_shoe(self) -> None:
        for i in range(len(self.decks)):
            for card in zip(self.decks[i].cards):
                self.cards.append(card[0])
    
    def shuffle_decks(self) -> list:
        """Shuffle Decks in this Shoe."""
        shuffle(self.cards)
        return self.cards
    
    def print_decks(self) -> None:
        "Print the Cards in this Shoe in list order."
        for card in self.cards:
            print(card)


# initialise 2 deck shoe and print the cards inside and card totals
shoe = Shoe(6)
shoe.insert_decks_into_shoe()
shoe.shuffle_decks()
shoe.print_decks()