from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():
    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2

    def num_pieces(self):
        color = self.opponent[self.color]
        if color == 1:
            color = 'B'
            openent_pieces = self.board.black_count
        elif color == 2:
            color = 'W'
            openent_pieces = self.board.white_count
        return openent_pieces

    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        openent_pieces = self.num_pieces()
        for i,checker in enumerate(moves):
            for j,move in enumerate(moves[i]):
                self.board.make_move(moves[i][j], self.color) #Make move
                temp = self.num_pieces()
                if temp < openent_pieces: # check if move took openent piece
                    openent_pieces = temp
                    best = (i,j)
                else:
                    best = (0,0)
                self.board.undo()
        self.board.make_move(moves[best[0]][best[1]],self.color)

'''
    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        move = moves[index][inner_index]
        self.board.make_move(move,self.color)
        return move
'''
