from lib.board_formatter import BoardFormatter
from unittest.mock import Mock

def test_display_ships_displays_empty_ship_grid():
    ship_grid = [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
    ]
    board = Mock()
    board.ship_grid = ship_grid
    board.grid_size = 10

    formatter = BoardFormatter(board)
    result = formatter.display_ships()

    expected_result = '  | A | B | C | D | E | F | G | H | I | J |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '1 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '2 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '3 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '4 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '5 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '6 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '7 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '8 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '9 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '10|   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '------------------------------------------+'
    
    assert result == expected_result

def test_display_ships_displays_multiple_ships():
    ship1 = Mock()
    ship2 = Mock()
    ship3 = Mock()
    ship_grid = [
        [None, ship1, ship1, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, ship2, None, None, None, None, None],
        [None, None, None, None, ship2, None, None, None, None, None],
        [None, None, None, None, ship2, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, ship3, ship3, ship3, ship3, None]
    ]
    board = Mock()
    board.ship_grid = ship_grid
    board.grid_size = 10


    formatter = BoardFormatter(board)
    result = formatter.display_ships()

    expected_result = '  | A | B | C | D | E | F | G | H | I | J |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '1 |   | S | S |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '2 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '3 |   |   |   |   | S |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '4 |   |   |   |   | S |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '5 |   |   |   |   | S |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '6 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '7 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '8 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '9 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '10|   |   |   |   |   | S | S | S | S |   |\n'
    expected_result += '------------------------------------------+'
    
    assert result == expected_result

def test_display_shots_displays_empty_shot_grid():
    shot_grid = [
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

    board = Mock()
    board.grid_size = 10
    board.shot_grid = shot_grid

    formatter = BoardFormatter(board)
    result = formatter.display_shots()

    expected_result = '  | A | B | C | D | E | F | G | H | I | J |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '1 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '2 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '3 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '4 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '5 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '6 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '7 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '8 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '9 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '10|   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '------------------------------------------+'

    assert result == expected_result

def test_display_shots_displays_shots():
    shot_grid = [
        [False, True, True, True, True, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, True, True]
    ]

    ship1 = Mock()
    ship2 = Mock()
    ship3 = Mock()
    ship_grid = [
        [None, ship1, ship1, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, ship2, None, None, None, None, None],
        [None, None, None, None, ship2, None, None, None, None, None],
        [None, None, None, None, ship2, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, ship3, ship3, ship3, ship3, None],
    ]

    board = Mock()
    board.ship_grid = ship_grid
    board.shot_grid = shot_grid
    board.grid_size = 10

    formatter = BoardFormatter(board)
    result = formatter.display_shots()

    expected_result = '  | A | B | C | D | E | F | G | H | I | J |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '1 |   | H | H | M | M |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '2 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '3 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '4 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '5 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '6 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '7 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '8 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '9 |   |   |   |   |   |   |   |   |   |   |\n'
    expected_result += '--|---+---+---+---+---+---+---+---+---+---|\n'
    expected_result += '10|   |   |   |   |   |   |   |   | H | M |\n'
    expected_result += '------------------------------------------+'

    assert expected_result == result