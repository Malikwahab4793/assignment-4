# class TicTacToe:
#     def __init__ (self):
#         self.board = [' ' for __ in range(9)] #we will use a single list ro rep 3x3 board
#         self.current = None #keep track for Winner!

#     def print_board(self):
#         for raw in [self.board[i*3:(i+1)*3] for i in range (3)]:
#             print('| ' +' | '.join(raw) + ' |')

#     @staticmethod

#     def print_board_nums():
#         # 0 | 1 |2 etc (tell us what number corresponds to what box)
#         number_board = [[str(i) for i in range (j*3) for j in range (3)]]
#         for raw in number_board:
#             print ('| ' +' | '.join(raw) + ' |')
        
#     def available_move(self):
#         return [i for i, spot in enumerate(self.board) if self == ' ' ]
    
#     def empty_squares(self):
#         return ' ' in self.board
    
#     def num_empty_squares(self):
#         return self.board.count(' ')
    
#     def make_move(self, square, letter):


#         if self.board[square] == ' ':
#             self.board[square] =  letter
#             if self.winner(square, letter):
#                 self.current_winner = letter
#             return True
#         return False
    
#     def winner(self, square, letter):


#         raw_ind = square //3
#         raw= self.board[raw_ind*3: (raw_ind +1) *3]
#         if all ([spot == letter] for spot in raw):
    

#         #  moves = []
#         # for (i, spot) in enumerate(self.board):
#         #     #['x', 'x', 'o']-->[(0, 'x'), (1, 'x'), (2, 'o')]
#         #     if spot == ' ':
#         #         moves.append(i)

# def play(game, x_player, o_player, print_game= True):
#     if print_game:
#         game.print_board_nums()

#     letter='x'

#     while game.empty_squares():
#         if letter == '0':
#             squares = o_player.get_move(game)
#         else:
#             squares = x_player.get_move(game)
#         if game.make_move(squares, letter ):
#             if print_game:
#                 print(letter + f'make a move to square {squares}')
#                 game.print_board()
#                 print(' ')
#             if game.current_winner:
#                 if print_game:
#                     print(letter + 'wins')
#                     return letter
#             if print_game:
#                 print('It\'s tie!')




import math
import time
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'
        time.sleep(0.8)

    if print_game:
        print("It's a tie!")
