import pygame
from pygame.locals import *
from game_state import GameState
import pygame.gfxdraw

chess_game = GameState()

background_colour = (255, 0, 0) 

piece_to_image_name = {'p': 'black_pawn', 'b': 'black_bisschop', 'n': 'black_knight', 'r': 'black_rook', 'q': 'black_queen', 'k': 'black_king', 'P': 'white_pawn', 'B': 'white_bisschop', 'N': 'white_knight', 'R': 'white_rook', 'Q': 'white_queen', 'K': 'white_king'}
loaded_pieces = {}
# Constants
WIDTH, HEIGHT = (1024, 1024)
RECT_SIZE = 1024 / 8

# colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (1, 50, 32)
RED = (255, 0, 0)
LIGHT_RED = (255, 127, 127)
BROWN = (184, 140, 100)
DARKER_WHITE = (248, 220, 180)

screen = pygame.display.set_mode((1024, 1024)) 
pygame.display.set_caption('Chess Game') 

def draw_indicators(piece, row, col):
    for row, col in chess_game.get_moves(piece, row, col):
        pygame.gfxdraw.aacircle(screen, int(col * RECT_SIZE + RECT_SIZE / 2), int(row * RECT_SIZE + RECT_SIZE / 2), 20, RED)
        pygame.gfxdraw.filled_circle(screen, int(col * RECT_SIZE + RECT_SIZE / 2), int(row * RECT_SIZE + RECT_SIZE / 2), 20, RED)

def draw_pieces():
    for row, line in enumerate(chess_game.board):
        for col, cell in enumerate(chess_game.board[row]):
            if cell == ' ':
                continue
            if cell in loaded_pieces:
                screen.blit(loaded_pieces[cell], (col * RECT_SIZE, row * RECT_SIZE))
            else:
                image = pygame.image.load(f'images/{piece_to_image_name[cell]}.png').convert_alpha()
                image = pygame.transform.smoothscale(image, (RECT_SIZE, RECT_SIZE))
                loaded_pieces[cell] = image
                screen.blit(image, (col * RECT_SIZE, row * RECT_SIZE))

def draw_squares():
    for row in range(len(chess_game.board)):
        for col in range(len(chess_game.board)):
            if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
                pygame.draw.rect(screen, DARKER_WHITE, Rect(col * RECT_SIZE, row * RECT_SIZE, RECT_SIZE, RECT_SIZE))
            else:
                pygame.draw.rect(screen, BROWN, Rect(col * RECT_SIZE, row * RECT_SIZE, RECT_SIZE, RECT_SIZE))

draw_squares()
draw_pieces()

running = True

while running: 
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            col, row = event.pos

            col = col // RECT_SIZE
            row = row // RECT_SIZE

            if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
                pygame.draw.rect(screen, LIGHT_RED, Rect(col * RECT_SIZE, row * RECT_SIZE, RECT_SIZE, RECT_SIZE))
            else:
                pygame.draw.rect(screen, RED, Rect(col * RECT_SIZE, row * RECT_SIZE, RECT_SIZE, RECT_SIZE))

            pygame.display.flip()  
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            col, row = event.pos

            col = int(col // RECT_SIZE)
            row = int(row // RECT_SIZE)

            piece = chess_game.board[row][col]
            draw_squares()
            draw_pieces()
            draw_indicators(piece, row, col)
            pygame.display.flip()  
        
    pygame.display.flip() 
