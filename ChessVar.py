class Player:
    """
    A class to represent a player in the atomic chess game. Player have their name and colo (white or black).
    """

    def __init__(self, name, color):
        """
        Constructor for Player class. Takes the name and color as the parameter
        The name can be any name.
        The color options are either White or Black.
        All data members are private
        """
        self._name = name
        self._color = color

    def get_name(self):
        """
        Returns the name of the player.
        """
        return self._name

    def get_color(self):
        """
        Returns the color the player has chosen.
        """
        return self._color


class Piece:
    """
    Piece class represents the different types of pieces in chess and how each type of pieces move
    """

    def __init__(self, color_type, position):
        """
        Initialize a piece with the color white or black.
        """
        self._color_type = color_type
        self._position = position

    def get_color_type(self):
        return self._color_type

    def update_new_position(self, new_pos):
        self._position = new_pos


class Pawn(Piece):
    """
    Inherits the Piece class to get the moves of the pawn piece.
    """

    def __init__(self, color_type, position):
        super().__init__(color_type, position)

    def get_moves(self, position, board):
        """
        Gets the possible moves of the pawn based on the position.
        Board is a parameter to track movement
        """
        row, col = position
        color = self._color_type[0]
        moves = []

        if color == "W":
            steps = -1
        else:
            steps = 1

        dg_left = board[row + steps][col - 1]
        dg_right = board[row + steps][col + 1]

        if board[row + steps][col] == ' ':
            moves.append((row + steps, col))
            if row == 6 and board[row + 2 * steps][col] == ' ':
                moves.append((row + 2 * steps, col))
            if row == 1 and board[row + 2 * steps][col] == ' ':
                moves.append((row + 2 * steps, col))
        if col > 0 and dg_left != ' ' and dg_left.get_color_type()[0] != color:
            moves.append((row + steps, col - 1))
        if col < 7 and dg_right != ' ' and dg_right.get_color_type()[0] != color:
            moves.append((row + steps, col + 1))

        return moves


class Rook(Piece):
    """
    Inherits the Piece class to get the moves of the rook piece.
    """

    def __init__(self, color_type, position):
        super().__init__(color_type, position)

    def get_moves(self, position, board):
        """
        Gets the possible moves of the Rook based on the position
        """
        row, col = position
        color = self.get_color_type()[0]
        moves = []

        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in steps:
            for j in range(1, 8):
                new_row = row + i[0] * j
                new_col = col + i[1] * j

                if 0 <= new_row < 8 and 0 <= new_col < 8: # Sets to the board's bounds
                    piece = board[new_row][new_col]
                    if piece == ' ':
                        moves.append((new_row, new_col))
                    elif piece.get_color_type()[0] != color:  # check if piece is an enemy
                        moves.append((new_row, new_col))
                        break
                    else:  # Checks for friendly
                        break
                else:  # Check for out of bounds
                    break
        return moves


class Knight(Piece):
    """
    Inherits the Piece class to get the moves of the Knight piece.
    """

    def __init__(self, color_type, position):
        super().__init__(color_type, position)

    def get_moves(self, position, board):
        """
        Gets the possible moves of the Knight based on the position
        """
        row, col = position
        color = self.get_color_type()[0]
        moves = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for m, n in knight_moves:
            new_row, new_col = row + m, col + n
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board[new_row][new_col]
                if piece == ' ':
                    moves.append((new_row, new_col))
                elif piece.get_color_type()[0] != color:
                    moves.append((new_row, new_col))
        return moves


class Bishop(Piece):
    """
    Inherits the Piece class to get the moves of the Bishop piece.
    """

    def __init__(self, color_type, position):
        super().__init__(color_type, position)

    def get_moves(self, position, board):
        """
        Gets the possible moves of the Bishop based on the position. Similar technique from the Rook piece.
        The bishop is like a linear slope.
        """
        row, col = position
        color = self.get_color_type()[0]
        moves = []

        steps = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for i in steps:
            for j in range(1, 8):
                new_row = row + i[0] * j
                new_col = col + i[1] * j

                if 0 <= new_row < 8 and 0 <= new_col < 8:  # sets the limits to the bounds of the board
                    piece = board[new_row][new_col]
                    if piece == ' ':
                        moves.append((new_row, new_col))
                    elif piece.get_color_type()[0] != color:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break

        return moves


