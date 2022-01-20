from game.die import Die


class Director:
    """
    A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
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
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        # The game is played with five dice.
        for i in range(5):
            die = Die()
            self.dice.append(die)


    def start_game(self):
        """
        Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # Enhanced game play and game over messages.
        print("\n ------- Start Dice Game - Have Fun! -------\n")
        print("++++++++++++++++++++++++++++++++++++")
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

        print("++++++++++++++++++++++++++++++++++++")
        print("\n ------- Good game. Thanks for playing! -------\n")


    def get_inputs(self):
        """
        Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        # The player is asked, "Roll dice?" at the beginning of each turn. Plus enhanced input validation.
        roll_dice = input("Roll dice? [y/n] ").lower()
        
        while(roll_dice not in("y", "n")):
            roll_dice = input("Roll dice? You must enter 'y' or 'n' ").lower()
        
        # If the player answers "n" or no, the game is over. 
        self.is_playing = (roll_dice == "y")
    

    def do_updates(self):
        """
        Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        # If the player answers "y" or yes, the points are added to their score.
        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        
        self.total_score += self.score


    def do_outputs(self):
        """
        Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        # The dice values and player score are displayed on the screen.
        print(f"You rolled: {values}")
        print(f"Your roll score is: {self.score}")
        print(f"Your total score is: {self.total_score}\n")

        # If the player does not roll any ones or fives the game is over.
        self.is_playing = (self.score > 0)

        if not self.is_playing:
            return 
        
        self.score = 0