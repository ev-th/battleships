from lib.board import Board
from unittest.mock import Mock
import pytest

def test_is_initialized_with_a_list_of_unplaced_ships():
    ship1 = Mock()
    ship2 = Mock()
    ship3 = Mock()
    ships = [ship1, ship2, ship3]

    board = Board(ships)

    assert board.unplaced_ships == ships

def test_is_initialized_with_an_empty_ship_grid():
    board = Board([])
    expected_grid = [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None]
    ]
    assert board.ship_grid == expected_grid

def test_is_initialized_with_an_unhit_shot_grid():
    board = Board([])
    expected_grid = [
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False]
    ]
    assert board.shot_grid == expected_grid

def test_places_a_length_2_ship_on_the_top_left_corner_vertically():
    ship = Mock()
    ship.length = 2
    board = Board([ship])
    board.place(ship, 0, 0, 'vertical')
    expected_grid = [
        [ship, None, None, None, None, None, None, None, None, None],
        [ship, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None]
    ]
    assert board.ship_grid == expected_grid

def test_places_a_length_3_ship_on_the_bottom_left_corner_horizontally():
    ship = Mock()
    ship.length = 3
    board = Board([ship])
    board.place(ship, 9, 0, 'horizontal')
    expected_grid = [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [ship, ship, ship, None, None, None, None, None, None, None]
    ]
    assert board.ship_grid == expected_grid

def test_places_a_length_4_ship_on_the_top_right_corner_horizontally():
    ship = Mock()
    ship.length = 4
    board = Board([ship])
    board.place(ship, 0, 6, 'horizontal')
    expected_grid = [
        [None, None, None, None, None, None, ship, ship, ship, ship],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None]
    ]
    assert board.ship_grid == expected_grid

def test_places_a_length_5_ship_on_the_bottom_right_corner_vertically():
    ship = Mock()
    ship.length = 5
    board = Board([ship])
    board.place(ship, 5, 9, 'vertical')
    expected_grid = [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, ship],
        [None, None, None, None, None, None, None, None, None, ship],
        [None, None, None, None, None, None, None, None, None, ship],
        [None, None, None, None, None, None, None, None, None, ship],
        [None, None, None, None, None, None, None, None, None, ship]
    ]
    assert board.ship_grid == expected_grid

def test_places_several_ships_on_the_board():
    ship1 = Mock()
    ship1.length = 2
    ship2 = Mock()
    ship2.length = 3
    ship3 = Mock()
    ship3.length = 3
    ship4 = Mock()
    ship4.length = 4
    ship5 = Mock()
    ship5.length = 5

    ships = [ship1, ship2, ship3, ship4, ship5]
    board = Board(ships)

    board.place(ship1, 0, 1, 'vertical')
    board.place(ship2, 2, 3, 'horizontal')
    board.place(ship3, 5, 6, 'horizontal')
    board.place(ship4, 6, 5, 'vertical')
    board.place(ship5, 1, 2, 'vertical')

    expected_grid = [
        [None, ship1, None, None, None, None, None, None, None, None],
        [None, ship1, ship5, None, None, None, None, None, None, None],
        [None, None, ship5, ship2, ship2, ship2, None, None, None, None],
        [None, None, ship5, None, None, None, None, None, None, None],
        [None, None, ship5, None, None, None, None, None, None, None],
        [None, None, ship5, None, None, None, ship3, ship3, ship3, None],
        [None, None, None, None, None, ship4, None, None, None, None],
        [None, None, None, None, None, ship4, None, None, None, None],
        [None, None, None, None, None, ship4, None, None, None, None],
        [None, None, None, None, None, ship4, None, None, None, None]
    ]
    assert board.ship_grid == expected_grid

def test_placing_ship_removes_it_from_unplaced_ships():
    ship1 = Mock()
    ship1.length = 2
    ship2 = Mock()
    ship2.length = 3

    board = Board([ship1, ship2])
    board.place(ship1, 0, 0, 'vertical')
    assert board.unplaced_ships == [ship2]

