from random import randint
from BoardClasses import Move
from BoardClasses import Board
import random
import math
import logging
logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
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
        self.startPieces = self.num_pieces(self.color) * 2

    def num_pieces(self, color):
        if color == 1:
            openent_pieces = self.board.black_count
        elif color == 2:
            openent_pieces = self.board.white_count
        return openent_pieces

    def get_max(self,depth,iterations):
        opp_color = self.opponent[self.color]
        best = (0,0)
        if depth == iterations:
            moves = self.board.get_all_possible_moves(self.color)
            opponent_pieces = self.num_pieces(opp_color) #number of opponent pieces before our move
            we_eat = 0
            #selects max taken pieces
            for x,checker in enumerate(moves):
                for v,move in enumerate(moves[x]):
                    self.board.make_move(moves[x][v], self.color) # we make second move
                    temp = opponent_pieces - self.num_pieces(opp_color)
                    if temp > we_eat:
                        we_eat = temp
                        best = (x,v)
                    self.board.undo()
            return (we_eat,best)
        else:
            best = (0,0)
            moves = self.board.get_all_possible_moves(self.color)
            max = -(self.num_pieces(self.color))
            our_pieces = self.num_pieces(self.color) # our pieces before our move
            for i,checker in enumerate(moves):
                for j,move in enumerate(moves[i]):
                    self.board.make_move(moves[i][j], self.color) #Make move
                    min = self.get_min(depth + 1, iterations)
                    if min > max:
                        max = min
                        best = (i,j)
                    elif min == max:
                        if(randint(0,1)):
                            best = (i,j)
                    self.board.undo()
            logging.info(best)
            return(max,best)

    def get_min(self, depth, iterations):
        min_color = self.opponent[self.color]
        min = self.num_pieces(min_color)
        if depth == iterations - 1:
            min_moves = self.board.get_all_possible_moves(min_color)
            maxs_pieces = self.num_pieces(self.color)
            for x, checker in enumerate(min_moves):
                for y, move in enumerate(min_moves[x]):
                    self.board.make_move(min_moves[x][y], min_color)
                    min_eats = maxs_pieces - self.num_pieces(self.color)
                    max_eats,b = self.get_max(depth + 1, iterations)
                    diff = max_eats - min_eats
                    if diff < min:
                        min = diff
                    self.board.undo()
            return min
        else:
            min_moves = self.board.get_all_possible_moves(min_color)
            for x, checker in enumerate(min_moves):
                for y, move in enumerate(min_moves[x]):
                    self.board.make_move(min_moves[x][y], min_color)
                    max_eats,b = self.get_max(depth + 1, iterations)
                    if max_eats < min:
                        min = max_eats
                    self.board.undo()
            return min

    def get_move(self,move):
        opp_color = self.opponent[self.color]
        tot_pieces = self.num_pieces(self.color) + self.num_pieces(opp_color)
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        max1,best1 = self.get_max(1,1)
        max2,best2 = self.get_max(1,3)
        max3,best3 = self.get_max(1,5)

        piece_prob = (tot_pieces/self.startPieces)/1.3
        if piece_prob
        probs = [prob1, prob2, prob3]
        bestl = [best1,best2,best3]
        r = random.random()
        index = 0
        while(r >= 0 and index < len(probs)):
          r -= probs[index]
          index += 1
        best = bestl[index-1]


        '''
        if max == 0 and len(self.board.get_all_possible_moves(opp_color)) < 3:
            ## Idea to improve choice, if max is tied look at the move which will get us closes
            ## closest to opponent piece
            inner = i
            distance = 100
            checker = self.board.get_all_possible_moves(opp_color)
            opp_checker = checker[0][0].seq[0]
            #for i,checker in enumerate(moves1):
            for j,move in enumerate(moves1[0]):
                temp_dist = math.sqrt(sum([(a - b) ** 2 for a, b in zip(move[0], opp_checker)]))
                if temp_dist < distance:
                    best = (0,j)
        '''
        move = moves[best[0]][best[1]]
        self.board.make_move(move,self.color)
        return move
