import pygame
from pygame.locals import *
from cengine import Engine
from const import *

screen_size = (800, 600)
sq_size = 60
def index_to_screen(index):    
    x = (7 - index % 8) * sq_size + 20
    y = (7 - index / 8) * sq_size + 20
    return x, y

def screen_to_index(x, y):    
    x = 7-((x-20) / 60)
    y = 7-((y-20) / 60)
    return y*8+x

def update_screen(screen, bg, pieces, sprites):
    screen.blit(bg,(0,0))           
    for piece, indices in pieces.items():
        for index in indices:
            screen.blit(sprites[piece], index_to_screen(index))
    pygame.display.flip()
def main():
    sprites = {WP: pygame.transform.scale(pygame.image.load('data/white/pawn.png'), (60, 60)),
               WB: pygame.transform.scale(pygame.image.load('data/white/bishop.png'), (60, 60)),
               WN: pygame.transform.scale(pygame.image.load('data/white/knight.png'), (60, 60)),
               WR: pygame.transform.scale(pygame.image.load('data/white/rook.png'), (60, 60)),
               WQ: pygame.transform.scale(pygame.image.load('data/white/queen.png'), (60, 60)),
               WK: pygame.transform.scale(pygame.image.load('data/white/king.png'), (60, 60)),
               BP: pygame.transform.scale(pygame.image.load('data/black/pawn.png'), (60, 60)),
               BB: pygame.transform.scale(pygame.image.load('data/black/bishop.png'), (60, 60)),
               BN: pygame.transform.scale(pygame.image.load('data/black/knight.png'), (60, 60)),
               BR: pygame.transform.scale(pygame.image.load('data/black/rook.png'), (60, 60)),
               BQ: pygame.transform.scale(pygame.image.load('data/black/queen.png'), (60, 60)),
               BK: pygame.transform.scale(pygame.image.load('data/black/king.png'), (60, 60))}
    screen = pygame.display.set_mode(screen_size)
    eng = Engine()
    bg = pygame.image.load('data/background1.png')
    frm, to = 0, 0
    update_screen(screen, bg, eng.board.piece_indices, sprites)
    while(1):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if frm and not to:
                        to = screen_to_index(*event.pos)
                    if not frm:
                        frm = screen_to_index(*event.pos)

                    if frm and to and eng.turn == WHITE:
                        eng.move(frm, to)
                        frm, to = 0,0
                        update_screen(screen, bg, eng.board.piece_indices, sprites)
        if eng.turn == BLACK:
            eng.AI_move()
            update_screen(screen, bg, eng.board.piece_indices, sprites)
##                elif event.button == 3:
##                    x, y = event.pos
##                    down['mouse3'] = 1

main()
