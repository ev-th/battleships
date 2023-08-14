class BoardFormatter:
    @classmethod
    def display_ships(cls, board):

        top_line = "  | A | B | C | D | E | F | G | H | I | J |"
        divider = "--|---+---+---+---+---+---+---+---+---+---|"
        bottom_line = "------------------------------------------+"

        rows = [top_line]
        for i, row in enumerate(board.ship_grid):
            row_number = str(i + 1)
            if (i + 1) < 10:
                row_number += " "

            positions = []
            for position in row:
                if position is None:
                    positions.append("   ")
                else:
                    positions.append(" S ")
            
            row_str = row_number + "|" + "|".join(positions) + "|"
            rows.append(divider)
            rows.append(row_str)
        rows.append(bottom_line)
        return "\n".join(rows)


    @classmethod
    def display_shots(cls, board):
        
        top_line = "  | A | B | C | D | E | F | G | H | I | J |"
        divider = "--|---+---+---+---+---+---+---+---+---+---|"
        bottom_line = "------------------------------------------+"

        rows = [top_line]
        for i in range(board.grid_size):
            row_number = str(i + 1)
            if (i + 1) < 10:
                row_number += " "

            positions = []
            for j in range(board.grid_size):
                if board.shot_grid[i][j]:
                    if board.ship_grid[i][j]:
                        positions.append(" H ")
                    else:
                        positions.append(" M ")
                else:
                    positions.append("   ")
            row_str = row_number + "|" + "|".join(positions) + "|"
            rows.append(divider)
            rows.append(row_str)
        rows.append(bottom_line)
        return "\n".join(rows)
