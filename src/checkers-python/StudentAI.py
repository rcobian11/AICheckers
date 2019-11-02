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

    def num_pieces(self, color):
        if color == 1:
            openent_pieces = self.board.black_count
        elif color == 2:
            openent_pieces = self.board.white_count
        return openent_pieces

    def get_move(self,move):
        opp_color = self.opponent[self.color]
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves1 = self.board.get_all_possible_moves(self.color) #all our first moves
        our_pieces = self.num_pieces(self.color) # our pieces before our move
        max = -(self.num_pieces(self.color))
        for i,checker in enumerate(moves1):
            for j,move in enumerate(moves1[i]):
                self.board.make_move(moves1[i][j], self.color) #Make move
                opp_moves = self.board.get_all_possible_moves(opp_color) # get all opponent moves
                our_pieces = self.num_pieces(self.color)
                min = self.num_pieces(self.color)
                #selects min diff pieces lost to pieces taken
                for r,opp_checker in enumerate(opp_moves):
                    for k,opp_move in enumerate(opp_moves[r]):
                        self.board.make_move(opp_moves[r][k], opp_color) #opponent makes move
                        they_eat = our_pieces - self.num_pieces(self.color)
                        moves2 = self.board.get_all_possible_moves(self.color) #all our second moves
                        opponent_pieces = self.num_pieces(opp_color) #number of opponent pieces before our move
                        we_eat = 0
                        #selects max taken pieces
                        for x,checker2 in enumerate(moves2):
                            for v,move2 in enumerate(moves2[x]):
                                self.board.make_move(moves2[x][v], self.color) # we make second move
                                temp = opponent_pieces - self.num_pieces(opp_color)
                                if temp > we_eat:
                                    we_eat = temp
                                    #best = (x,v)
                                self.board.undo()
                        diff = we_eat - they_eat
                        if diff < min:
                            min = diff
                        self.board.undo()
                if min > max:
                    max = min
                    best = (i,j)
                self.board.undo()

        move = moves1[best[0]][best[1]]
        self.board.make_move(move,self.color)
        return move
