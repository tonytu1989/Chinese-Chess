import pygame
import os
from board import Board

board = pygame.transform.scale(pygame.image.load(os.path.join('images','chess_board.png')), (880, 980))
rect = (0, 0, 900, 1000)

def game_window():
    global screen, bo 
    screen.blit(board, (0, 0))
    bo.draw(screen)
    pygame.display.update()

def game_over(screen, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text, 1, (255, 0, 0))
    win.blit(txt, (width/2 - txt.get_width()/2, 300))
    running = True
    pygame.display.update()

    PYGAME.SET_TIME(PYGAME.userevent+1, 5000)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False
            elif event.type == pygame.USEREVENT+1:
                running = False

        

def click(pos):
    import math

    """ return pos (x, y) """

    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < x < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[1]
            i = int(divX / (rect[2]/9))
            j = int(divY / (rect[3]/10))
            return i, j




def main():
    global bo
    bo = Board(10, 9)
    bo.update_moves()
    running = True
    clock = pygame.time.Clock()

    while running:

        game_window()

        
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                bo.update_moves()
                i, j = click(pos)
                bo.select(i, j)
                bo.update_moves()

        #Check for checkmate
        if bo.check_mate('r'):
            game_over(screen, "RED WINS")
        elif bo.check_mate('b'):
            game_over(screen, "Black WINS")
        




screen = pygame.display.set_mode((880, 980)) #Board is 9 x 10
pygame.display.set_caption("Chinese_Chess")
main()
