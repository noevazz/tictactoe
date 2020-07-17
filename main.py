from board import Board

class TicTacToe(Board):
    def __init__(self):
        super().__init__()
    
    def set_game_mode(self, game_mode):
        if game_mode == "1": # 1vs1
            self.player_1 = {}
            self.player_2 = {}
        elif game_mode == "2": # PCvsYou
            # WIP
            pass
        else:
            return False
        self.game_mode = game_mode
        return True
    
    def start_playing(self):
        if self.game_mode == "1":
            self.play_1vs1()
        elif self.game_mode == "2":
            # WIP
            pass
    
    def play_1vs1(self):
        print(super().get_board())
        while True:
            opt_player1 = input("Player 1 [X]: ")
            super().set_quadrant(opt_player1, "x")
            print(super().get_board())
            if self.check_winner() != None:
                print("the winner is", self.check_winner())
                break
            opt_player2 = input("Player 2 [O]: ")
            super().set_quadrant(opt_player2, "O")
            print(super().get_board())
            if self.check_winner() != None:
                print("the winner is", self.check_winner())
                break
    
    def check_winner(self):
        """
        Returns None if there is no winner
        Returns "X" or "O" depends of the winner
        """
        winner_options = [[1,2,3], # Horizontal line #1
                          [4,5,6], # Horizontal line #2
                          [7,8,9], # Horizontal line #3
                          [1,4,7], # Vertical line #1
                          [2,5,8], # Vertical line #2
                          [3,6,9], # Vertical line #3
                          [1,5,9], # Backslash
                          [7,5,3]] # Forward slash
        for option in winner_options:
            if super().get_quadrants()[ str(option[0]) ]["value"] == super().get_quadrants()[ str(option[1]) ]["value"] and \
                super().get_quadrants()[ str(option[0]) ]["value"] == super().get_quadrants()[ str(option[2]) ]["value"]:
               return super().get_quadrants()[ str(option[0]) ]["value"]
        return None

if __name__ == "__main__":
    gm = None
    game = TicTacToe()
    while game.set_game_mode(gm) == False:
        gm = input("Game mode [1=1vs1, 2=PCvsYou]: ")
    game.start_playing()