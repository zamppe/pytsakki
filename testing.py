from numpy import uint64
from cengine import *

def benchmark(func):
    """ a decorator that prints the processing time of a function"""
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        tt = time.clock()-t
        print(func.__name__, tt)
        return res
    return wrapper



def bitboard(n):
        import re
        string = "{0:064b}".format(n)
        for line in re.findall('[01]{8}', string):
            print(line)
    ##    return '\n'.join(x for x in re.findall('[01]{8}', str("{0:064b}".format(n))))

def print_bitboards():
    collection = [black_pieces, white_pieces, occupiedBB, emptyBB,
              black_pawns, black_rooks, black_knights,
              black_bishops, black_queens, black_kings,
              white_pawns, white_rooks, white_knights,
              white_bishops, white_queens, white_kings]
    for board in collection:
        bitboard(board)
        print()


@benchmark
def main():
    e = Engine()
    for _ in range(10000):
        attack_squares(e.board, WHITE)
    
##    screen = pygame.set_screen
##    

##    for event in events
##      if mous down:
##         mous_down = tru
##         from_sq = translate(mous coordinates)
##         piece = piece_at(from_sq)
##         
##      if mous up:
##         mous_down = fals
##         to_sq = translate(mous coordinates)
##         if piece_at(to_sq) == EMPTY : make quiet move
##      if wheelmotion and mous_down and piece_at(from_sq) != EMPTY :
##         move piece sprite on screen to mous coords
main()
