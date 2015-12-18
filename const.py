from numpy import uint64

"""all the uint64's here exist due to slowness of making new instance
   every time """
uint64l = []
for i in range(64):
    uint64l.append(uint64(i))

notA = uint64(0b0111111101111111011111110111111101111111011111110111111101111111)
notAB = uint64(0b0011111100111111001111110011111100111111001111110011111100111111)
notH = uint64(0b1111111011111110111111101111111011111110111111101111111011111110)
notGH = uint64(0b1111110011111100111111001111110011111100111111001111110011111100)
rank5 = uint64(0xff00000000)
rank4 = uint64(0xff000000)
debruijn64 = uint64(0x03f79d71b4cb0a89)

EMPTY = 2
WHITE = 0
WP = 3
WB = 5
WN = 7
WR = 9
WQ = 11
WK = 13
BLACK = 1
BP = 4
BB = 6
BN = 8
BR = 10
BQ = 12
BK = 14

piece_shortcuts = {3: 'WP',
                   5: 'WB',
                   7: 'WN',
                   9: 'WR',
                   11: 'WQ',
                   13: 'WK',
                   4: 'BP',
                   6: 'BB',
                   8: 'BN',
                   10: 'BR',
                   12: 'BQ',
                   14: 'BK'}

piece_names = {3: 'White pawn',
               5: 'White bishop',
               7: 'White knight',
               9: 'White rook',
               11: 'White queen',
               13: 'White king',
               4: 'Black pawn',
               6: 'Black bishop',
               8: 'Black knight',
               10: 'Black rook',
               12: 'Black queen',
               14: 'Black king'}

"""
http://chessprogramming.wikispaces.com/BitScan#Bitscan%20forward-De%20Bruijn%20Multiplication
A 64-bit De Bruijn sequence contains 64-overlapped unique 6-bit sequences,
thus a circle of 64 bits, where five leading zeros overlap five hidden
"trailing" zeros. There are 226 = 67108864 odd sequences with 6 leading
binary zeros and 226 even sequences with 5 leading binary zeros, which
may be calculated from the odd ones by shifting left one.
"""
index64 = [
    0,  1, 48,  2, 57, 49, 28,  3,
    61, 58, 50, 42, 38, 29, 17,  4,
    62, 55, 59, 36, 53, 51, 43, 22,
    45, 39, 33, 30, 24, 18, 12,  5,
    63, 47, 56, 27, 60, 41, 37, 16,
    54, 35, 52, 21, 44, 32, 23, 11,
    46, 26, 40, 15, 34, 20, 31, 10,
    25, 14, 19,  9, 13,  8,  7,  6]

index64r = [
    0, 47,  1, 56, 48, 27,  2, 60,
    57, 49, 41, 37, 28, 16,  3, 61,
    54, 58, 35, 52, 50, 42, 21, 44,
    38, 32, 29, 23, 17, 11,  4, 62,
    46, 55, 26, 59, 40, 36, 15, 53,
    34, 51, 20, 43, 31, 22, 10, 45,
    25, 39, 14, 33, 19, 30,  9, 24,
    13, 18,  8, 12,  7,  6,  5, 63]