class Queen(Piece):
    """
    Inherits the Piece class to get the moves of the Queen piece
    """

    def __init__(self, color_type, position):
        super().__init__(color_type, position)

    def get_moves(self, position, board):
        """
        Gets the possible moves of the Queen based on the position
        """
        moves = []

        moves.extend(Rook(self._color_type, position).get_moves(position, board))
        moves.extend(Bishop(self._color_type, position).get_moves(position, board))

        return moves


class King(Piece):
    """
    Inherits the Piece class to get the moves of the King piece.
    """

    def __init__(self, color_type, position):
        super().__init__(color_type, position)

    def get_moves(self, position, board):
        """
        Gets the possible moves of the King based on the position
        """
        row, col = position
        color = self.get_color_type()[0]
        moves = []
        steps = [
            (1, 0), (1, 1), (1, -1),
            (0, 1), (0, -1),
            (-1, 0), (-1, 1), (-1, -1),

        ]
        for m, n in steps:
            new_row, new_col = row + m, col + n
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] == ' ' or board[new_row][new_col].get_color_type()[0] != color:
                    moves.append((new_row, new_col))
        return moves


class ChessVar:
    """
    The ChessCar class to represent the atomic chess game. 2-player game where white starts first.
    Uses the Player class for the player data and the Piece class for the possible moves.
    """

    def __init__(self):
        """
        Constructor for ChessVar Class.
        Takes no parameters.
        Initializes the board and places initial pieces in correct positions.
        All data members are private.
        I could use this for the visual board.
        """
        self._board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]

        self._board[0][0] = Rook('BR', (0, 0))
        self._board[0][1] = Knight('BN', (0, 1))
        self._board[0][2] = Bishop('BB', (0, 2))
        self._board[0][3] = Queen('BQ', (0, 3))
        self._board[0][4] = King('BK', (0, 4))
        self._board[0][5] = Bishop('BB', (0, 5))
        self._board[0][6] = Knight('BN', (0, 6))
        self._board[0][7] = Rook('BR', (0, 7))
        for i in range(8):
            self._board[1][i] = Pawn('BP', (1, i))

        self._board[7][0] = Rook('WR', (7, 0))
        self._board[7][1] = Knight('WN', (7, 1))
        self._board[7][2] = Bishop('WB', (7, 2))
        self._board[7][3] = Queen('WQ', (7, 3))
        self._board[7][4] = King('WK', (7, 4))
        self._board[7][5] = Bishop('WB', (7, 5))
        self._board[7][6] = Knight('WN', (7, 6))
        self._board[7][7] = Rook('WR', (7, 7))
        for i in range(8):
            self._board[6][i] = Pawn('WP', (6, i))

        self._player = {}
        self._game_state = 'UNFINISHED'
        self._current_turn = 'White'

    def create_player(self, player_name, color):
        """
        Creates a player instance and stores it in the players dictionary
        """
        self._player.update({color: Player(player_name, color)})

    def get_board(self):
        return self._board

    def print_board(self):
        """
        Print the current state of the board.
        """
        pieces = {
            'BR': '[♖]', 'BN': '[♘]', 'BB': '[♗]', 'BQ': '[♕]', 'BK': '[♔]', 'BP': '[♙]',
            'WR': '[♜]', 'WN': '[♞]', 'WB': '[♝]', 'WQ': '[♛]', 'WK': '[♚]', 'WP': '[♟]',
            ' ': '[ ]'
        }
        print(" -----| " + self._current_turn + "'s Turn |-----")
        print("__|_A__B__C__D__E__F__G__H_")
        for i in range(8):
            print("{0} |".format(8 - i), end='')
            for j in range(8):
                piece = self._board[i][j]
                if piece == ' ':
                    print('[ ]', end='')
                else:
                    print(pieces[piece.get_color_type()], end='')
                if i == 3 and j == 7:
                    print("                   example of correct input 'b2 b4'", end='')
                if i == 4 and j == 7:
                    print("                             Type 'quit' to forfeit", end='')
                if i == 5 and j == 7:
                    print("                                 Made By Calvin Lee", end='')
            print()
        print("__|_A__B__C__D__E__F__G__H_")
        print("GAME STATUS: " + self._game_state)

    def get_game_state(self):
        """
        Gets the current state of the game that returns 'UNFINISHED', 'WHITE_WON', 'BLACK_WON'
        """
        return self._game_state

    def get_current_turn(self):
        return self._current_turn

    def switch_turn(self):
        """
        Switches the current player
        """

        if self._current_turn == 'White':
            self._current_turn = "Black"
        elif self._current_turn == 'Black':
            self._current_turn = "White"

    def update_game_state(self):
        """
        Update the game state by checking if a king has been captured.
        """
        kings = []
        for n in self._board:
            for m in n:
                if m != ' ' and m.get_color_type()[1] == 'K':
                    kings.append(m.get_color_type())

        if 'WK' not in kings:
            self._game_state = 'BLACK_WON'
        elif 'BK' not in kings:
            self._game_state = "WHITE_WON"

    def letters_to_num(self, position):
        """
        converts the letter coordinate to mxn numbers
        """

        row_dict = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
        col_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        row = row_dict[position[1]]
        col = col_dict[position[0]]
        return (row, col)

    def make_move(self, position, destination):
        """
        Takes the current position and the destination as the parameters to move the piece.
        The current position will be used to determine the color of the piece and the type of piece.
        Calls the is_valid_move method to check if the move is valid.
        The get_moves fromt the pieces already hecks whether it is friendly.
        """
        row = destination[0]
        col = destination[1]
        aoe = []

        piece = self._board[position[0]][position[1]]
        if piece != ' ' and piece.get_color_type()[0] != self._current_turn[0]:
            return 'Wrong turn'
        elif piece != ' ' and destination in piece.get_moves(position, self._board):
            temp = self._board[row][col]
            self._board[row][col] = piece
            self._board[position[0]][position[1]] = ' '
            piece.update_new_position(destination)
            if temp != ' ':
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        aoe.append((row + i, col + j))
                for n in aoe:
                    if 0 <= n[0] <= 7 and 0 <= n[1] <= 7:
                        self._board[n[0]][n[1]] = ' '
        else:
            return "IllEGAL MOVE"

    def run(self):
        """
        Main method to run the chess game.
        """
        print("Welcome to Atomic Chess! BOOM!")
        print("Capture the enemy's king to win!")
        print("Made by Calvin Lee\n")
        print("!!! Please play this on dark mode for the correct chess colors !!!\n")
        x = input("Start Game (Y/N): ")
        if x.upper() == 'N':
            print("please play :(")
            return
        elif x.upper() != 'Y':
            print('Invalid input')
            return

        while self.get_game_state() == 'UNFINISHED':
            print('\n\n\n\n')
            self.print_board()
            move = input(f"{self.get_current_turn()}'s Turn: ")
            if move.lower() == 'quit':
                if self.get_current_turn() == 'White':
                    self._game_state = 'BLACK_WON'
                else:
                    self._game_state = 'WHITE_WON'
                break
            try:
                position, destination = move.split()
                pos = self.letters_to_num(position.lower())
                dest = self.letters_to_num(destination.lower())
                if self.make_move(pos, dest) == "IllEGAL MOVE":
                    print("\n\n\n! Illegal Move. Please follows the rules of chess !")
                elif self.make_move(pos, dest) != "Wrong turn":
                    print("Not your turn")
                    self.update_game_state()
                    if self.get_game_state() == 'UNFINISHED':
                        self.switch_turn()
            except ValueError:
                print("Invalid input. Example of correct input: 'b2 b4'.")
            except Exception:
                print(f"ERROR: {Exception}")

        print('\n\n\n\n')
        self.print_board()
        print(f"Game Over: {self.get_game_state()}")


if __name__ == '__main__':
    game = ChessVar()
    game.run()
