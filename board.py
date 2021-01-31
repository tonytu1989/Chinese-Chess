import pygame
import os

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        

        self.board = [[0 for x in range(9)] for _ in range (rows)]

        self.board[0][0] = Rook(0, 0, "b")
        self.board[0][8] = Rook(0, 8, "b")
        self.board[0][1] = Knight(0, 1, "b")
        self.board[0][7] = Knight(0, 7, "b")
        self.board[0][2] = Elephant(0, 2, "b")
        self.board[0][6] = Elephant(0, 6, "b")
        self.board[0][3] = Guard(0, 3, "b")
        self.board[0][5] = Guard(0, 5, "b")
        self.board[0][4] = King(0, 4, "b")
        self.board[2][1] = Cannon(2, 1, "b")
        self.board[2][7] = Cannon(2, 7, "b")
        self.board[3][0] = Pawn(3, 0, "b")
        self.board[3][2] = Pawn(3, 2, "b")
        self.board[3][4] = Pawn(3, 4, "b")
        self.board[3][6] = Pawn(3, 6, "b")
        self.board[3][8] = Pawn(3, 8, "b")

        self.board[9][0] = Rook(9, 0, "r")
        self.board[9][8] = Rook(9, 8, "r")
        self.board[9][1] = Knight(9, 1, "r")
        self.board[9][7] = Knight(9, 7, "r")
        self.board[9][2] = Elephant(9, 2, "r")
        self.board[9][6] = Elephant(9, 6, "r")
        self.board[9][3] = Guard(9, 3, "r")
        self.board[9][5] = Guard(9, 5, "r")
        self.board[9][4] = King(9, 4, "r")
        self.board[7][1] = Cannon(7, 1, "r")
        self.board[7][7] = Cannon(7, 7, "r")
        self.board[6][0] = Pawn(6, 0, "r")
        self.board[6][2] = Pawn(6, 2, "r")
        self.board[6][4] = Pawn(6, 4, "r")
        self.board[6][6] = Pawn(6, 6, "r")
        self.board[6][8] = Pawn(6, 8, "r")

    def draw(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(screen)   
        