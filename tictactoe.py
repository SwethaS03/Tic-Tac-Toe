
class TicTacToe:
    BOARD_SIZE = 3
    EMPTY_SYMBOL = " "
    ROW_SEPARATOR = "      ═══╬═══╬═══"
    COLUMN_SEPARATOR = "║"
    COLUMN_LABELS = "   A   B   C\n"
    ROW_TEMPLATE = "   {}   {} {} {} {}\n"

    def __init__(self, player_symbol):
        self.board = [[self.EMPTY_SYMBOL] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.player_symbol = player_symbol

    def restart(self):
        self.board = [[self.EMPTY_SYMBOL] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]

    def draw_grid(self):
        rows = [self.ROW_TEMPLATE.format(i + 1, self.board[i][0], self.COLUMN_SEPARATOR,
                                          self.board[i][1], self.COLUMN_SEPARATOR, self.board[i][2])
                for i in range(self.BOARD_SIZE)]
        print(f"\n{self.COLUMN_LABELS}{self.ROW_SEPARATOR.join(rows)}")

    def edit_square(self, grid_coord):
        col, row = grid_coord[0].capitalize(), int(grid_coord[1])
        col_index = "ABC".index(col)
        row_index = row - 1
        if self.board[row_index][col_index] == self.EMPTY_SYMBOL:
            self.board[row_index][col_index] = self.player_symbol

    def did_win(self, player_symbol):
        b = self.board
        # Check rows
        for i in range(self.BOARD_SIZE):
            if all(c == player_symbol for c in b[i]):
                return True
        # Check columns
        for j in range(self.BOARD_SIZE):
            if all(b[i][j] == player_symbol for i in range(self.BOARD_SIZE)):
                return True
        # Check diagonals
        if all(b[i][i] == player_symbol for i in range(self.BOARD_SIZE)):
            return True
        if all(b[i][self.BOARD_SIZE - i - 1] == player_symbol for i in range(self.BOARD_SIZE)):
            return True
        return False

    def is_draw(self):
        return all(c != self.EMPTY_SYMBOL for row in self.board for c in row) and not self.did_win(self.player_symbol)
