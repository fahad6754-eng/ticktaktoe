
## ✅ Features

- Turn-based two-player gameplay
- Validates moves and tracks win/draw conditions
- Game history logging to uniquely named folders (e.g., `game1`, `game2`)
- Clear modular design using OOP and separation of concerns
- Uses `pathlib` for all directory and file operations

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/fahad6754-eng/ticktaktoe.git
   cd tic_tac_toe

2. Run the game:

   python main.py

📝 Logging
Each game session creates a new directory under game_log/ (e.g., game1, game2, ...) and logs:

Player details

All moves with positions

Board state after each move

Final result (win or draw)

#🛠️ Requirements
Python 3.7 or higher (standard libraries only)

#📚 Concepts Used
Object-Oriented Programming (OOP)

Modular Design

pathlib for file/directory management

Logging and text file manipulation

Generators for dynamic move availability

📩 License
This project is open-source and available under the MIT License.
