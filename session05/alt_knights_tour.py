# Taken from http://rosettacode.org/wiki/Knight%27s_tour#Python
# Annotated as "Knights tour using Warnsdorffs algorithm"

from collections import deque
from itertools import count

# Copied from https://stackoverflow.com/questions/5384570/whats-the-shortest-way-to-count-the-number-of-items-in-a-generator-iterator/34404546#34404546
def ilen(it):
    """Calculates the length of an iterator"""
    # Make a stateful counting iterator
    counter = count()
    # zip it with the input iterator, then drain until input exhausted at C level
    deque(zip(it, counter), 0) # cnt must be second zip arg to avoid advancing too far
    # Since count 0 based, the next value is the count
    return next(counter)

class Board:

    def __init__(self, boardsize):
        self._boardsize = boardsize
        self._board = {(x,y):0 for x in range(boardsize) for y in range(boardsize)}

    def __getitem__(self, xy):
        return self._board[xy]

    def __setitem__(self, xy, n ):
        self._board[xy] = n

    def strcell(self, x, y):
        """Returns the contents of cell (x,y) or blank if the move# is 0"""
        cell = self._board[(x,y)]
        return '%2i' % cell if cell else '  '

    def __str__(self):
        r = range(self._boardsize)
        return '\n'.join(','.join(self.strcell(x, y) for x in r) for y in r)

    def chess2index(self, chess):
        """Convert Algebraic chess notation to internal index format"""
        chess = chess.strip().lower()
        x = ord(chess[0]) - ord('a')
        y = self._boardsize - int(chess[1:])
        return (x, y)

    def __len__(self):
        """Returns the number of squares on the board"""
        return self._boardsize ** 2

    _kmoves = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)) 

    def knightmoves(self, P, exclude):
        """Given a position P, it generates the available next positions that
        are a knight's move away, not previously visited AND does not include
        an excluded position.
        """
        Px, Py = P
        for x,y in Board._kmoves:
            x1 = Px + x
            y1 = Py + y
            if 0 <= x1 < self._boardsize:
                if 0 <= y1 < self._boardsize:
                    x1y1 = (x1, y1)
                    if not self._board[x1y1]:
                        if x1y1 != exclude:
                            yield x1y1

    def min_accessible(self, P):
        """Finds the next move that has the property that it has the minimum
        number of onwards moves.
        """
        sofar = ( len(Board._kmoves) + 1, None )
        for pos in self.knightmoves(P, None):
            n = ilen(self.knightmoves(pos, P))
            if n <= sofar[0]:
                sofar = (n, pos)
        return sofar[1]

    def knights_tour(self, start, _debug=False):
        """Calculates a knight's tour, stamping the move number into each
        square of the board as it progresses.
        """
        move = 1
        P = self.chess2index(start)
        self[P] = move
        move += 1
        if _debug:
            print(self)
        while move <= len(self):
            P = self.min_accessible(P)
            self[P] = move
            move += 1
            if _debug:
                print(self)
                input('\n%2i next: ' % move)
        return self._board.copy()

default_boardsize = 6

def knights_tour(start, boardsize=default_boardsize, _debug=False):
    """Given a boardsize and a starting xy-position, calculates a board 
    dict<position: (int,int), move_number: int> that corresponds to a knight's
    tour of that size chessboard. A move_number of 0 is treated as unassigned.
    """
    board = Board(boardsize)
    return board.knights_tour(start)

if __name__ == '__main__':
    while 1:
        boardsize = int(input('\nboardsize: '))
        if boardsize < 5:
            continue
        start = input('Start position: ')
        board = Board(boardsize)
        results = board.knights_tour(start, _debug=True)
        print(board)