from lib.ship import Ship

def test_initialized_with_3_gives_length_and_health_of_3():
    ship = Ship(3)
    assert ship.length == 3
    assert ship.health == 3

def test_initialized_with_5_gives_length_and_health_of_5():
    ship = Ship(5)
    assert ship.length == 5
    assert ship.health == 5

def test_take_damage_reduces_health_from_5_to_4():
    ship = Ship(5)
    assert ship.health == 5
    ship.take_damage()
    assert ship.health == 4

def test_take_damage_reduces_health_from_2_to_1():
    ship = Ship(2)
    assert ship.health == 2
    ship.take_damage()
    assert ship.health == 1

def test_is_sunk_returns_false_when_health_is_positive():
    ship = Ship(2)
    assert ship.is_sunk() == False

def test_is_sunk_returns_true_when_health_is_0():
    ship = Ship(2)
    ship.take_damage()
    ship.take_damage()
    assert ship.is_sunk() == True