def test_placing_multiple_ships_removes_them_from_unplaced_ships():
    ship1 = Mock()
    ship1.length = 2
    ship2 = Mock()
    ship2.length = 3
    ship3 = Mock()
    ship3.length = 5

    board = Board([ship1, ship2, ship3])
    board.place(ship2, 0, 0, 'vertical')
    board.place(ship3, 0, 1, 'vertical')
    assert board.unplaced_ships == [ship1]

def test_placing_ship_past_the_right_of_the_board_raises_error():
    ship = Mock()
    ship.length = 3
    board = Board([ship])
    with pytest.raises(Exception) as e:
        board.place(ship, 0, 8, 'horizontal')
    error_message = str(e.value)
    assert error_message == "Ship cannot be placed outside of the grid."


def test_placing_ship_past_the_bottom_of_the_board_raises_error():
    ship = Mock()
    ship.length = 2
    board = Board([ship])
    with pytest.raises(Exception) as e:
        board.place(ship, 9, 5, 'vertical')
    error_message = str(e.value)
    assert error_message == "Ship cannot be placed outside of the grid."

def test_placing_ship_horizontally_on_top_of_another_raises_error():
    ship1 = Mock()
    ship1.length = 2
    ship2 = Mock()
    ship2.length = 3

    board = Board([ship1, ship2])
    board.place(ship1, 1, 1, 'vertical')
    with pytest.raises(Exception) as e:
        board.place(ship2, 1, 0, 'horizontal')
    error_message = str(e.value)
    assert error_message == "Ship cannot be placed on top of another ship."

def test_placing_ship_horizontally_on_top_of_another_raises_error():
    ship1 = Mock()
    ship1.length = 2
    ship2 = Mock()
    ship2.length = 3

    board = Board([ship1, ship2])
    board.place(ship1, 1, 1, 'horizontal')
    with pytest.raises(Exception) as e:
        board.place(ship2, 0, 1, 'vertical')
    error_message = str(e.value)
    assert error_message == "Ship cannot be placed on top of another ship."

def test_shoot_updates_shot_grid_at_correct_position():
    board = Board([])
    board.shoot(0, 0)
    expected_grid = [
        [True, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
    ]
    assert board.shot_grid == expected_grid

def test_shoot_can_add_multiple_shots():
    board = Board([])
    board.shoot(0, 0)
    board.shoot(1, 2)
    board.shoot(9, 9)
    board.shoot(5, 7)
    expected_grid = [
        [True, False, False, False, False, False, False, False, False, False],
        [False, False, True, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, True, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, True],
    ]
    assert board.shot_grid == expected_grid

def test_shoot_calls_take_damage_on_ship_at_the_same_coords():
    ship = Mock()
    ship.length = 4
    board = Board([ship])
    board.place(ship, 0, 0, 'horizontal')
    board.shoot(0, 1)
    ship.take_damage.assert_called_once()

def test_shoot_returns_miss_when_there_is_no_ship_at_coords():
    board = Board([])
    assert board.shoot(0, 0) == 'miss'

def test_shoot_returns_hit_when_there_is_ship_at_coords_but_not_sunk():
    ship = Mock()
    ship.length = 3
    ship.is_sunk.return_value = False
    board = Board([ship])
    board.place(ship, 0, 0, 'horizontal')
    board.shoot(0, 1)
    assert board.shoot(0, 0) == 'hit'

def test_shoot_returns_sunk_when_there_is_ship_at_coords_and_it_is_sunk():
    ship = Mock()
    ship.length = 3
    ship.is_sunk.return_value = True
    board = Board([ship])
    board.place(ship, 0, 0, 'horizontal')
    assert board.shoot(0, 0) == 'sink'

def test_shoot_raises_error_when_coords_have_already_taken_a_shot():
    board = Board([])
    board.shoot(5, 5)
    with pytest.raises(Exception) as e:
        board.shoot(5, 5)
    assert str(e.value) == "Cannot shoot the same coordinates twice."

def test_shoot_raises_error_when_row_value_is_too_high():
    board = Board([])
    with pytest.raises(Exception) as e:
        board.shoot(10, 5)
    assert str(e.value) == "Cannot shoot outside of the grid."

def test_shoot_raises_error_when_column_value_is_too_high():
    board = Board([])
    with pytest.raises(Exception) as e:
        board.shoot(5, 10)
    assert str(e.value) == "Cannot shoot outside of the grid."
    pass
