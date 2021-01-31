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
    R.append(pygame.transform.scale(img, (70, 70))) 
for img in b:
    B.append(pygame.transform.scale(img, (70, 70)))


class Piece:
    img = -1

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def move(self):
        pass

    def selected(self):
        return self.selected
    
    def draw(self, screen):
        if self.color == 'r':
            draw_piece = R[self.img]
        else:
            draw_piece = B[self.img] 

#make img indexes from r and b list
class Pawn(Piece):
    img = 0

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