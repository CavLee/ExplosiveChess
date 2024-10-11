# Atomic Chess Variant - `ChessVar` Class

This project implements a Python class, `ChessVar`, designed to simulate a variant of chess called **Atomic Chess**. While the game begins with standard chess rules, it introduces explosive new mechanics when pieces are captured. The `ChessVar` class encapsulates these unique rules, providing an interactive and strategic gameplay experience.

## Features:
- **Standard Chess Setup**: The game uses the normal chess starting position, with white moving first. Piece movements follow standard chess rules, but there is no castling, en passant, or pawn promotion.
- **Explosive Captures**: In Atomic Chess, capturing a piece causes an "explosion" in the 8 surrounding squares, removing all pieces except pawns. Even the capturing piece is destroyed in this explosion.
- **King Rules**: Kings cannot capture other pieces and are immune to the explosion radius unless directly captured. Moves that would simultaneously blow up both kings are not allowed.
- **Game End**: The game concludes if a player's king is captured or blown up. The game ends with a win for the opposing player.

## Class Methods:
- `__init__()`: Initializes the game board, player turns, and other required variables.
- `get_game_state()`: Returns the current game state as `'UNFINISHED'`, `'WHITE_WON'`, or `'BLACK_WON'`.
- `make_move(from_square, to_square)`: Processes a player's move. It validates the move, handles piece capture and explosions, updates the board, adjusts the game state if necessary, and returns `True` for valid moves or `False` otherwise.

## Purpose:
The `ChessVar` class offers a creative spin on traditional chess, blending familiar gameplay mechanics with the chaotic, strategic nature of Atomic Chess. This project demonstrates skills in object-oriented programming, state management, and implementing custom game rules.

Explore this class to experience the thrill of explosive chess tactics!

