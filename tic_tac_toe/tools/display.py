def print_welcome():
    print("Welcome to Tic-Tac-Toe!")

def print_board(board):
    display = board.display()
    for row in display:
        print(" | ".join(row))
        if row != display[-1]:
            print("-" * 9)

def print_winner(player):
    print(f"Congratulations, {player.name}! You win!")

def prompt_move(player):
    return input(f"{player.name}'s Turn ({player.marker}): Enter a position (1-9): ")

def ask_restart():
    return input("Would you like to play again? (yes/no): ").lower().startswith('y')
