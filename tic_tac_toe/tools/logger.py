from pathlib import Path

class Logger:
    def __init__(self, player1, player2):
        self.log_dir = Path("tic_tac_toe/game_log")
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.game_number = self._get_next_game_number()
        self.current_log_path = self.log_dir / f"game{self.game_number}"
        self.current_log_path.mkdir()
        self.log_file = self.current_log_path / "log.txt"
        self.move_count = 0
        self._init_log(player1, player2)

    def _get_next_game_number(self):
        existing = [int(p.name[4:]) for p in self.log_dir.glob("game*/") if p.name[4:].isdigit()]
        return max(existing, default=0) + 1

    def _init_log(self, p1, p2):
        with self.log_file.open("w") as f:
            f.write(f"Game {self.game_number} Log\n")
            f.write(f"Players:\n- {p1.name} ({p1.marker})\n- {p2.name} ({p2.marker})\n")
            f.write(f"First move: {p1.name}\n\nMoves:\n")

    def log_move(self, player, position, board):
        self.move_count += 1
        with self.log_file.open("a") as f:
            f.write(f"Move {self.move_count}: {player.name} -> Position {position}\n")
            rows = board.display()
            for row in rows:
                f.write(" | ".join(row) + "\n")
            f.write("-" * 9 + "\n")

    def log_result(self, result):
        with self.log_file.open("a") as f:
            f.write(f"Result: {result}\n")
