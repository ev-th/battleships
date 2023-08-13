class Board:
    def __init__(self, ships):
        self.unplaced_ships = ships
        self.ship_grid = [[None] * 10 for _ in range(10)]
        self.shot_grid = [[False] * 10 for _ in range(10)]

    def place(self, ship, row, column, orientation):
        if orientation == 'vertical':
            if row + ship.length - 1 >= 10:
                raise Exception("Ship cannot be placed outside of the grid.")
            for i in range(ship.length):
                if self.ship_grid[row + i][column] != None:
                    raise Exception("Ship cannot be placed on top of another ship")
            for i in range(ship.length):
                self.ship_grid[row + i][column] = ship
        if orientation == 'horizontal':
            if column + ship.length - 1 >= 10:
                raise Exception("Ship cannot be placed outside of the grid.")
            for i in range(ship.length):
                if self.ship_grid[row][column + i] != None:
                    raise Exception("Ship cannot be placed on top of another ship")
            for i in range(ship.length):
                self.ship_grid[row][column + i] = ship

        self.unplaced_ships.remove(ship)

    def shoot(self, row, column):
        self.shot_grid[row][column] = True
        ship = self.ship_grid[row][column]
        if ship:
            ship.take_damage()
            if ship.is_sunk() == False:
                return 'hit'
            else:
                return 'sink'
        return 'miss'
