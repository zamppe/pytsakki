from lookups import *
from const import *
from bitoperations import *





class Board:
    def __init__(self, *args):
        if args:
            self.pieceBB = [0]*15
            for ptype, value in enumerate(args[0]):        
                self.pieceBB[ptype] = uint64(value)
            self.occupiedBB = uint64(args[1])
            self.emptyBB = uint64(args[2])
            self.piece_indices = {}
            for piece, indices in args[3].items():
                self.piece_indices[piece] = indices
        else:
            """the initial chess position"""
            self.pieceBB = [0]*15
            self.pieceBB[WHITE] = uint64(65535L)
            self.pieceBB[BLACK] = uint64(18446462598732840960L)
            self.pieceBB[WP] = uint64(65280)
            self.pieceBB[WB] = uint64(36)
            self.pieceBB[WN] = uint64(66)
            self.pieceBB[WR] = uint64(129)
            self.pieceBB[WQ] = uint64(16)
            self.pieceBB[WK] = uint64(8)
            self.pieceBB[BP] = uint64(71776119061217280L)
            self.pieceBB[BB] = uint64(2594073385365405696L)
            self.pieceBB[BN] = uint64(4755801206503243776L)
            self.pieceBB[BR] = uint64(9295429630892703744L)
            self.pieceBB[BQ] = uint64(1152921504606846976L)
            self.pieceBB[BK] = uint64(576460752303423488L)
            self.occupiedBB = uint64(self.pieceBB[BLACK] | self.pieceBB[WHITE])
            self.emptyBB = uint64(~self.occupiedBB)
            self.piece_indices = {0:[],
                                  3:[15,14,13,12,11,10,9,8],
                                  5:[5,2],
                                  7:[6,1],
                                  9:[7,0],
                                  11:[4],
                                  13:[3],
                                  4:[55,54,53,52,51,50,49,48],
                                  6:[61, 58],
                                  8:[62, 57],
                                  10:[63, 56],
                                  12:[60],                 
                                  14:[59]}
            self.piece_counts = [0,0,0,8,8,2,2,2,2,2,2,1,1,1,1]
            self.best_black = None
            self.moves = 0
    def piece_at(self, index):
        for piece, indices in self.piece_indices.items():
            if index in indices: return piece
        return EMPTY
##        flag = flags[index]
##        if(self.emptyBB & flag != 0):
##            return EMPTY
##        color = self.color_at(index)
##        if color == WHITE:
##            for piece in [WP,WB,WN,WR,WQ,WK]:
##                if(self.pieceBB[piece] & flag != 0):
##                    return piece
##        elif color == BLACK:
##            for piece in [BP,BB,BN,BR,BQ,BK]:
##                if(self.pieceBB[piece] & flag != 0):
##                    return piece
                
    

    def print_board(self):
        table = ['00']*64
        for ptype in range(3, 15):
            indices = get_indices(self.pieceBB[ptype])
            for index in indices:
                table[63-index] = piece_shortcuts[ptype]
        string = ''
        print '--------'
        print 'moves: '+str(self.moves)
        for i in range(8, 65, 8):
            print(table[i-8:i])
    
    def make_move(self, move):
        """he doesn't care about the rules, he only does what he's been told to."""
        fromBB = flags[move.frm]
        toBB = flags[move.to]
        fromto = fromBB ^ toBB
        self.pieceBB[move.ptype] ^= fromto
        self.pieceBB[move.pcolor] ^= fromto
        if isinstance(move, QuietMove):    
            self.occupiedBB ^= fromto
            self.emptyBB ^= fromto
        else:
            self.pieceBB[move.ctype] ^= toBB
            self.pieceBB[move.ccolor] ^= toBB
            self.occupiedBB ^= fromBB
            self.emptyBB ^= fromBB
            #remove the index of the captured piece
            self.piece_indices[move.ctype] = [i for i in self.piece_indices[move.ctype] if i != move.to]
            self.piece_counts[move.ctype] -= 1
        #change the index of the moved piece
        self.piece_indices[move.ptype] = [i if i != move.frm else move.to for i in self.piece_indices[move.ptype]]
        self.moves+=1

    def unmake_move(self, move):
        """make_move and unmake_move are dangerous methods. calls must be made
           in turns correctly for piece_indices to remain correct"""
        fromBB = flags[move.frm]
        toBB = flags[move.to]
        fromto = fromBB ^ toBB
        self.pieceBB[move.ptype] ^= fromto
        self.pieceBB[move.pcolor] ^= fromto
        if isinstance(move, QuietMove):    
            self.occupiedBB ^= fromto
            self.emptyBB ^= fromto
        else:
            self.pieceBB[move.ctype] ^= toBB
            self.pieceBB[move.ccolor] ^= toBB
            self.occupiedBB ^= fromBB
            self.emptyBB ^= fromBB
            #add the index of the captured piece back
            self.piece_indices[move.ctype] += [move.to]
            self.piece_counts[move.ctype] += 1
        #change the index of the moved piece
        self.piece_indices[move.ptype] = [i if i != move.to else move.frm for i in self.piece_indices[move.ptype]]
        self.moves-=1
    
    def get_moves(self, color):
        moves = []
        for piece, indices in self.piece_indices.items():            
            for from_sq in indices:                
                if piece == WP+color:
                    to_squares = get_indices(legit_pawn_moves(self, from_sq, color))
                elif piece == WN+color:
                    to_squares = get_indices(legit_knight_moves(self, from_sq, color))
                elif piece == WB+color:
                    to_squares = get_indices(legit_bishop_moves(self, from_sq, color))
                elif piece == WR+color:
                    to_squares = get_indices(legit_rook_moves(self, from_sq, color))
                elif piece == WQ+color:
                    to_squares = get_indices(legit_queen_moves(self, from_sq, color))
                elif piece == WK+color:
                    to_squares = get_indices(legit_king_moves(self, from_sq, color))
                else:
                    to_squares=[]
                for to_sq in to_squares:
                    tgt = self.piece_at(to_sq)
                    if tgt != EMPTY:
                        moves.append(CapturingMove(from_sq, to_sq, piece, color, tgt, color^1))
                    else:
                        moves.append(QuietMove(from_sq, to_sq, piece, color))
        return sorted(moves, key=lambda move: move.value, reverse = True)

