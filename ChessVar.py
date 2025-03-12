# Author: Michael Santora
# GitHub username: santoram
# Date: 11/26/2024
# Description: This is the portfolio project and final assignment for the class. Create Fog Of War Chess!
#    No checks, checkmates, castling, en passant, or pawn promotion
#    Create a class called ChessVar to implement
#    Each player can view their own pieces and opponents pieces are marked with an *
#    Opponent pieces become visible if within range of a legal attack
#    Must include an init method to initialize any data members
#    Include a method called get_game_state that could be either UNFINISHED', 'WHITE_WON', 'BLACK_WON'
#    A method called get_board that takes one parameter - a string indicating the perspective from which to display the
#        board and return the board (White returns the white players board, black returns the black chessboard, etc...)
#    Include a method called make_move that takes two params - strings that represents the square moved from and the
#        square moved two. If the game was already won,it should return false, otherwise it should update the board

class Player:
    """Creates a player"""

    def __init__(self, name, color, chessboard):
        """
        Creates a player object, initializes 4 data members
        Private Data members:
            - name: will be either player 1 or player 2
            - color: indicates the color a player object is playing
            - chessboard: a chessboard object that is unqiue to this player object
            - chess_collection: a dictionary containing either white or black chess piece objects
            """
        self._name = name
        self._color = color
        self._chessboard = chessboard
        self._chess_collection = {}

    def __str__(self):
        """returns a string representing a player object"""
        return f"This player object is {self.get_name()}, who is playing {self.get_color()}"

    def get_name(self):
        """returns the players name"""
        return self._name

    def get_color(self):
        """returns the color this player object is"""
        return self._color

    def get_chessboard_object(self):
        """returns the correct board this player object has"""
        return self._chessboard

    def add_to_collection(self, chess_object):
        """
        adds a specific chess piece to the collection
        takes a chess piece object as a parameter
        """
        self._chess_collection[chess_object.get_piece_name()] = chess_object

    def view_collection(self):
        """returns the full collection of chess pieces tied to a specific player object"""
        return self._chess_collection

    def get_chess_piece(self, location):
        """
        identifies where a specific chess piece object is on the players board
        takes location (not coordinates) as a parameter
        """
        for chess_item in self.view_collection():
            if self.view_collection()[chess_item].get_location() == location:
                return self.view_collection()[chess_item]

    def check_king(self):
        """confirms if a King has been captured by iterating through a specific players chessboard"""
        check_list = []
        for rank in self.get_chessboard_object().get_chessboard():
            for item in rank:
                check_list.append(item)
        if self.get_color() == "white" and "K" not in check_list:
            return False
        elif self.get_color() == "black" and "k" not in check_list:
            return False
        elif self.get_color() == "audience":
            pass
        else:
            return True

    def move_piece(self, start, end):
        """
        moves a specific chess piece object to the requested location on the board.
        this will only occur if the move is confirmed to be legal
        parameters: stop and end coordinates
        """
        # Grabs the correct piece object from the players collection
        piece_to_move = self.get_chess_piece(start)
        start_coor = self.get_chessboard_object().get_board_mapping()[start]
        end_coor = self.get_chessboard_object().get_board_mapping()[end]
        legality_check = piece_to_move.legality_check(start_coor, end_coor)
        if legality_check is True:
            return True
        else:
            return False


