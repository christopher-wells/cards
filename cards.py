from random import shuffle


class Card:
    """
    A single Card.
    """

    def __init__(self, suit, name, value) -> None:
        self.suit = suit
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}{self.suit} - {self.value}."


class Deck:
    """
    A Deck of Cards.
    """

    def __init__(self) -> None:
        self.suits = ("♥", "♣", "♦", "♠")
        self.names = ("A", "2", "3", "4", "5", "6", "7",
                      "8", "9", "10", "J", "Q", "K")
        self.values = ((1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
        self.cards = []
        # create deck
        for suit in self.suits:
            for name, value in zip(self.names, self.values):
                self.cards.append(Card(suit, name, value))

    def __str__(self) -> str:
        return f"A Deck of Cards."

    def shuffle_deck(self) -> list:
        # shuffle this Deck
        shuffle(self.cards)
        return self.cards

    def print_deck(self) -> None:
        # print this Deck in list order
        for card in self.cards:
            print(card)


class Shoe:
    """
    A Shoe class that contains one or more Decks. A Shoe is an object in a
    casino from which the cards are dealt.
    """

    def __init__(self, deck_total=1) -> None:
        if deck_total < 1:
            self.deck_total = 1
        else:
            self.deck_total = deck_total
        self.decks = None
        self.cards = None
        # card count for keeping track of when a new shuffle will take place
        self.card_count = 0

    def __str__(self) -> str:
        return f"A Shoe containing {self.deck_total} Decks."

    def shuffle_cards(self) -> None:
        # shuffle Cards in this Shoe
        shuffle(self.cards)

    def print_decks(self) -> None:
        # print the Cards in this Shoe in list order
        for card in self.cards:
            print(card)

    def deal_card_from_shoe(self, hand):
        # add the Card to the Hand and then remove from Deck
        hand.cards.append(self.cards[0])
        self.cards.pop(0)

    def shuffle_new_decks_into_shoe(self):
        # generate new decks for deck_total
        self.decks = [Deck() for deck in range(self.deck_total)]
        self.cards = []
        # add Cards from Decks
        for i in range(len(self.decks)):
            for card in zip(self.decks[i].cards):
                self.cards.append(card[0])
        # initial shuffle
        self.shuffle_cards()
