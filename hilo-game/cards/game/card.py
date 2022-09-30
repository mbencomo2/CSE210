from random import randint

# TODO: Implement the Card class as follows...


# 1) Add the class declaration. Use the following class comment.
class Card:
    """A card with a different number of symbols on one side.

    The responsibility of Card is to keep track of the number of symbols and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of symbols on the card.
        points (int): The number of points the card is worth.
    """

    # 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Card with a value and points attribute.

            Args:
                self (Card): An instance of Card.
            """
        self.value = 0


# 3) Create the roll(self) method. Use the following method comment.

    def draw(self):
        """Generates a new random value
            
        Args:
            self (Card): An instance of Card.
        """
        self.value = randint(1, 13)

