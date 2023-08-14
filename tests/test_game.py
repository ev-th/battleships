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

def test_get_unplaced_ships_first_gets_player_1_unplaced_ships():
    pass

def test_get_unplaced_ships_gets_player_2_unplaced_ships_after_next_turn_is_called():
    pass

def test_place_ship_first_places_ship_on_player_1_board():
    pass

def test_place_ship_places_ship_on_player_2_board_after_next_turn_is_called():
    pass

def test_shoot_first_shoots_player_2_board():
    pass

def test_shoot_shoots_player_1_board_after_next_turn_is_called():
    pass

def test_shoots_player_2_board_after_next_turn_is_called_twice():
    pass

def test_shoot_returns_the_return_value_of_shooting_a_board():
    pass

def test_get_current_player_name_first_gets_player_1_name():
    pass

def test_get_current_player_name_gets_player_2_name_after_next_turn_is_called():
    pass

def test_get_current_player_name_first_gets_player_1_name_after_next_turn_is_called_twice():
    pass

def test_get_current_player_board_first_gets_player_1_board():
    pass

def test_get_current_player_board_gets_player_2_board_after_next_turn_is_called():
    pass

def test_get_current_player_board_first_gets_player_1_board_after_next_turn_is_called_twice():
    pass

def test_get_current_opponent_board_first_gets_player_2_board():
    pass

def test_get_current_opponent_board_gets_player_1_board_after_next_turn_is_called():
    pass

def test_get_current_opponent_board_first_gets_player_2_board_after_next_turn_is_called_twice():
    pass

def test_get_winner_returns_player_name_if_opponents_board_is_defeated():
    pass

def test_get_winner_returns_None_name_if_neither_board_is_defeated():
    pass