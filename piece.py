import pygame
import os


red_pawn = pygame.image.load(os.path.join('images','rP.png'))
red_cannon = pygame.image.load(os.path.join('images','rC.png'))
red_rook = pygame.image.load(os.path.join('images','rR.png'))
red_knight = pygame.image.load(os.path.join('images','rN.png'))
red_elephant = pygame.image.load(os.path.join('images','rE.png'))
red_guard = pygame.image.load(os.path.join('images','rG.png'))
red_king = pygame.image.load(os.path.join('images','rK.png'))

black_pawn = pygame.image.load(os.path.join('images','bP.png'))
black_cannon = pygame.image.load(os.path.join('images','bC.png'))
black_rook = pygame.image.load(os.path.join('images','bR.png'))
black_knight = pygame.image.load(os.path.join('images','bN.png'))
black_elephant = pygame.image.load(os.path.join('images','bE.png'))
black_guard = pygame.image.load(os.path.join('images','bG.png'))
black_king = pygame.image.load(os.path.join('images','bK.png'))

r = [red_pawn, red_cannon, red_rook, red_knight, red_elephant, red_guard, red_king]
b = [black_pawn, black_cannon, black_rook, black_knight, black_elephant, black_guard, black_king]

R = []
B = []

#scaling images
for img in r:
    R.append(pygame.transform.scale(img, (68, 68))) 
for img in b:
    B.append(pygame.transform.scale(img, (68, 68)))


class Piece:
    img = -1
    rect = (0, 0, 900, 1000)
    startX = rect[0]
    startY = rect[1]


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []



    def is_selected(self):
        return self.selected
    
    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)

    def draw(self, screen):
        if self.color == 'r':
            draw_piece = R[self.img]
        else:
            draw_piece = B[self.img] 

        if self.selected:

            moves = self.move_list

            for move in moves:
                x = 35 + round(self.startX + (move[0] * self.rect[2]/9))
                y = 35 + round(self.startY + (move[1] * self.rect[3]/10))
                pygame.draw.circle(screen, (255, 0, 0,), (x, y), 10)

         
        x = 1 + round(self.startX + (self.col * self.rect[2]/9))
        y = 1 + round(self.startY + (self.row * self.rect[3]/10))

        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, 75, 75), 5)

        screen.blit(draw_piece, (x, y))

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

#make img indexes from r and b list
class Pawn(Piece):
    img = 0

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.super_pawn = False
        self.pawn = True

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        
        
        if self.color =='b':
            if i < 5:
                p = board[i + 1][j]
                if p == 0:
                    moves.append((j, i + 1))
                elif p.color != self.color:
                    moves.append((j, i + 1))

        else:
            if i > 0:
                p = board[i - 1][j]
                if p == 0:
                    moves.append((j, i - 1))
                elif p.color != self.color:
                    moves.append((j, i - 1))
                    
        return moves


class Cannon(Piece):
    img = 1
    
    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        #UP
        for x in range(i -1, -1, - 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        #Down
        for x in range(i + 1, 9, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        #Left
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        #Right
        for x in range(j + 1, 9, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
            else:
                break

        return moves


class Rook(Piece):
    img = 2

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        #UP
        for x in range(i -1, -1, - 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        #Down
        for x in range(i + 1, 9, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        #Left
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        #Right
        for x in range(j + 1, 9, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
            else:
                break

        return moves



class Knight(Piece):
    img = 3

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        #Down left
        if i < 9 and j > 0:
            p = board[i + 2][j - 1]
            if p == 0:
                moves.append((j - 1, i + 2))
            elif p.color != self.color:
                moves.append((j - 1, i + 2))

        #UP left
        if i > 1 and j > 0:
            p = board[i - 2][j - 1]
            if p == 0:
                moves.append((j - 1, i - 2))
            elif p.color != self.color:
                moves.append((j - 1, i - 2))

        #Down Right
        if i < 8 and j < 9:
            p = board[i + 2][j + 1]
            if p == 0:
                moves.append((j + 1, i + 2))
            elif p.color != self.color:
                moves.append((j + 1, i + 2))

        #Up right
        if i > 1 and j < 9:
            p = board[i - 2][j + 1]
            if p == 0:
                moves.append((j + 1, i - 2))
            elif p.color != self.color:
                moves.append((j + 1 - 2))

        return moves


class Elephant(Piece):
    img = 4

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        #Up LEFT Diagonal
        if self.color == 'b':
        #Down Left Diagonal        
            if i < 9: 
                if j > 0:
                    p = board[i + 2][j - 2]
                    if p == 0:
                        moves.append((j - 2, i + 2))
                    elif p.color != self.color:
                        moves.append((j - 2, i + 2))
                #Down Right Diagonal
                if j < 9:
                    p = board[i + 2][j + 2]
                    if p == 0:
                        moves.append((j + 2, i + 2))    
                    elif p.color != self.color:
                        moves.append((j + 2, i + 2))
        else:
            #Up left
            if i > 0:
                if j < 9:
                    p = board[i - 2][j - 2]
                    if p == 0:
                        moves.append((j - 2, i - 2))
                    elif p.color != self.color:
                        moves.append((j - 2, i - 2))

                #Up RIGHT    
                if j < 9:
                    p = board[i - 2][j + 2]
                    if p == 0:                      
                        moves.append((j + 2, i - 2))
                    elif p.color != self.color:
                        moves.append((j + 2, - 2))
        return moves  

class Guard(Piece):
    img = 5

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if self.color == 'b':
        #Down Left Diagonal        
            if i < 3 and j < 6 and j > 3: 
                if j > 0:
                    p = board[i + 1][j - 1]
                    if p == 0:
                        moves.append((j - 1, i + 1))
                    elif p.color != self.color:
                        moves.append((j - 1, i + 1))

                #Down Right Diagonal
            if i < 3 and j < 6 and j > 3:
                if j < 6:
                    p = board[i + 1][j + 1]
                    if p == 0:
                        moves.append((j + 1, i + 1))    
                    elif p.color != self.color:
                        moves.append((j + 1, i + 1))
        else:
            #Up left
            if i > 0:
                if j < 7:
                    p = board[i - 1][j - 1]
                    if p == 0:
                        moves.append((j - 1, i - 1))
                    elif p.color != self.color:
                        moves.append((j - 1, i - 1))
                #Up RIGHT    
                if j < 9:
                    p = board[i - 1][j + 1]
                    if p == 0:                      
                        moves.append((j + 1, i - 1))
                    elif p.color != self.color:
                        moves.append((j + 1, i - 1))
        return moves  
            


class King(Piece):
    img = 6

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves =[]
        #UP
        if i > 0:
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))
        #Down
        if i < 9:
            if j > 0:
                p = board[i + 1][j]
                if p == 0:
                    moves.append((j, i + 1))
                elif p.color != self.color:
                    moves.append((j, i + 1))
        #Left
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))
        #Right
        if j < 9:
            p = board[i][j + 1]
            if p ==0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))

        return moves
