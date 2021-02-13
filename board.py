from piece import BlackPawn
from piece import RedPawn
from piece import Cannon
from piece import Rook
from piece import Knight
from piece import BlackElephant
from piece import RedElephant
from piece import BlackGuard
from piece import RedGuard
from piece import BlackKing
from piece import RedKing



class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        

        self.board = [[0 for x in range(9)] for _ in range (rows)]

        self.board[0][0] = Rook(0, 0, "b")
        self.board[0][8] = Rook(0, 8, "b")
        self.board[0][1] = Knight(0, 1, "b")
        self.board[0][7] = Knight(0, 7, "b")
        self.board[0][2] = BlackElephant(0, 2, "b")
        self.board[0][6] = BlackElephant(0, 6, "b")
        self.board[0][3] = BlackGuard(0, 3, "b")
        self.board[0][5] = BlackGuard(0, 5, "b")
        self.board[0][4] = BlackKing(0, 4, "b")
        self.board[2][1] = Cannon(2, 1, "b")
        self.board[2][7] = Cannon(2, 7, "b")
        self.board[3][0] = BlackPawn(3, 0, "b")
        self.board[3][2] = BlackPawn(3, 2, "b")
        self.board[3][4] = BlackPawn(3, 4, "b")
        self.board[3][6] = BlackPawn(3, 6, "b")
        self.board[3][8] = BlackPawn(3, 8, "b")

        self.board[9][0] = Rook(9, 0, "r")
        self.board[9][8] = Rook(9, 8, "r")
        self.board[9][1] = Knight(9, 1, "r")
        self.board[9][7] = Knight(9, 7, "r")
        self.board[9][2] = RedElephant(9, 2, "r")
        self.board[9][6] = RedElephant(9, 6, "r")
        self.board[9][3] = RedGuard(9, 3, "r")
        self.board[9][5] = RedGuard(9, 5, "r")
        self.board[9][4] = RedKing(9, 4, "r")
        self.board[7][1] = Cannon(7, 1, "r")
        self.board[7][7] = Cannon(7, 7, "r")
        self.board[6][0] = RedPawn(6, 0, "r")
        self.board[6][2] = RedPawn(6, 2, "r")
        self.board[6][4] = RedPawn(6, 4, "r")
        self.board[6][6] = RedPawn(6, 6, "r")
        self.board[6][8] = RedPawn(6, 8, "r")


    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)


    def draw(self, screen): #Draw pieces in its starting position
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(screen)   
    
    def get_danger_moves(self, color):
        danger_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color:
                        for move in self.board[i][j].move_list:
                            danger_moves.append(move)

        return danger_moves

    def check_mate(self, color):  
        danger_moves = self.get_danger_moves(color)
        king_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == color:
                        for move in self.board[i][j].move_list:
                            king_moves.append(move)
                    
                    
        if len(king_moves) == 0:
            return False       

        for move in king_moves:
            if move not in danger_moves:
                return False

        return True



    def is_checked(self, color):
        danger_moves = self.get_danger_moves(color)
        king_pos = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == color:
                        king_pos = (j, i) 

        if king_pos in danger_moves:
            return True
        return False

        

    def select(self, col, row): #Selecting 
        prev = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].selected:
                        prev = (i, j)

        if self.board[row][col] == 0:
            moves = self.board[prev[0]][prev[1]].move_list
            if (col, row) in moves:
                self.move(prev, (row, col))
            self.unselect()
        else: 
            #Taking pieces
            if self.board[prev[0]][prev[1]].color != self.board[row][col].color:
                moves = self.board[prev[0]][prev[1]].move_list
                if (col, row) in moves:
                    self.move(prev, (row, col))
                self.unselect()               
                self.board[row][col].selected = True

            else:
                self.unselect()
                self.board[row][col].selected = True



            
    def unselect(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False

            

    def move(self, start, end):
        nBoard = self.board[:]
        nBoard[start[0]][start[1]].change_pos((end[0], end[1]))
        nBoard[end[0]][end[1]] = nBoard[start[0]][start[1]]
        nBoard[start[0]][start[1]] = 0
        self.board = nBoard