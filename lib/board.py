class Board:
    def __init__(self, ships):
        self.unplaced_ships = ships
        self.ship_grid = [[None] * 10 for _ in range(10)]
        self.shot_grid = [[False] * 10 for _ in range(10)]

    def place(self, ship, row, column, orientation):
        if orientation == 'vertical':
            for i in range(ship.length):
                self.ship_grid[row + i][column] = ship
        if orientation == 'horizontal':
            for i in range(ship.length):
                self.ship_grid[row][column + i] = ship

        self.unplaced_ships.remove(ship)

    def shoot(position):
        pass