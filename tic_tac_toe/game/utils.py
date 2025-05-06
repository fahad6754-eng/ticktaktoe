def validate_move(move, board):
    return move in board.available_moves()

def clean_input(user_input):
    try:
        return int(user_input)
    except ValueError:
        return None