##    def get_black_moves(self):
##        moves = []
##        for piece, indices in piece_indices.items():
##            for from_sq in indices:
##                if piece == BP:
##                    to_squares = legit_pawn_moves(self, from_sq, BLACK)
##                elif piece == BN:
##                    to_squares = legit_knight_moves(self, from_sq, BLACK)
##                elif piece == BB:
##                    to_squares = legit_bishop_moves(self, from_sq, BLACK)
##                elif piece == BR:
##                    to_squares = legit_rook_moves(self, from_sq, BLACK)
##                elif piece == BQ:
##                    to_squares = legit_queen_moves(self, from_sq, BLACK)
##                elif piece == BK:
##                    to_squares = legit_king_moves(self, from_sq, BLACK)
##                
##                for to_sq in to_squares:
##                    tgt = self.piece_at(to_sq)
##                    if tgt != EMPTY:
##                        CapturingMove(from_sq, to_sq, piece, BLACK, tgt, WHITE)
##                    else:
##                        QuietMove(from_sq, to_sq, piece, BLACK)
##        return moves
##            
##
##    def get_white_moves(self):
##        moves = []
##        for piece, indices in piece_indices.items():
##            for from_sq in indices:
##                if piece == WP:
##                    to_squares = legit_pawn_moves(self, from_sq, WHITE)
##                elif piece == WN:
##                    to_squares = legit_knight_moves(self, from_sq, WHITE)
##                elif piece == WB:
##                    to_squares = legit_bishop_moves(self, from_sq, WHITE)
##                elif piece == WR:
##                    to_squares = legit_rook_moves(self, from_sq, WHITE)
##                elif piece == WQ:
##                    to_squares = legit_queen_moves(self, from_sq, WHITE)
##                elif piece == WK:
##                    to_squares = legit_king_moves(self, from_sq, WHITE)
##                
##                for to_sq in to_squares:
##                    tgt = self.piece_at(to_sq)
##                    if tgt != EMPTY:
##                        CapturingMove(from_sq, to_sq, piece, WHITE, tgt, BLACK)
##                    else:
##                        QuietMove(from_sq, to_sq, piece, WHITE)
##        return moves
                

class Move:
    def __init__(self, frm, to, ptype, pcolor):
        self.frm = frm
        self.to = to
        self.ptype = ptype
        self.pcolor = pcolor

    def __str__(self):
        piece = piece_names[self.ptype]
        return piece + ': ' +coords[self.frm] + ' TO ' + coords[self.to]
        
class QuietMove(Move):
    def __init__(self, frm, to, ptype, pcolor):
        Move.__init__(self, frm, to, ptype, pcolor)
##        super(QuietMove, self).__init__(*args, **kwargs)
        self.value = square_value[ptype][to]
    

