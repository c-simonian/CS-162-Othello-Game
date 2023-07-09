# Author: Christian Simonian
# GitHUb Username: c-simonian
# Date: 06/08/2023
# Description: Contains a player class which contains a player object. The class contains two get methods such as get_color
               #and get_name. The Othello class contains information about the players and the board. Containing methods
               #such as print_board, return_winner, return_available_position, make_move, and play_game. The Othello class
               #is where most of the operations are done for the game.
class Player:
    """A class that represents a player in the game. Contains the players name and the piece
    color either being black or white"""

    def __init__(self, name, color):
        """The constructor for the player Class."""
        self._name = name
        self._color = color

    def get_color(self):
        """Returns the color of the player"""
        return self._color

    def get_name(self):
        """Returns the player name"""
        return self._name


class Othello:
    """A class that represents the game as played. Containing information about the players and the board.
            Containing methods such as print_board, return_winner, return_available_position, make_move, and play_game"""

    def __init__(self):
        self._list_of_players = []
        # self._board = [
        #     ['O' if row == 3 and col == 3 else 'O' if row == 4 and col == 4 else 'X' if row == 3 and col == 4 else
        #     'X' if row == 4 and col == 3 else '.' for col in range(8)] for row in range(8)]
        self._board = [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
            ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
            ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
            ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
            ['*', '.', '.', '.', 'X', 'O', '.', '.', '.', '*'],
            ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
            ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
            ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
            ]

    def get_list_of_players(self):
        """returns the list of players"""
        return self._list_of_players

    # def print_board(self):
    #     row = ['*' for boarder in range(8)]
    #     top = list(row)
    #     bottom = list(row)
    #     border = '*'
    #     print(' '.join(top))
    #     for index in range(8):
    #         print(border + ' ' + ' '.join(self._board[index]) + ' ' + border)
    #     print(' '.join(bottom))

    def print_board(self):
        """prints the game board"""
        for index in range(10):
            print(' '.join(self._board[index]) + ' ')

    def create_player(self, player_name, color):
        """creates a new player object, it takes in the player_name and color as parameters.
        Adds the player object to the list_of_players"""
        self._list_of_players.append(Player(player_name, color))

    def return_winner(self):
        """Will be called by the play_game function if the game is over.
        Takes in no parameters. Returns the color of the winner a long with the players name. Will return it's a tie
        if white and black have the same number of pieces on the board when the game is determined to be finished."""
        white_count = 0
        black_count = 0
        for row_index in range(len(self._board)):
            for col_index in range(len(self._board[0])):
                if self._board[row_index][col_index] == 'O':
                    white_count += 1
                if self._board[row_index][col_index] == 'X':
                    black_count += 1
        if black_count > white_count:
            for obj in self._list_of_players:
                if str(obj.get_color()) == 'black':
                    return f'Winner is black player:{obj.get_name()}'
        if white_count > black_count:
            for obj in self._list_of_players:
                if str(obj.get_color()) == 'white':
                    return f'Winner is white player:{obj.get_name()}'
        else:
            return "It's a tie"

    def return_available_positions(self, color):
        """returns the available positions for the certain color passed as a parameter
        an available position will be defined a legal move in which the certain player can make"""
        color_to_char = {'black': 'X', 'white': 'O'}
        # directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        possible_positions = []
        visited_positions = []
        # for row_index, sub_list in enumerate(self._board):
        #     for col_index, item in enumerate(sub_list):
        if color.lower() == 'black':
            opponent_color_val = 'O'
        if color.lower() == 'white':
            opponent_color_val = 'X'
        for row_index in range(len(self._board)):
            for col_index in range(len(self._board[0])):
                if self._board[row_index][col_index] == color_to_char[color]:
                    for sub_row, sub_col in directions:
                        if self._board[row_index + sub_row][col_index + sub_col] == opponent_color_val and (row_index + sub_row, col_index + sub_col) not in visited_positions: # this needs to be opposite of whatever color is passed in
                            visited_positions.append((row_index + sub_row, col_index + sub_col))
                            # print(opponent_color_val)
                            opponent_row_index, opponent_col_index = row_index + sub_row, col_index + sub_col
                            for s_row, s_col in directions:
                                if self._board[opponent_row_index + s_row][opponent_col_index + s_col] == '.' and (
                                    opponent_row_index + s_row,opponent_col_index + s_col) not in possible_positions and self._board[opponent_row_index - s_row][opponent_col_index - s_col] == color_to_char[color]:
                                        possible_positions.append((opponent_row_index + s_row, opponent_col_index + s_col))
        return sorted(possible_positions)

    def make_move(self, color, piece_position):
        """takes in the color and piece_position as parameters. It will move the specified color to the
        specified positions. This will be called by the play_game function"""
        for column, row in enumerate(self._board):
            directions = [(1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
            row = piece_position[0]
            col = piece_position[1]
            if color.lower() == 'white':
                self._board[row][col] = "O"
                for sub_row, sub_col in directions:
                    if self._board[row + sub_row][col + sub_col] == 'X':
                        self._board[row + sub_row][col + sub_col] = 'O'
            if color.lower() == 'black':
                self._board[row][col] = "X"
                for sub_row, sub_col in directions:
                    if self._board[row + sub_row][col + sub_col] == 'O':
                        self._board[row + sub_row][col + sub_col] = 'X'

        self.print_board()   #comment out when submit
        return self._board

    def play_game(self, player_color, piece_position):
        """takes in the player_color and piece_position as parameters. It will verify
        for the specified players color if the piece_position is a valid move. If it is
        not it will display the valid moves and return invalid move. If the position is valid
        it will call the make_move function. If the game has been indicated as over due to no more
        empty spaces left it print count for each color and will call the return_winner function"""
        invalid_move = 'Invalid move'
        valid_pos_list = self.return_available_positions(player_color)
        black_count = 0
        white_count = 0
        if piece_position not in valid_pos_list:
            print(f"Here are the valid moves: {valid_pos_list}")
            return invalid_move
        if piece_position in valid_pos_list:
            self.make_move(player_color, piece_position)
            for row_index in range(len(self._board)):
                for col_index in range(len(self._board[0])):
                    if self._board[row_index][col_index] == 'X':
                        black_count += 1
                    if self._board[row_index][col_index] == 'O':
                        white_count += 1
                    if self._board[row_index][col_index] == '.':
                        return
            return f"Game is ended white piece:{white_count} black piece:{black_count}"




#
game = Othello()
game.create_player("Helen", "white")
game.create_player("Leo", "black")
print(game.return_available_positions('black'))
game.play_game("black", (6, 5))
# print(game.return_available_positions('white'))
game.play_game("white", (6, 6))
print(game.return_available_positions('black'))
# game.play_game("black", (1,6))
# print(game.return_available_positions('white'))
# game.play_game("white", (7, 5))

# print(game.return_winner())
# game.print_board()
# game.make_move('white', (1,1))


# avail_pos_black = [(2, 3), (3, 2), (4, 5), (5, 4)]
# avail_pos_white = [(5, 3), (3, 5), (4, 2), (2, 4)]
# playgame
# call available positions:
# check if piece position in that

# t_1 = Othello()
#
# t_1 = Othello()
# t_1.print_board()
#
# t_1.create_player('bob', 'black')
# t_1.create_player('andrew', 'white')
# # print(t_1.get_list_of_players())
#
# print(t_1.return_available_positions('black'))
# print(t_1.play_game('black', (6,5)))
# print(t_1.return_available_positions('white'))
# print(t_1.play_game('white', (4,6)))
# print(t_1.return_available_positions('black'))
# print(t_1._board)
# print(t_1.play_game('black', (2,1)))
# print(t_1.return_available_positions('white'))
# print(t_1.play_game('white', (4,4)))

# print(t_1.return_winner())





