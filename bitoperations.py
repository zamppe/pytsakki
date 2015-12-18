from const import *
import lookups
from cengine import *

def bitboard(bb):
    """prints bitboard in readable 8x8 format"""
    import re
    for x in re.findall('[01]{8}', '{0:0>64b}'.format(bb)): print x
    
def bitscan(bb):
    return index64[((bb & -bb) * debruijn64) >> uint64l[58]]

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
def bitscan_reverse(bb):
    bb |= bb >> uint64l[1]
    bb |= bb >> uint64l[2]
    bb |= bb >> uint64l[4]
    bb |= bb >> uint64l[8]
    bb |= bb >> uint64l[16]
    bb |= bb >> uint64l[32]
    return index64r[(bb * debruijn64) >> uint64l[58]]

def get_indices(bitboard):
    """returns a set of indices of 1 bits"""
    indices = []
    c = 0  
    while bitboard:
        bit = bitboard & uint64l[1]
        bitboard >>= uint64l[1]
        if bit:
            indices.append(c)
        c += 1
    return set(indices)

def north(bb):          return  bb << uint64l[8]
def south(bb):          return  bb >> uint64l[8]                   
def east(bb):           return (bb >> uint64l[1]) & notA  
def west(bb):           return (bb << uint64l[1]) & notH
def north_west(bb):     return (bb << uint64l[9]) & notH
def north_east(bb):     return (bb << uint64l[7]) & notA
def south_west(bb):     return (bb >> uint64l[7]) & notH
def south_east(bb):     return (bb >> uint64l[9]) & notA
def ray_north(sq):      return lookups.northattacks[sq]
def ray_south(sq):      return lookups.southattacks[sq]
def ray_east(sq):       return lookups.eastattacks[sq]
def ray_west(sq):       return lookups.westattacks[sq]
def ray_north_west(sq): return lookups.nwattacks[sq]
def ray_north_east(sq): return lookups.neattacks[sq]
def ray_south_west(sq): return lookups.swattacks[sq]
def ray_south_east(sq): return lookups.seattacks[sq]

def diagonal_attacks(board, sq):
    nw = ray_north_west(sq)
    blocker = board.occupiedBB & nw
    if blocker:
        nw ^= ray_north_west(bitscan(blocker))

    se = ray_south_east(sq)
    blocker = board.occupiedBB & se
    if blocker:
        se ^= ray_south_east(bitscan_reverse(blocker))

    ne = ray_north_east(sq)
    blocker = board.occupiedBB & ne
    if blocker:
        ne ^= ray_north_east(bitscan(blocker))

    sw = ray_south_west(sq)
    blocker = board.occupiedBB & sw
    if blocker:
        sw ^= ray_south_west(bitscan_reverse(blocker))

    return ne | sw | nw | se

def file_attacks(board, sq):
    s = ray_south(sq)
    blocker = board.occupiedBB & s
    if blocker:
        s ^= ray_south(bitscan_reverse(blocker))

    n = ray_north(sq)
    blocker = board.occupiedBB & n
    if blocker:
        n ^= ray_north(bitscan(blocker))

    return s | n

def rank_attacks(board, sq):
    w = ray_west(sq)
    blocker = board.occupiedBB & w
    if blocker:
        w ^= ray_west(bitscan(blocker))

    e = ray_east(sq)
    blocker = board.occupiedBB & e
    if blocker:
        e ^= ray_east(bitscan_reverse(blocker))

    return w | e