class CapturingMove(Move):
    def __init__(self, frm, to, ptype, pcolor, ctype, ccolor):
        Move.__init__(self, frm, to, ptype, pcolor)
        self.ctype = ctype
        self.ccolor = ccolor
        self.value = square_value[ptype][to] + piece_value[ctype]        


def legit_moves(board, color):
    pMoves = legit_pawn_moves(board.pieceBB[WP+color], color)
    nMoves = legit_knight_moves(board.pieceBB[WN+color])
    bMoves = legit_bishop_moves(board.pieceBB[WB+color], color)
    rMoves = legit_rook_moves(board.pieceBB[WR+color], color)
    qMoves = legit_queen_moves(board.pieceBB[WQ+color], color)
    kMoves = legit_king_moves(board.pieceBB[WK+color])
    return(pMoves | nMoves | bMoves | rMoves | qMoves | kMoves)    


def legit_pawn_moves(board, index, color):
    """GUI tool"""
    pawnBB = flags[index]
    if color == WHITE:
        aAttack = north_east(pawnBB) & board.pieceBB[BLACK]
        bAttack = north_west(pawnBB) & board.pieceBB[BLACK]
        move1 = north(pawnBB) & board.emptyBB
        move2 = (pawnBB << uint64l[16]) & board.emptyBB & rank4
    else:
        aAttack = south_east(pawnBB) & board.pieceBB[WHITE]
        bAttack = south_west(pawnBB) & board.pieceBB[WHITE]
        move1 = south(pawnBB) & board.emptyBB
        move2 = (pawnBB >> uint64l[16]) & board.emptyBB & rank5
    return aAttack | bAttack | move1 | move2

def legit_knight_moves(board, index, color):
    """GUI tool"""
    knightBB = flags[index]
    nen = (knightBB << uint64l[15]) & notA
    nee = (knightBB << uint64l[6])  & notAB
    see = (knightBB >> uint64l[10]) & notAB
    ses = (knightBB >> uint64l[17]) & notA
    nwn = (knightBB << uint64l[17]) & notH
    nww = (knightBB << uint64l[10]) & notGH
    sww = (knightBB >> uint64l[6])  & notGH
    sws = (knightBB >> uint64l[15]) & notH
    attacks = (nen | nee | see | ses | nwn | nww | sww | sws)
    return (attacks & board.emptyBB) | (attacks & board.pieceBB[color^1])

def legit_bishop_moves(board, index, color):
    """GUI tool"""
    attacks = diagonal_attacks(board, index) 
    return (attacks & board.emptyBB) | (attacks & board.pieceBB[color^1])
      
def legit_rook_moves(board, index, color):
    """GUI tool"""
    attacks = file_attacks(board, index) | rank_attacks(board, index) 
    return (attacks & board.emptyBB) | (attacks & board.pieceBB[color^1])
   
def legit_queen_moves(board, index, color):
    """GUI tool"""
    attacks = file_attacks(board, index) | rank_attacks(board, index) | diagonal_attacks(board, index) 
    return (attacks & board.emptyBB) | (attacks & board.pieceBB[color^1])

def legit_king_moves(board, index, color):
    """GUI tool"""
    kingBB = flags[index]
    nAttack = north(kingBB)
    wAttack = west(kingBB)
    eAttack = east(kingBB)
    sAttack = south(kingBB)    
    neAttack = north_east(kingBB)
    nwAttack = north_west(kingBB)
    seAttack = south_east(kingBB)
    swAttack = south_west(kingBB)
    attacks = (nAttack | wAttack | eAttack | sAttack | neAttack | nwAttack | seAttack | swAttack)
    return (attacks & board.emptyBB) | (attacks & board.pieceBB[color^1])

def attack_squares(board, color):
    """Tool for checking checks and mates"""
    pAttacks = pawn_attack_squares(board, color)
    nAttacks = knight_attack_squares(board, color)
    bAttacks = bishop_attack_squares(board, color)
    rAttacks = rook_attack_squares(board, color)
    qAttacks = queen_attack_squares(board, color)
    kAttacks = king_attack_squares(board, color)
    return(pAttacks | nAttacks | bAttacks | rAttacks | qAttacks | kAttacks)

def pawn_attack_squares(board, color):
    if color == WHITE:
        neAttack = north_east(board.pieceBB[WP])
        nwAttack = north_west(board.pieceBB[WP])
        return neAttack | nwAttack
    else:
        seAttack = south_east(board.pieceBB[BP])
        swAttack = south_west(board.pieceBB[BP])
        return seAttack | swAttack