class Chessboard:
    """Creates a chessboard for Fog of War gameplay"""

    def __init__(self, board_color):
        """
        Creates a chessboard object, takes board_color as an argument
        Data members:
            - board: 3 versions: white view, black view, audience view
            - board_color: Black, White or audience
            - board_mapping: Provides x and y locations for each location on the chessboard
          """
        self._board = None
        self._board_color = board_color
        self._board_mapping = {
            'a8': [0, 0], 'b8': [0, 1], 'c8': [0, 2], 'd8': [0, 3], 'e8': [0, 4], 'f8': [0, 5], 'g8': [0, 6],
            'h8': [0, 7],
            'a7': [1, 0], 'b7': [1, 1], 'c7': [1, 2], 'd7': [1, 3], 'e7': [1, 4], 'f7': [1, 5], 'g7': [1, 6],
            'h7': [1, 7],
            'a6': [2, 0], 'b6': [2, 1], 'c6': [2, 2], 'd6': [2, 3], 'e6': [2, 4], 'f6': [2, 5], 'g6': [2, 6],
            'h6': [2, 7],
            'a5': [3, 0], 'b5': [3, 1], 'c5': [3, 2], 'd5': [3, 3], 'e5': [3, 4], 'f5': [3, 5], 'g5': [3, 6],
            'h5': [3, 7],
            'a4': [4, 0], 'b4': [4, 1], 'c4': [4, 2], 'd4': [4, 3], 'e4': [4, 4], 'f4': [4, 5], 'g4': [4, 6],
            'h4': [4, 7],
            'a3': [5, 0], 'b3': [5, 1], 'c3': [5, 2], 'd3': [5, 3], 'e3': [5, 4], 'f3': [5, 5], 'g3': [5, 6],
            'h3': [5, 7],
            'a2': [6, 0], 'b2': [6, 1], 'c2': [6, 2], 'd2': [6, 3], 'e2': [6, 4], 'f2': [6, 5], 'g2': [6, 6],
            'h2': [6, 7],
            'a1': [7, 0], 'b1': [7, 1], 'c1': [7, 2], 'd1': [7, 3], 'e1': [7, 4], 'f1': [7, 5], 'g1': [7, 6],
            'h1': [7, 7]
        }

    def __str__(self):
        """Returns a string to represent a chessboard object"""
        return f"This is a chessboard object. This specific board is {self.get_board_color()}"

    def get_board_color(self):
        """return the color of a specific board object"""
        return self._board_color

    def get_chessboard(self):
        """returns the correct chessboard tied to a specific player object"""
        return self._board

    def get_board_map_coord(self, location):
        """
        returns x and y location for requested spot
        takes location as a parameter
        """
        return self._board_mapping[location]

    def get_board_mapping(self):
        """returns the full mapping of the board"""
        return self._board_mapping

    def update_board(self, board_location, piece):
        """
        updates a spot on a specific chessboard
        takes location and (chess) piece as parameters
        """
        mod_loc = self._board_mapping[board_location]
        mod_y = mod_loc[0]
        mod_x = mod_loc[1]
        self._board[mod_y][mod_x] = piece

    def load_board(self):
        """sets the correct chessboard needed for a specific player object"""
        if self._board_color == "white":
            self._board = [
                ['*', '*', '*', '*', '*', '*', '*', '*'],
                ['*', '*', '*', '*', '*', '*', '*', '*'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
            ]

        elif self._board_color == "black":
            self._board = [
                ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['*', '*', '*', '*', '*', '*', '*', '*'],
                ['*', '*', '*', '*', '*', '*', '*', '*']
            ]

        elif self._board_color == "audience":
            self._board = [
                ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
            ]


class ChessPiece:
    """Creates a chess piece required to play the game"""

    def __init__(self, name, piece_type, player_obj, location):
        """
        Creates a chess piece object that is needed to play Fog of War
        Takes 4 parameters and initializes as private data members:
            - piece_name: Provides the name of the piece object
            - piece_type: provides the specific type of piece (p, k, q, etc...)
            - player_object: provides player object related to this piece object
            - location: where on the board the piece currently resides
        """
        self._piece_name = name
        self._piece_type = piece_type
        self._player_obj = player_obj
        self._location = location

    def __str__(self):
        """provides the type of chess piece this object is"""
        return f"This is a {self.get_piece_name()} object."

    def get_piece_name(self):
        """returns the name of this piece object"""
        return self._piece_name

    def get_piece_type(self):
        """returns the type of chess piece this object is"""
        return self._piece_type

    def get_player_obj(self):
        """returns which player collection this piece belongs to"""
        return self._player_obj

    def get_location(self):
        """reveals where the specific object is on the chessboard"""
        return self._location

    # leverage this to get coordinates
    def get_chessboard(self):
        """gets the correct chessboard related to this piece object"""
        chessboard = self.get_player_obj().get_chessboard_object().get_chessboard()
        return chessboard

    def set_location(self, new_location):
        """
        updates the current location for this specific chess piece
        takes location as parameter
        """
        self._location = new_location


class Pawn(ChessPiece):
    """Creates a Pawn piece used for the chess game"""

    def __init__(self, name, piece_type, player_obj, location, starting_location):
        """
        Creates a pawn object and inherits from the parent class
        Takes 2 additional parameters
        - starting_location: provides the starting position for a specific pawn object
        - first_move: confirms if a specific pawn object made its initial move
        """
        super().__init__(name, piece_type, player_obj, location)
        self._starting_location = starting_location
        self._first_move = True

    def set_first_move_made(self, status):
        """
        sets the move status from True to False or vice versa
        takes status as a parameter and can be set to either true or false"""
        if status is True or status is False:
            self._first_move = status
        return False

    def get_first_move_status(self):
        """
        confirms if a specific pawn object has made its initial move by returning the status
        if true the pawn has not made its first move
        """
        return self._first_move

    # starting and ending points are already in coordinate form
    def legality_check(self, starting, ending):
        """
        verifies if a proposed move is legal
        takes starting and ending locations as parameters
        """
        y1 = starting[0]
        y2 = ending[0]
        x1 = starting[1]
        x2 = ending[1]
        ver_mvt = y2 - y1
        hor_mvt = x2 - x1
        travel = [ver_mvt, hor_mvt]

        if self.get_player_obj().get_color() == "white":
            # white pawns can't move down the board / only upward (if you look from white being on the bottom)
            if ver_mvt >= 0:
                return False
            elif self.get_first_move_status() is False and ver_mvt <= -2:
                return False
            elif (self.get_first_move_status() is True and ver_mvt == -2 and hor_mvt == 0 and
                  self.get_chessboard()[y2][x2] == " "):
                return True
            elif (self.get_first_move_status() is True and ver_mvt == -1 and hor_mvt == 0 and
                  self.get_chessboard()[y2][x2] == " "):
                return True
            elif (self.get_first_move_status() is False and ver_mvt == -1 and hor_mvt == 0 and
                  self.get_chessboard()[y2][x2] == " "):
                return True
            elif travel == [-1, 1] and self.get_chessboard()[y2][x2] in ["p", "r", "n", "b", "q", "k", "*"]:
                return True
            elif travel == [-1, -1] and self.get_chessboard()[y2][x2] in ["p", "r", "n", "b", "q", "k", "*"]:
                return True
            else:
                return False

        elif self.get_player_obj().get_color() == "black":
            # black pawns can only move downward (if viewing where black is on top)
            if ver_mvt <= 0:
                return False
            elif self.get_first_move_status() is False and ver_mvt >= 2:
                return False
            elif (self.get_first_move_status() is True and ver_mvt == 2 and hor_mvt == 0 and
                  self.get_chessboard()[y2][x2] == " "):
                return True
            elif (self.get_first_move_status() is True and ver_mvt == 1 and hor_mvt == 0 and
                  self.get_chessboard()[y2][x2] == " "):
                return True
            elif (self.get_first_move_status() is False and ver_mvt == 1 and hor_mvt == 0 and
                  self.get_chessboard()[y2][x2] == " "):
                return True
            elif travel == [1, 1] and self.get_chessboard()[y2][x2] in ["P", "R", "N", "B", "Q", "K", "*"]:
                return True
            elif travel == [1, -1] and self.get_chessboard()[y2][x2] in ["P", "R", "N", "B", "Q", "K", "*"]:
                return True
            else:
                return False


class Rook(ChessPiece):
    """Creates a Rook piece used for the chess game"""

    def __init__(self, name, piece_type, player_obj, location):
        """
        Creates a Rook object and inherits from the parent class
        """
        super().__init__(name, piece_type, player_obj, location)

    def legality_check(self, starting, ending):
        """
        verifies if a proposed move is legal
        takes starting and ending locations as parameters
        """
        y1 = starting[0]
        y2 = ending[0]
        x1 = starting[1]
        x2 = ending[1]
        ver_mvt = y2 - y1
        hor_mvt = x2 - x1
        abs_ver_mvt = abs(y2 - y1)
        abs_hor_mvt = abs(x2 - x1)
        current_player_obj = self.get_player_obj().get_color()

        if abs_ver_mvt != 0 and abs_hor_mvt != 0:
            return False
        elif abs_ver_mvt == 0 and abs_hor_mvt == 0:
            return False
        # move up
        elif ver_mvt < 0 and hor_mvt == 0:
            for num in range(1, abs_ver_mvt):
                if y1 - num < 0:
                    return False
                elif self.get_chessboard()[y1 - num][x1] != " ":
                    return False
        # move down
        elif ver_mvt > 0 and hor_mvt == 0:
            for num in range(1, abs_ver_mvt):
                if y1 + num > 7:
                    return False
                elif self.get_chessboard()[y1 + num][x1] != " ":
                    return False
        # move left
        elif ver_mvt == 0 and hor_mvt < 0:
            for num in range(1, abs_hor_mvt):
                if x1 - num < 0:
                    return False
                elif self.get_chessboard()[y1][x1 - num] != " ":
                    return False
        # move right
        elif ver_mvt == 0 and hor_mvt > 0:
            for num in range(1, abs_hor_mvt):
                if x1 + num > 7:
                    return False
                elif self.get_chessboard()[y1][x1 + num] != " ":
                    return False

        if current_player_obj == "white" and self.get_chessboard()[y2][x2] in ["p", "r", "n", "b", "q", "k", "*", " "]:
            return True
        elif current_player_obj == "black" and self.get_chessboard()[y2][x2] in ["P", "R", "N", "B", "Q", "K", "*", " "]:
            return True
        else:
            return False


class Knight(ChessPiece):
    """Creates a Knight piece used for the chess game"""

    def __init__(self, name, piece_type, player_obj, location):
        """
        Creates a Knight object and inherits from the parent class
        """
        super().__init__(name, piece_type, player_obj, location)

    def legality_check(self, starting, ending):
        """
        verifies if a proposed move is legal
        takes starting and ending locations as parameters
        """
        y1 = starting[0]
        y2 = ending[0]
        x1 = starting[1]
        x2 = ending[1]
        ver_mov = abs(y2 - y1)
        hor_mov = abs(x2 - x1)
        abs_mov = [ver_mov, hor_mov]

        if (self.get_player_obj().get_color() == "white" and self.get_chessboard()[y2][x2] in
                ["p", "r", "n", "b", "q", "k", "*", " "]):
            if abs_mov == [1, 2] or abs_mov == [2, 1]:
                return True
            else:
                return False
        elif (self.get_player_obj().get_color() == "black" and self.get_chessboard()[y2][x2] in
              ["P", "R", "N", "B", "Q", "K", "*", " "]):
            if abs_mov == [1, 2] or abs_mov == [2, 1]:
                return True
            else:
                return False
        else:
            return False


class Bishop(ChessPiece):
    """Creates a Bishop piece used for the chess game"""

    def __init__(self, name, piece_type, player_obj, location):
        """
        Creates a Bishop object and inherits from the parent class
        """
        super().__init__(name, piece_type, player_obj, location)

    def legality_check(self, starting, ending):
        """
        verifies if a proposed move is legal
        takes starting and ending locations as parameters
        """
        y1 = starting[0]
        y2 = ending[0]
        x1 = starting[1]
        x2 = ending[1]
        ver_mvt = y2 - y1
        hor_mvt = x2 - x1
        abs_ver_mvt = abs(y2 - y1)
        abs_hor_mvt = abs(x2 - x1)
        current_player_obj = self.get_player_obj().get_color()

        if abs_ver_mvt != abs_hor_mvt:
            return False
        elif abs_ver_mvt == 0 and abs_hor_mvt == 0:
            return False
        # move up and to the left
        elif ver_mvt < 0 and hor_mvt < 0:
            for num in range(1, abs_ver_mvt):
                if y1 - num < 0:
                    return False
                elif self.get_chessboard()[y1 - num][x1 - num] != " ":
                    return False
        # move up and to the right
        elif ver_mvt < 0 and hor_mvt > 0:
            for num in range(1, abs_ver_mvt):
                if y1 - num < 0:
                    return False
                elif self.get_chessboard()[y1 - num][x1 + num] != " ":
                    return False
        # move down and to the left
        elif ver_mvt > 0 and hor_mvt < 0:
            for num in range(1, abs_hor_mvt):
                if y1 + num > 7:
                    return False
                elif self.get_chessboard()[y1 + num][x1 - num] != " ":
                    return False
        # move down and to the left
        elif ver_mvt > 0 and hor_mvt > 0:
            for num in range(1, abs_hor_mvt):
                if y1 + num > 7:
                    return False
                elif self.get_chessboard()[y1 + num][x1 + num] != " ":
                    return False

        if current_player_obj == "white" and self.get_chessboard()[y2][x2] in ["p", "r", "n", "b", "q", "k", "*", " "]:
            return True
        elif current_player_obj == "black" and self.get_chessboard()[y2][x2] in ["P", "R", "N", "B", "Q", "K", "*", " "]:
            return True
        else:
            return False


class Queen(ChessPiece):
    """Creates a Queen piece used for the chess game"""

    def __init__(self, name, piece_type, player_obj, location):
        """
        Creates a Queen object and inherits from the parent class
        """
        super().__init__(name, piece_type, player_obj, location)

    def legality_check(self, starting, ending):
        """
        verifies if a proposed move is legal
        takes starting and ending locations as parameters
        """
        y1 = starting[0]
        y2 = ending[0]
        x1 = starting[1]
        x2 = ending[1]
        ver_mvt = y2 - y1
        hor_mvt = x2 - x1
        abs_ver_mvt = abs(y2 - y1)
        abs_hor_mvt = abs(x2 - x1)
        current_player_obj = self.get_player_obj().get_color()

        if abs_ver_mvt == 0 and abs_hor_mvt == 0:
            return False
        # move up
        elif ver_mvt < 0 and hor_mvt == 0:
            for num in range(1, abs_ver_mvt):
                if y1 - num < 0:
                    return False
                elif self.get_chessboard()[y1 - num][x1] != " ":
                    return False
        # move down
        elif ver_mvt > 0 and hor_mvt == 0:
            for num in range(1, abs_ver_mvt):
                if y1 + num > 7:
                    return False
                elif self.get_chessboard()[y1 + num][x1] != " ":
                    return False
        # move left
        elif ver_mvt == 0 and hor_mvt < 0:
            for num in range(1, abs_hor_mvt):
                if x1 - num < 0:
                    return False
                elif self.get_chessboard()[y1][x1 - num] != " ":
                    return False
        # move right
        elif ver_mvt == 0 and hor_mvt > 0:
            for num in range(1, abs_hor_mvt):
                if x1 + num > 7:
                    return False
                elif self.get_chessboard()[y1][x1 + num] != " ":
                    return False
        # bishop style movement
        elif abs_ver_mvt != 0 and abs_hor_mvt != 0:
            if abs_ver_mvt != abs_hor_mvt:
                return False
            else:
                # move up and to the left
                if ver_mvt < 0 and hor_mvt < 0:
                    for num in range(1, abs_ver_mvt):
                        if y1 - num < 0:
                            return False
                        elif self.get_chessboard()[y1 - num][x1 - num] != " ":
                            return False
                # move up and to the right
                elif ver_mvt < 0 and hor_mvt > 0:
                    for num in range(1, abs_ver_mvt):
                        if y1 - num < 0:
                            return False
                        elif self.get_chessboard()[y1 - num][x1 + num] != " ":
                            return False
                # move down and to the left
                elif ver_mvt > 0 and hor_mvt < 0:
                    for num in range(1, abs_hor_mvt):
                        if y1 + num > 7:
                            return False
                        elif self.get_chessboard()[y1 + num][x1 - num] != " ":
                            return False
                # move down and to the left
                elif ver_mvt > 0 and hor_mvt > 0:
                    for num in range(1, abs_hor_mvt):
                        if y1 + num > 7:
                            return False
                        elif self.get_chessboard()[y1 + num][x1 + num] != " ":
                            return False

        if current_player_obj == "white" and self.get_chessboard()[y2][x2] in ["p", "r", "n", "b", "q", "k", "*", " "]:
            return True
        elif current_player_obj == "black" and self.get_chessboard()[y2][x2] in ["P", "R", "N", "B", "Q", "K", "*", " "]:
            return True
        else:
            return False

class King(ChessPiece):
    """Creates a King piece used for the chess game"""

    def __init__(self, name, piece_type, player_obj, location):
        """
        Creates a King object and inherits from the parent class
        """
        super().__init__(name, piece_type, player_obj, location)

    def legality_check(self, starting, ending):
        """
        verifies if a proposed move is legal
        takes starting and ending locations as parameters
        """
        y1 = starting[0]
        y2 = ending[0]
        x1 = starting[1]
        x2 = ending[1]
        ver_mov = abs(y2 - y1)
        hor_mov = abs(x2 - x1)
        abs_mov = [ver_mov, hor_mov]

        if ver_mov > 1 or hor_mov > 1:
            return False
        elif (self.get_player_obj().get_color() == "white" and self.get_chessboard()[y2][x2] in
                ["p", "r", "n", "b", "q", "k", "*", " "]):
            if abs_mov == [1, 0] or abs_mov == [0, 1] or abs_mov == [1, 1]:
                return True
            else:
                return False
        elif (self.get_player_obj().get_color() == "black" and self.get_chessboard()[y2][x2] in
              ["P", "R", "N", "B", "Q", "K", "*", " "]):
            if abs_mov == [1, 0] or abs_mov == [0, 1] or abs_mov == [1, 1]:
                return True
            else:
                return False
        else:
            return False


class ChessVar:
    """
    Creates an abstract board game based on a chess variant known as Fog of War
    """

    def __init__(self):
        """
        Creates a Fog of War game object and takes no parameters
        Private data members:
            - game_name: Fog of War
            - players: a collection of the player objects (does not include audience)
            - current_player: confirms which player object is the current player
            - opponent: confirms which player object is currently the opponent
            - game_state: can either be UNFINISHED, WHITE WON or BLACK WON
            - initial_setup: confirms if the game just started
            - default_player_boards: default chessboards for white, black and audience types
        """
        self._game_name = "Fog of War"
        self._players = {}
        self._current_player = None
        self._opponent = None
        self._game_state = "UNFINISHED"
        self._initial_setup = True
        self._default_player_boards = {
            "white": [
                ['*', '*', '*', '*', '*', '*', '*', '*'],
                ['*', '*', '*', '*', '*', '*', '*', '*'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
            ],
            "black": [
                ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['*', '*', '*', '*', '*', '*', '*', '*'],
                ['*', '*', '*', '*', '*', '*', '*', '*']],
            "audience": [
                ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        }

    def __str__(self):
        """Returns a string to represent the game object"""
        return f"This is a game object. This game is called {self.get_game_name()}"

    def get_game_name(self):
        """Returns the name of the game"""
        return f"You're playing {self._game_name}!"

    def get_player_obj(self, player_name):
        """
        Returns a specific player object
        Takes player name as parameter
        """
        return self._players[player_name]

    def add_player_obj(self, player_obj):
        """
        adds a player object to the collection
        take a specific player object as a parameter
        """
        self._players[player_obj.get_name()] = player_obj

    def get_player_collection(self):
        """returns the full collection of player objects"""
        return self._players

    def set_current_player(self, player_name):
        """
        sets the current player to the respective player object by taking a player object name
        can only be player 1 or player 2
        """
        if player_name == "player 1" or player_name == "player 2":
            self._current_player = self.get_player_collection()[player_name]
        else:
            return False

    def get_current_player(self):
        """returns the current player """
        return self._current_player

    def set_opponent(self, player_name):
        """
        sets the opposing player to the respective player object by taking a player object name
        can only be player 1 or player 2
        """
        if player_name == "player 1" or player_name == "player 2":
            self._opponent = self.get_player_collection()[player_name]
        else:
            return False

    def get_opponent(self):
        """returns the current opponent"""
        return self._opponent

    def get_game_state(self):
        """Returns the current state of the game"""
        return self._game_state

    def set_game_state(self, status):
        """
        Updates the status of the game
        Parameter: status
        """
        if status == "UNFINISHED" or status == "WHITE_WON" or status == "BLACK_WON":
            self._game_state = status
        else:
            return False

    def get_default_board(self, color):
        """
        returns the default mapping for a specific board color
        takes color as a parameter
        can either be black, white or audience
        """
        if color == "white" or color == "black" or color == "audience":
            return self._default_player_boards[color]
        else:
            return False

    def get_board(self, board_color):
        """
        Provides a specific version of a chessboard in its current state
        Takes board color as parameter
        """
        board = None

        if self.get_player_collection() != {}:
            if board_color == "white":
                board = self.get_player_collection()["player 1"].get_chessboard_object().get_chessboard()
            elif board_color == "black":
                board = self.get_player_collection()["player 2"].get_chessboard_object().get_chessboard()
            elif board_color == "audience":
                board = self.get_player_collection()["audience"].get_chessboard_object().get_chessboard()
        else:
            if board_color == "white":
                board = self.get_default_board("white")
            elif board_color == "black":
                board = self.get_default_board("black")
            elif board_color == "audience":
                board = self.get_default_board("audience")

        return board

    def get_initial_setup(self):
        """returns the initial setup status"""
        return self._initial_setup

    def set_initial_setup(self, status):
        """
        sets the initial setup status
        takes status as a parameter
        """
        if status is True or status is False:
            self._initial_setup = status
        else:
            return False

    def clear_fog_of_war(self):
        """make obvious any pieces that can be captured by either player 1 or player 2"""
        white_player_board = self.get_player_collection()["player 1"].get_chessboard_object().get_chessboard()
        black_player_board = self.get_player_collection()["player 2"].get_chessboard_object().get_chessboard()
        player_1_collections = []
        player_2_collections = []

        for piece in self.get_player_collection()["player 1"].view_collection():
            if self.get_player_collection()["player 1"].view_collection()[piece].get_location() != " ":
                player_1_collections.append(self.get_player_collection()["player 1"].view_collection()[piece].get_location())

        for piece in self.get_player_collection()["player 2"].view_collection():
            if self.get_player_collection()["player 2"].view_collection()[piece].get_location() != " ":
                player_2_collections.append(self.get_player_collection()["player 2"].view_collection()[piece].get_location())

        reveal_locations = []
        for item in player_1_collections:
            index = 0
            while index <= (len(player_2_collections) - 1):
                # checks to see if white piece can actually capture the black piece legally
                result = self.get_player_collection()["player 1"].move_piece(item, player_2_collections[index])
                end_coor = self.get_player_collection()["player 1"].get_chessboard_object().get_board_map_coord(player_2_collections[index])
                if result is True and white_player_board[end_coor[0]][end_coor[1]] != " ":
                    # add all the location spots white can capture to a list
                    spot_revealed = player_2_collections[index]
                    reveal_locations.append(spot_revealed)
                    # get the piece on the black chessboard that white is capturing
                    reveal = black_player_board[end_coor[0]][end_coor[1]]
                    # update white chessboard, white chess piece and black chess piece
                    self.get_player_collection()["player 1"].get_chessboard_object().update_board(player_2_collections[index], reveal)
                    index += 1
                elif result is False and player_2_collections[index] not in reveal_locations:
                    if white_player_board[end_coor[0]][end_coor[1]] in ["p", "r", "n", "b", "q", "k"]:
                        self.get_player_collection()["player 1"].get_chessboard_object().update_board(player_2_collections[index], "*")
                        index += 1
                    else:
                        index += 1
                else:
                    index += 1

        black_reveal_locations = []
        for item in player_2_collections:
            index = 0
            while index <= (len(player_2_collections) - 1):
                result = self.get_player_collection()["player 2"].move_piece(item, player_1_collections[index])
                end_coor = self.get_player_collection()["player 2"].get_chessboard_object().get_board_map_coord(player_1_collections[index])
                if result is True and white_player_board[end_coor[0]][end_coor[1]] != " ":
                    # add all the location spots black can capture to a list
                    spot_revealed = player_1_collections[index]
                    black_reveal_locations.append(spot_revealed)
                    # get the piece on the white chessboard that white is capturing
                    white_reveal = white_player_board[end_coor[0]][end_coor[1]]
                    # update black chessboard, black chess piece and white chess piece
                    self.get_player_collection()["player 2"].get_chessboard_object().update_board(player_1_collections[index], white_reveal)
                    index += 1
                elif result is False and player_1_collections[index] not in black_reveal_locations:
                    if black_player_board[end_coor[0]][end_coor[1]] in ["P", "R", "N", "B", "Q", "K"]:
                        self.get_player_collection()["player 2"].get_chessboard_object().update_board(player_1_collections[index], "*")
                        index += 1
                    else:
                        index += 1
                else:
                    index += 1

    def load_default_game_settings(self):
        """returns game to default settings"""
        self.set_game_state("UNFINISHED")

        # create chessboard
        white_chessboard = Chessboard("white")
        white_chessboard.load_board()
        black_chessboard = Chessboard("black")
        black_chessboard.load_board()
        audience_chessboard = Chessboard("audience")
        audience_chessboard.load_board()

        # create player objects (including audience) and add to collection
        player_1 = Player("player 1", "white", white_chessboard)
        player_2 = Player("player 2", "black", black_chessboard)
        audience = Player("audience", "audience", audience_chessboard)
        self.add_player_obj(player_1)
        self.set_current_player("player 1")
        self.add_player_obj(player_2)
        self.set_opponent("player 2")
        self.add_player_obj(audience)

        # create chess piece objects
        # BLACK CHESS PIECES
        a7_pawn = Pawn("pawn_1", "p", player_2, "a7", "a7")
        b7_pawn = Pawn("pawn_2", "p", player_2, "b7", "b7")
        c7_pawn = Pawn("pawn_3", "p", player_2, "c7", "c7")
        d7_pawn = Pawn("pawn_4", "p", player_2, "d7", "d7")
        e7_pawn = Pawn("pawn_5", "p", player_2, "e7", "e7")
        f7_pawn = Pawn("pawn_6", "p", player_2, "f7", "f7")
        g7_pawn = Pawn("pawn_7", "p", player_2, "g7", "g7")
        h7_pawn = Pawn("pawn_8", "p", player_2, "h7", "h7")
        a8_rook = Rook("rook_a8", "r", player_2, "a8")
        b8_knight = Knight("knight_b8", "n", player_2, "b8")
        c8_bishop = Bishop("bishop_c8", "b", player_2, "c8")
        d8_queen = Queen("queen_d8", "q", player_2, "d8")
        e8_king = King("king_e8", "k", player_2, "e8")
        f8_bishop = Bishop("bishop_f8", "b", player_2, "f8")
        g8_knight = Knight("knight_g8", "n", player_2, "g8")
        h8_rook = Rook("rook_h8", "r", player_2, "h8")

        black_collection = [a7_pawn, b7_pawn, c7_pawn, d7_pawn, e7_pawn, f7_pawn, g7_pawn, h7_pawn, a8_rook, b8_knight,
                            c8_bishop, d8_queen, e8_king, f8_bishop, g8_knight, h8_rook]
        for item in black_collection:
            player_2.add_to_collection(item)
        # WHITE CHESS Pieces
        a2_pawn = Pawn("pawn_9", "P", player_1, "a2", "a2")
        b2_pawn = Pawn("pawn_10", "P", player_1, "b2", "b2")
        c2_pawn = Pawn("pawn_11", "P", player_1, "c2", "c2")
        d2_pawn = Pawn("pawn_12", "P", player_1, "d2", "d2")
        e2_pawn = Pawn("pawn_13", "P", player_1, "e2", "e2")
        f2_pawn = Pawn("pawn_14", "P", player_1, "f2", "f2")
        g2_pawn = Pawn("pawn_15", "P", player_1, "g2", "g2")
        h2_pawn = Pawn("pawn_16", "P", player_1, "h2", "h2")
        a1_rook = Rook("rook_a1", "R", player_1, "a1")
        b1_knight = Knight("knight_b1", "N", player_1, "b1")
        c1_bishop = Bishop("bishop_c1", "B", player_1, "c1")
        d1_queen = Queen("queen_d1", "Q", player_1, "d1")
        e1_king = King("king_e1", "K", player_1, "e1")
        f1_bishop = Bishop("bishop_f1", "B", player_1, "f1")
        g1_knight = Knight("knight_g1", "N", player_1, "g1")
        h1_rook = Rook("rook_h1", "R", player_1, "h1")
        white_collection = [a2_pawn, b2_pawn, c2_pawn, d2_pawn, e2_pawn, f2_pawn, g2_pawn, h2_pawn, a1_rook, b1_knight,
                            c1_bishop, d1_queen, e1_king, f1_bishop, g1_knight, h1_rook]
        for item in white_collection:
            player_1.add_to_collection(item)

    def make_move(self, start, end):
        """
        moves a chess piece object if the move is legal
        parameters:
        - start: starting location on the board that has the piece a player is requesting to move
        - end: the location at which the specific chess piece object has been requested to move to
        """
        # loads the default game settings if applicable
        if self.get_initial_setup() is True:
            self.load_default_game_settings()
            self.set_initial_setup(False)
        else:
            pass

        # Check if both spots are on the board
        boundary_check = None
        board_map = self.get_current_player().get_chessboard_object().get_board_mapping()
        if start.lower() in board_map and end.lower() in board_map:
            boundary_check = True
        else:
            return False

        # get coordinates for start and stop locations for all the players pieces
        current_locations = []
        for piece in self.get_current_player().view_collection():
            current_locations.append(self.get_current_player().view_collection()[piece].get_location())

        if boundary_check is True:
            if start.lower() in current_locations:
                result = self.get_current_player().move_piece(start.lower(), end.lower())
                if result is True:
                    moving_piece = self.get_current_player().get_chess_piece(start.lower()).get_piece_type()
                    if moving_piece in ["P", "p"]:
                        self.get_current_player().get_chess_piece(start.lower()).set_first_move_made(False)
                    self.get_current_player().get_chessboard_object().update_board(end.lower(), moving_piece)
                    self.get_current_player().get_chessboard_object().update_board(start.lower(), " ")
                    self.get_opponent().get_chessboard_object().update_board(end.lower(), "*")
                    self.get_opponent().get_chessboard_object().update_board(start.lower(), " ")
                    self.get_player_collection()["audience"].get_chessboard_object().update_board(end.lower(),
                                                                                                  moving_piece)
                    self.get_player_collection()["audience"].get_chessboard_object().update_board(start.lower(), " ")
                    self.get_current_player().get_chess_piece(start.lower()).set_location(end.lower())

                    # clear the fog of war!
                    self.clear_fog_of_war()

                    # switch current player with opponent
                    if self.get_current_player().get_name() == "player 1":
                        self.set_current_player("player 2")
                        self.set_opponent("player 1")
                    elif self.get_current_player().get_name() == "player 2":
                        self.set_current_player("player 1")
                        self.set_opponent("player 2")
                    else:
                        pass

                    # check if a King was captured
                    white_result = None
                    black_result = None
                    for player in self.get_player_collection():
                        if self.get_player_collection()[player].get_color() == "white":
                            white_result = self.get_player_collection()[player].check_king()
                        elif self.get_player_collection()[player].get_color() == "black":
                            black_result = self.get_player_collection()[player].check_king()
                    if white_result is False:
                        self.set_game_state("BLACK_WON")
                        self.set_initial_setup(True)
                        return self.get_game_state()
                    elif black_result is False:
                        self.set_game_state("WHITE_WON")
                        self.set_initial_setup(True)
                        return self.get_game_state()
                    else:
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False


def main():
    """Runs the program as a script"""
    # game = ChessVar()
    # print(game.make_move('d2', 'd4'))
    # print(game.make_move('g7', 'g5'))
    # print(game.make_move('c1', 'g5'))
    # print(game.make_move('e7', 'e6'))
    # print(game.make_move('g5', 'd8'))
    # print(game.make_move('f8', 'c5'))
    # print(game.make_move('b1', 'c3'))
    # print(game.make_move('g8', 'F6'))
    # print(game.make_move('a1', 'c1'))
    # print(game.make_move('b7', 'b5'))
    # print(game.make_move('D1', 'd3'))
    # print(game.make_move('b5', 'b4'))
    # print(game.make_move('c3', 'e4'))
    # print(game.make_move('f6', 'e4'))
    # print(game.make_move('f2', 'f4'))
    # print(game.make_move('h8', 'f8'))
    # print(game.make_move('c2', 'c3'))
    # print(game.make_move('b4', 'c3'))
    # print(game.make_move('b2', 'c3'))
    # print(game.make_move('e8', 'e7'))
    # print(game.make_move('d8', 'e7'))
    # for row in game.get_board("audience"):
    #     print(row)
    # print("")
    # for row in game.get_board("white"):
    #     print(row)
    # print("")
    # for row in game.get_board("black"):
    #     print(row)
    # print("")


if __name__ == '__main__':
    main()
