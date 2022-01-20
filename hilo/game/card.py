import random

class Card:
    """
    An individual card with a different or random number from 1 to 13.

    The responsibility of Card is to keep track of the card drawn and calculate the points earn or lose.
   
    Attributes:
        value (int): The number of card drawn.
        points (int): The number of points the card is worth if guess correctly or incorrectly.
    """

    def __init__(self):
        """
        Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        #self.points = 0
    
    def drawn(self):
        """
        Generates a new random value and calculates the points.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
        #self.points = 100 if self.value == 1 else 75 if self.value == 0 else 0