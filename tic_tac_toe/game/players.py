import random

class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def get_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name}'s Turn ({self.marker}): Enter position (1-9): "))
                if move in board.available_moves():
                    return move
                print("Invalid or taken position. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")
