import pygame
import os
from board import Board

board = pygame.image.load(os.path.join('images','chess_board.png'))


def game_window():
    global screen 
    screen.blit(board, (0, 0))
    bo = Board(10, 9)
    bo.draw(screen)
    

    pygame.display.update()


def main():

    running = True
    clock = pygame.time.Clock()

    while running:

        game_window()

        
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


screen = pygame.display.set_mode((900, 1000)) #Board is 9 x 10
pygame.display.set_caption("Chinese_Chess")
main()
