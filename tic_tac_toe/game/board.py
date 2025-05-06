class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display(self):
        return [self.board[i:i+3] for i in range(0, 9, 3)]

    def place_move(self, position, marker):
        if self.board[position - 1] not in ["X", "O"]:
            self.board[position - 1] = marker
            return True
        return False

    def check_winner(self, marker):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6],            # Diagonals
        ]
        return any(all(self.board[i] == marker for i in combo) for combo in win_conditions)

    def is_draw(self):
        return all(s in ["X", "O"] for s in self.board)

    def available_moves(self):
        return (i+1 for i, val in enumerate(self.board) if val not in ["X", "O"])
