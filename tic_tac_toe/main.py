from game.board import Board
from game.players import Player
from tools.display import print_welcome, print_board, print_winner, prompt_move, ask_restart
from tools.logger import Logger

def main():
    print_welcome()
    name1 = input("Please enter Player 1 name: ")
    name2 = input("Please enter Player 2 name: ")

    player1 = Player(name1, "X")
    player2 = Player(name2, "O")
    board = Board()
    logger = Logger(player1, player2)

    current_player = player1

    while True:
        print_board(board)
        move = current_player.get_move(board)
        if board.place_move(move, current_player.marker):
            logger.log_move(current_player, move, board)
            if board.check_winner(current_player.marker):
                print_board(board)
                print_winner(current_player)
                logger.log_result(f"{current_player.name} wins!")
                break
            elif board.is_draw():
                print_board(board)
                print("It's a draw!")
                logger.log_result("Draw")
                break
            current_player = player2 if current_player == player1 else player1

    if ask_restart():
        main()

if __name__ == "__main__":
    main()

# game/board.py
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
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6],
        ]
        return any(all(self.board[i] == marker for i in combo) for combo in win_conditions)

    def is_draw(self):
        return all(s in ["X", "O"] for s in self.board)

    def available_moves(self):
        return (i+1 for i, val in enumerate(self.board) if val not in ["X", "O"])