def knight_attack_squares(board, color):
    nen = (board.pieceBB[WN+color] << uint64l[15]) & notA
    nee = (board.pieceBB[WN+color] << uint64l[6])  & notAB
    see = (board.pieceBB[WN+color] >> uint64l[10]) & notAB
    ses = (board.pieceBB[WN+color] >> uint64l[7])  & notA
    nwn = (board.pieceBB[WN+color] << uint64l[17]) & notH
    nww = (board.pieceBB[WN+color] << uint64l[10]) & notGH
    sww = (board.pieceBB[WN+color] >> uint64l[6])  & notGH
    sws = (board.pieceBB[WN+color] >> uint64l[15]) & notH
    return nen | nee | see | ses | nwn | nww | sww | sws

def bishop_attack_squares(board, color):
##    a = uint64()
##    for i in get_indices(board.pieceBB[WB + color]):
##       a |=  diagonal_attacks(board, i)
##    return a
    return reduce(lambda x, y: x | y, [diagonal_attacks(board, i) for i in get_indices(board.pieceBB[WB + color])])
def rook_attack_squares(board, color):
    return reduce(lambda x, y: x | y, [file_attacks(board, i) | rank_attacks(board, i) for i in get_indices(board.pieceBB[WR + color])])

def queen_attack_squares(board, color):
    return reduce(lambda x, y: x | y, [file_attacks(board, i) | rank_attacks(board, i) | diagonal_attacks(board, i) for i in get_indices(board.pieceBB[WQ + color])])




def king_attack_squares(board, color):
    nAttack = north(board.pieceBB[WK+color])
    wAttack = west(board.pieceBB[WK+color])
    eAttack = east(board.pieceBB[WK+color])
    sAttack = south(board.pieceBB[WK+color])    
    neAttack = north_east(board.pieceBB[WK+color])
    nwAttack = north_west(board.pieceBB[WK+color])
    seAttack = south_east(board.pieceBB[WK+color])
    swAttack = south_west(board.pieceBB[WK+color])
    return (nAttack | wAttack | eAttack | sAttack | neAttack | nwAttack | seAttack | swAttack)

def black_pawn_moves(board):
    move1 = (board.pieceBB[BP] >> uint64l[8]) & board.emptyBB
    move2 = (board.pieceBB[BP] >> uint64l[16]) & board.emptyBB & rank5
    return move1 | move2

def movable_black_pawns(board):
    movableby1 = board.emptyBB<<uint64l[8] & board.pieceBB[BP]
    movableby2 = ((board.emptyBB & rank5)<<uint64l[8] & board.emptyBB)<<uint64l[8] & board.pieceBB[BP]
    return movableby1 | movableby2

def white_pawn_moves(board):
    move1 = (board.pieceBB[WP] << uint64l[8]) & board.emptyBB
    move2 = (board.pieceBB[WP] << uint64l[16]) & board.emptyBB & rank4
    return move1 | move2

def movable_white_pawns(board):
    movableby1 = (board.emptyBB >> uint64l[8]) & board.pieceBB[WP]
    movableby2 = ((board.emptyBB & rank4)>>uint64l[8] & board.emptyBB)>>uint64l[8] & board.pieceBB[WP]
    return movableby1 | movableby2

def black_rook_moves():
    pass

def knight_moves_lookup(board, color):
    return reduce(lambda x, y: x | y, [knightmoves[i] for i in piece_indices[WN+color]])

def knight_moves(knights):
    nen = (knights << uint64l[15]) & notA
    nee = (knights << uint64l[6]) & notAB
    see = (knights >> uint64l[10]) & notAB
    ses = (knights >> uint64l[17]) & notA
    nwn = (knights << uint64l[17]) & notH
    nww = (knights << uint64l[10]) & notGH
    sww = (knights >> uint64l[6]) & notGH
    sws = (knights >> uint64l[15]) & notH
    return nen | nee | see | ses | nwn | nww | sww | sws

        
def black_knight_moves():
    nen = (pieceBB[BN] << uint64l[15]) & notA
    nee = (pieceBB[BN] << uint64l[6]) & notAB
    see = (pieceBB[BN] >> uint64l[10]) & notAB
    ses = (pieceBB[BN] >> uint64l[17]) & notA
    nwn = (pieceBB[BN] << uint64l[17]) & notH
    nww = (pieceBB[BN] << uint64l[10]) & notGH
    sww = (pieceBB[BN] >> uint64l[6]) & notGH
    sws = (pieceBB[BN] >> uint64l[15]) & notH
    return (nen | nee | see | ses | nwn | nww | sww | sws) & emptyBB



