class Board:
    def __init__(self, ships, grid_size=10):
        self.grid_size = grid_size
        self.unplaced_ships = ships
        self.placed_ships = []
        self.ship_grid = [[None] * grid_size for _ in range(grid_size)]
        self.shot_grid = [[False] * grid_size for _ in range(grid_size)]

    def place(self, ship, row, column, orientation):
        coords = self._get_ship_placement_coordinates(ship, row, column, orientation)

        if not self._is_valid_coordinates(coords):
            raise Exception("Ship cannot be placed outside of the grid.")
        if not self._is_vacant_coordinates(coords):
            raise Exception("Ship cannot be placed on top of another ship.")

        for coord in coords:
            self.ship_grid[coord[0]][coord[1]] = ship

        self.unplaced_ships.remove(ship)
        self.placed_ships.append(ship)
    
    def shoot(self, row, column):
        self._record_shot_position(row, column)

        ship = self.ship_grid[row][column]
        if ship:
            return self._damage_ship(ship)
        else:
            return 'miss'
        
    def is_defeated(self):
        if self.placed_ships == []:
            raise Exception("There are no ships placed on the board.")
        for ship in self.placed_ships:
            if ship.health > 0:
                return False
        return True
        
    def _get_ship_placement_coordinates(self, ship, row, column, orientation):
        if orientation == 'vertical':
            return [(row + i, column) for i in range(ship.length)]
        if orientation == 'horizontal':
            return [(row, column + i) for i in range(ship.length)]

    def _is_valid_coordinates(self, coordinates):
        for row, column in coordinates:
            if row >= self.grid_size or column >= self.grid_size:
                return False
        return True
    
    def _is_vacant_coordinates(self, coordinates):
        for row, column in coordinates:
            if self.ship_grid[row][column]:
                return False
        return True
        
    def _record_shot_position(self, row, column):
        if row >= self.grid_size or column >= self.grid_size:
            raise Exception("Cannot shoot outside of the grid.")
        if self.shot_grid[row][column] == True:
            raise Exception("Cannot shoot the same coordinates twice.")
        self.shot_grid[row][column] = True

    def _damage_ship(self, ship):
        ship.take_damage()
        if ship.is_sunk():
            return 'sink'
        else:
            return 'hit'