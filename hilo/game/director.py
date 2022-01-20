from game.card import Card


class Director:
    """
    A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """
        Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        # The player starts the game with 300 points.
        self.score = 300
        self.is_playing = True
        self.the_card = Card()
        self.next_card = Card()
        self.the_card_value = 0


    def start_game(self):
        """
        Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # Enhanced game play and game over messages.
        print("\n ------- Have fun playing the 'Hilo Game' -------\n")
        print("++++++++++++++++++++++++++++++++++++")
        
        while self.is_playing:
            self.guess_hi_or_lo()
            self.do_outputs()
            self.will_you_keep_playing()
        
        print("++++++++++++++++++++++++++++++++++++")
        print("\n ------- Good game. Thanks for playing! -------\n")


    def guess_hi_or_lo(self):
        """
        Ask the user if they want to drawn.

        Args:
            self (Director): An instance of Director.
        """
        if(self.the_card_value == 0):
            self.the_card.drawn()
            self.next_card.drawn()
            print(f"The card is: {self.the_card.value}")
        else:
            self.next_card.drawn()
            print(f"The card is: {self.the_card_value}")
            self.the_card.value = self.the_card_value
        
        # The player is asked, "Higher or lower?" at the beginning of each turn. Plus enhanced input validation.
        # The player guesses if the next one will be higher or lower.
        guess_option = input("Higher or lower? [h/l] ").lower()
        
        while(guess_option not in("h", "l")):
            guess_option = input("Higher or lower? You must enter 'h' or 'l' ").lower()
        
        print(f"Next card was: {self.next_card.value}")

        if(guess_option == "l"):
            if(self.next_card.value == self.the_card.value):
                self.score
            elif(self.next_card.value < self.the_card.value):
                self.score += 100
            else:
                self.score -= 75
        elif(guess_option == "h"):
            if(self.next_card.value == self.the_card.value):
                self.score
            elif(self.next_card.value > self.the_card.value):
                self.score += 100
            else:
                self.score -= 75
        
        self.the_card_value = self.next_card.value
    

    def do_outputs(self):
        """
        Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        # The dice values and player score are displayed on the screen.
        print(f"Your roll score is: {self.score}")
        #print(f"Your total score is: {self.total_score}\n")

        # If the player does not roll any ones or fives the game is over.
        self.is_playing = (self.score > 0)

        if not self.is_playing:
            return
    

    def will_you_keep_playing(self):
        """
        Ask the user if they want to keep playing the Hilo game.

        Args:
            self (Director): An instance of Director.
        """
        # The player is asked, "Play again?" at the end of each turn. Plus enhanced input validation.
        play_again = input("Play again? [y/n] ").lower()
        
        while(play_again not in("y", "n")):
            play_again = input("Play again? You must enter 'y' or 'n' ").lower()
        
        # If the player answers "n" or no, the game is over. 
        self.is_playing = (play_again == "y")

        if not self.is_playing:
            return
        
        print()
    