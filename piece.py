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

    def move(self):
        pass

    def is_selected(self):
        return self.selected
    
    def draw(self, screen, board):
        if self.color == 'r':
            draw_piece = R[self.img]
        else:
            draw_piece = B[self.img] 

        moves = self.valid_moves(board)

        for move in moves:
            x = 45 + round(self.startX + (self.move[0] * self.rect[2]/9))
            y = 45 + round(self.startY + (self.move[1] * self.rect[3]/10))
            pygame.draw.circle(screen, (255, 0, 0,), 10)

         
        x = 1 + round(self.startX + (self.col * self.rect[2]/9))
        y = 1 + round(self.startY + (self.row * self.rect[3]/10))

        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, 75, 75), 5)

        screen.blit(draw_piece, (x, y))

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
        
        try:
            if self.color =='b':
                if i < 3:
                    p = board[i + 1][j]
                    if p == 0:
                        moves.append((j, i + 1))
        except:
            pass

        return moves


class Cannon(Piece):
    img = 1
    



class Rook(Piece):
    img = 2

class Knight(Piece):
    img = 3

class Elephant(Piece):
    img = 4

class Guard(Piece):
    img = 5

class King(Piece):
    img = 6