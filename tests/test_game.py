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
    ships = Mock()
    board_object1 = Mock()
    board_object1.unplaced_ships = ships
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    result = game.get_unplaced_ships()

    assert result == ships

def test_get_unplaced_ships_gets_player_2_unplaced_ships_after_next_turn_is_called():
    ships = Mock()
    board_object1 = Mock()
    board_object2 = Mock()
    board_object2.unplaced_ships = ships
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.next_turn()
    result = game.get_unplaced_ships()

    assert result == ships

def test_place_ship_first_places_ship_on_player_1_board():
    ship = Mock()
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.place_ship(ship, 6, 2, 'vertical')

    board_object1.place.assert_called_once_with(ship, 6, 2, 'vertical')

def test_place_ship_places_ship_on_player_2_board_after_next_turn_is_called():
    ship = Mock()
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.next_turn()
    game.place_ship(ship, 6, 2, 'vertical')

    board_object2.place.assert_called_once_with(ship, 6, 2, 'vertical')

def test_shoot_first_shoots_player_2_board():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.shoot(7, 9)

    board_object2.shoot.assert_called_once_with(7, 9)

def test_shoot_shoots_player_1_board_after_next_turn_is_called():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.shoot(7, 9)
    game.next_turn()
    game.shoot(3, 4)

    board_object1.shoot.assert_called_once_with(3, 4)

def test_shoots_player_2_board_after_next_turn_is_called_twice():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.shoot(7, 9)
    game.next_turn()
    game.shoot(3, 4)
    game.next_turn()
    game.shoot(2, 1)

    board_object1.shoot.assert_called_with(3, 4)

def test_shoot_returns_the_return_value_of_shooting_a_board():
    board_object1 = Mock()
    board_object2 = Mock()
    board_object2.shoot.return_value = "miss"
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    result = game.shoot(1, 2)

    assert result == "miss"

def test_get_current_player_name_first_gets_player_1_name():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    result = game.get_current_player_name()

    assert result == "player1"

def test_get_current_player_name_gets_player_2_name_after_next_turn_is_called():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.next_turn()
    result = game.get_current_player_name()

    assert result == "player2"

def test_get_current_player_name_first_gets_player_1_name_after_next_turn_is_called_twice():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.next_turn()
    game.next_turn()
    result = game.get_current_player_name()

    assert result == "player1"

def test_get_current_player_board_first_gets_player_1_board():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    result = game.get_current_player_board()
    
    assert result == board_object1

def test_get_current_player_board_gets_player_2_board_after_next_turn_is_called():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.next_turn()
    result = game.get_current_player_board()

    assert result == board_object2

def test_get_current_player_board_first_gets_player_1_board_after_next_turn_is_called_twice():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.next_turn()
    game.next_turn()
    result = game.get_current_player_board()

    assert result == board_object1

def test_get_current_opponent_board_first_gets_player_2_board():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    result = game.get_current_opponent_board()

    assert result == board_object2

def test_get_current_opponent_board_gets_player_1_board_after_next_turn_is_called():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.next_turn()
    result = game.get_current_opponent_board()

    assert result == board_object1

def test_get_current_opponent_board_first_gets_player_2_board_after_next_turn_is_called_twice():
    board_object1 = Mock()
    board_object2 = Mock()
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    game.next_turn()
    game.next_turn()
    result = game.get_current_opponent_board()

    assert result == board_object2

def test_get_winner_returns_player_1_if_player_2_board_is_defeated():
    board_object1 = Mock()
    board_object1.is_defeated.return_value = False
    board_object2 = Mock()
    board_object2.is_defeated.return_value = True
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    result = game.get_winner()

    assert result == "player1"

def test_get_winner_returns_player_2_if_player_1_board_is_defeated():
    board_object1 = Mock()
    board_object1.is_defeated.return_value = True
    board_object2 = Mock()
    board_object2.is_defeated.return_value = False
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    result = game.get_winner()

    assert result == "player2"

def test_get_winner_returns_None_name_if_neither_board_is_defeated():
    board_object1 = Mock()
    board_object1.is_defeated.return_value = False
    board_object2 = Mock()
    board_object2.is_defeated.return_value = False
    board_class = Mock()
    board_class.side_effect = [board_object1, board_object2]
    game = Game("player1", "player2", board_class)

    result = game.get_winner()

    assert result is None