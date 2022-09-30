from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.total_score = 300
        self.hi_lo = ''

        for i in range(2):
            card = Card()
            self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        print(f'\nGame over, your score was {self.total_score}. \nTry again to improve your score!')

    def get_inputs(self):
        """Generate new card values, then ask the user their hi_lo guess.

        Args:
            self (Director): An instance of Director.
        """

        for i in range(2):
            card = self.cards[i]
            card.draw()
        print(f'\nThe card is: {self.cards[0].value}')
        while True:
            self.hi_lo = input('Higher or lower? [h/l]: ')
            if self.hi_lo.upper() == 'H' or self.hi_lo.upper() == 'L':
                break
            else:
                print('That is not a valid response.')
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        first_card = self.cards[0].value
        second_card = self.cards[1].value
        if self.hi_lo.upper() == 'H' and first_card <= second_card:
            self.total_score += 100
        elif self.hi_lo.upper() == 'L' and first_card >= second_card:
            self.total_score += 100
        else:
            self.total_score -= 75
        if self.total_score <= 0:
            self.is_playing = False


    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to draw again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        value = f"{self.cards[1].value} "
        print(f"Next card was: {value}")
        print(f"Your score is: {self.total_score}")
        self.is_playing = (self.total_score > 0)
        play_again = input("Play again? [y/n]: ")
        self.is_playing = (play_again == "y")