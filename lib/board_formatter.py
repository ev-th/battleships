class BoardFormatter:
    def __init__(self, board):
        self.board = board
        self.top_line = "  | A | B | C | D | E | F | G | H | I | J |"
        self.divider = "--|---+---+---+---+---+---+---+---+---+---|"
        self.bottom_line = "------------------------------------------+"

    def display_ships(self):
        return self._format('ship')

    def display_shots(self):
        return self._format('shot')
    
    def _format(self, version):
        rows = [self.top_line]

        for i in range(self.board.grid_size):
            rows.append(self.divider)

            if version == 'ship':
                positions = self._format_ship_row(i)
            elif version == 'shot':
                positions = self._format_shot_row(i)

            row_str = self._format_row_index(i) + "|" + "|".join(positions) + "|"
            rows.append(row_str)

        rows.append(self.bottom_line)
        return "\n".join(rows)

    def _format_ship_row(self, row_index):
        positions = []
        for position in self.board.ship_grid[row_index]:
            if position is None:
                positions.append("   ")
            else:
                positions.append(" S ")
        return positions

    def _format_shot_row(self, row_index):
        positions = []
        for j in range(self.board.grid_size):
            if self.board.shot_grid[row_index][j]:
                if self.board.ship_grid[row_index][j]:
                    positions.append(" H ")
                else:
                    positions.append(" M ")
            else:
                positions.append("   ")
        return positions
        
    def _format_row_index(self, index):
        row_number = str(index + 1)
        if (index + 1) < 10:
            row_number += " "
        return row_number
