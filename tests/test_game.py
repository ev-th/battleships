from lib.game import Game
from unittest.mock import Mock

def test_game_is_initilized_with_two_boards():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]

    game = Game("player1", "player2", board_class)

    assert game.players == [
            {"name": "player1", "board": board_object1},
            {"name": "player2", "board": board_object2}
        ]

def test_game_initialized_with_turn_count_at_0():
    board_class = Mock()
    game = Game("player1", "player2", board_class)
    assert game.turn_count == 0
