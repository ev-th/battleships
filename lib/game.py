class Game:
    def __init__(self, player1, player2, board_class):
        self.turn_count = 0
        self.players = [
            {"name": player1, "board": board_class()},
            {"name": player2, "board": board_class()}
        ]

    def get_unplaced_ships():
        pass

    def place_ship(self, row, column, length):
        pass

    def shoot(self, row, column):
        pass

    def get_current_player_name(self):
        pass

    def get_current_player_board(self):
        pass

    def get_current_opponent_board(self):
        pass

    def get_winner(self):
        pass

    def next_turn():
        pass