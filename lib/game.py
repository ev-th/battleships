class Game:
    def __init__(self, player1, player2, board_class):
        self.turn_count = 0
        self.players = [
            {"name": player1, "board": board_class()},
            {"name": player2, "board": board_class()}
        ]

    def get_unplaced_ships(self):
        board = self.get_current_player_board()
        return board.unplaced_ships

    def place_ship(self, ship, row, column, orientation):
        board = self.get_current_player_board()
        board.place(ship, row, column, orientation)

    def shoot(self, row, column):
        board = self.get_current_opponent_board()
        return board.shoot(row, column)

    def get_current_player_name(self):
        current_player_index = self.turn_count % 2
        return self.players[current_player_index]["name"]

    def get_current_player_board(self):
        current_player_index = self.turn_count % 2
        return self.players[current_player_index]["board"]

    def get_current_opponent_board(self):
        opponent_player_index = (self.turn_count + 1) % 2
        return self.players[opponent_player_index]["board"]

    def get_winner(self):
        if self.players[0]["board"].is_defeated():
            return self.players[1]["name"]
        elif self.players[1]["board"].is_defeated():
            return self.players[0]["name"]
        else:
            return None

    def next_turn(self):
        self.turn_count += 1