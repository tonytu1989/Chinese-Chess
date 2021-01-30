import pygame
import os
board = pygame.image.load(os.path.join('images','chess_board.png'))
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

def main():
    running = True
    clock = pygame.time.Clock()

    while running:

        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        pygame.display.flip()


screen = pygame.display.set_mode((900, 1000)) #Board is 9 x 10
pygame.display.set_caption("Chinese_Chess")
screen.blit(board, (0, 0))
screen.blit(black_elephant, (100, 100))
main()