def white_knight_moves():
    nen = (pieceBB[WN] << uint64l[15]) & notA
    nee = (pieceBB[WN] << uint64l[6]) & notAB
    see = (pieceBB[WN] >> uint64l[10]) & notAB
    ses = (pieceBB[WN] >> uint64l[17]) & notA
    nwn = (pieceBB[WN] << uint64l[17]) & notH
    nww = (pieceBB[WN] << uint64l[10]) & notGH
    sww = (pieceBB[WN] >> uint64l[6]) & notGH
    sws = (pieceBB[WN] >> uint64l[15]) & notH
    return (nen | nee | see | ses | nwn | nww | sww | sws) & emptyBB

def evaluate(state):
    pc = state.piece_counts
    matvalue = piece_value[WP] * (pc[BP] - pc[WP]) +\
               piece_value[WN] * (pc[BN] - pc[WN]) +\
               piece_value[WB] * (pc[BB] - pc[WB]) +\
               piece_value[WR] * (pc[BR] - pc[WR]) +\
               piece_value[WQ] * (pc[BQ] - pc[WQ]) +\
               piece_value[WK] * (pc[BK] - pc[WK])
    mobvalue = 0
    for piece, indices in state.piece_indices.items():
        color = 1
        if piece & 1 == 0:
            color = -1
        for index in indices:
            mobvalue += square_value[piece][index] * color
    return matvalue + mobvalue
           

  

def alpha_beta_max(alpha, beta, depth, state, move=None):
    if depth == 0:
        return evaluate(state) #+ evaluate_move(state, move)
    moves = state.get_moves(BLACK)
    for move in moves:
        state.make_move(move)
        score = alpha_beta_min(alpha, beta, depth-1, state, move)
        state.unmake_move(move)
        if score >= beta:         
            return beta
        if score > alpha:
            
            
            if depth == 4:
                state.best_black = move
                state.print_board()
                print move
            alpha = score  
    return alpha
    
def alpha_beta_min(alpha, beta, depth, state, move=None):
    if depth == 0:
        return -(evaluate(state)) # + evaluate_move(state, move))
    moves = state.get_moves(WHITE)
    for move in moves:
        state.make_move(move)
        score = alpha_beta_max(alpha, beta, depth-1, state, move)
        state.unmake_move(move)
        if score <= alpha:
            return alpha
        if score < beta:
            beta = score
    
    return beta

class Engine:
    def __init__(self):
        self.board = Board()
        self.turn = WHITE

    def move(self, from_sq, to_sq):
        """the function called from UI"""
        piece = self.board.piece_at(from_sq)
        color = piece & 1 ^ 1
        tgt = self.board.piece_at(to_sq)
        #if there is a piece at the source square
        if piece != EMPTY:
            #check the piece type
            if piece == WP+color:
                to_squares = get_indices(legit_pawn_moves(self.board, from_sq, color))
            elif piece == WN+color:
                to_squares = get_indices(legit_knight_moves(self.board, from_sq, color))
            elif piece == WB+color:
                to_squares = get_indices(legit_bishop_moves(self.board, from_sq, color))
            elif piece == WR+color:
                to_squares = get_indices(legit_rook_moves(self.board, from_sq, color))
            elif piece == WQ+color:
                to_squares = get_indices(legit_queen_moves(self.board, from_sq, color))
            elif piece == WK+color:
                to_squares = get_indices(legit_king_moves(self.board, from_sq, color))
            else:
                to_squares = [] 
            #if the move is legit for this piece type
            if to_sq in to_squares:
                #finally define the type of the move
                if tgt != EMPTY:
                    tgtcolor = tgt & 1 ^ 1
                    self.board.make_move(CapturingMove(from_sq, to_sq, piece, color, tgt, tgtcolor))
                else:
                    self.board.make_move(QuietMove(from_sq, to_sq, piece, color))
                self.turn ^= 1
    def AI_move(self, depth = 4, color = BLACK):
        """let the computer do the move for the desired color"""
##        for move in self.board.get_moves(BLACK):
##            print move, evaluate_move(self.board, move)
        if depth % 2 != 0: depth -= 1
        if color == BLACK:
            b = alpha_beta_max(-10000, 10000, depth, self.board)
            print self.board.best_black
            self.p()
            print self.board.piece_indices
        self.board.make_move(self.board.best_black)
        self.turn ^= 1
        
    def p(self):
        self.board.print_board()

