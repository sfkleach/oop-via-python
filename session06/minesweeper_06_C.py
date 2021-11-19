'''
Minesweeper game.
 
    There is an n by m grid that has a random number of between 20% to 60%
    of randomly hidden mines that need to be found. 
 
    Positions in the grid are modified by entering their coordinates
    where the first coordinate is horizontal in the grid and the second
    vertical. The top left of the grid is position 1,1; the bottom right is
    at n,m.
 
    * The total number of mines to be found is shown at the beginning of the
    game.
    * Each mine occupies a single grid point, and its position is initially
    unknown to the player
    * The grid is shown as a rectangle of characters between moves.
    * You are initially shown all grids as obscured, by a single dot '.'
    * You may mark what you think is the position of a mine which will show
    as a '?'
    * You can mark what you think is free space by entering its coordinates.
    :*  If the point is free space then it is cleared, as are any adjacent
    points that are also free space- this is repeated recursively for
    subsequent adjacent free points unless that point is marked as a mine
    or is a mine.
    ::*   Points marked as a mine show as a '?'.
    ::*   Other free points show as an integer count of the number of adjacent
    true mines in its immediate neighbourhood, or as a single space ' ' if the
    free point is not adjacent to any true mines.
    * Of course you loose if you try to clear space that starts on a mine.
    * You win when you have correctly identified all mines.
 
 
    When prompted you may:
        Toggle where you think a mine is at position x, y:
          m <x> <y>
        Clear the grid starting at position x, y (and print the result):
          c <x> <y>
        Print the grid so far:
          p
        Resign
          r
    Resigning will first show the grid with an 'N' for unfound true mines, a
    'Y' for found true mines and a '?' for where you marked clear space as a
    mine 
 
'''
 
from abc import abstractmethod
import random
from itertools import product
from pprint import pprint as pp

class Game:

    gridsize  = (6, 4)
    minerange = (0.2, 0.6)

    def __init__(self):
        self._xgrid = Game.gridsize[0]
        self._ygrid = Game.gridsize[1]
        minmines, maxmines = Game.minerange
        fullcount = self._xgrid * self._ygrid    
        minecount = random.randint(int(fullcount*minmines), int(fullcount*maxmines))
        self._mines = set(random.sample(tuple(self.all_grid_positions()), minecount))
        self._show = {xy:'.' for xy in self.all_grid_positions()}
        self._markedmines = set([])
    
    def all_grid_positions(self):
        for i in range(self._xgrid):
            for j in range(self._ygrid):
                yield (i, j)

    def printgrid(self):
        print( '\n'.join(self.gridline(y) for y in range(self._ygrid)) )

    def gridline(self, y):
        return ''.join(self._show[(x,y)] for x in range(self._xgrid))

    def resign(self):
        for m in self._mines:
            self._show[m] = 'Y' if m in self._markedmines else 'N'

    def finished(self):
        return self._mines == self._markedmines

    def lenMines(self):
        return len(self._mines)

    def countNearByMines(self, xy):
        x, y = xy
        return sum(
            1
            for xx in (x-1, x, x+1)
            for yy in (y-1, y, y+1)
            if (xx, yy) in self._mines 
        )

    def xychar(self, xy):
        xychar = str(self.countNearByMines(xy))
        if xychar == '0': 
            xychar = '.'
        return xychar
 
    def clear(self, xy, cleared=None):
        if cleared is None:
            cleared = set([])
        if xy in cleared:
            return
        x, y = xy
        if self._show[xy] == '.':
            self._show[xy] = self.xychar(xy)
            for xx in (x-1, x, x+1):
                for yy in (y-1, y, y+1):
                    xxyy = (xx, yy)
                    if ( xxyy != xy
                        and xxyy in self.all_grid_positions()
                        and xxyy not in self._mines 
                        and xxyy not in self._markedmines ):
                        self.clear(xxyy, cleared | set([xy]))

    def toggle(self, xy):
        if xy in self._markedmines:
            self._markedmines.remove(xy)
            self._show[xy] = '.'
        else:
            self._markedmines.add(xy)
            self._show[xy] = '?'

    def pick(self, xy):
        if xy in self._mines | self._markedmines:
            print( '\nKLABOOM!! You hit a mine.\n' )
            self.resign()
            self.printgrid()
            return False
        else:
            self.clear(xy)
            self.printgrid()
            return True
    
    def summary(self):
        got = len(self._mines.intersection(self._markedmines))
        missed = len(self._markedmines.difference(self._mines))
        n_mines = len(self._mines)
        print(f'\nYou got {got} and missed {missed} of the {n_mines} mines')

    def mark(self, *, x, y):
        self.toggle((x,y))

    def play2(self):
        print( __doc__ )
        print(f'\nThere are {self.lenMines()} true mines of fixed position in the grid\n')
        self.printgrid()
        while not self.finished():
            command = inputCommand()
            if command:
                if not command.do_command(self):
                    break
        self.summary()

def inputCommand():
    inp = input('m x y/c x y/p/r: ').strip().split()
    if inp[0] == 'm' and len(inp) == 3:
        return MarkCommand(*inp)
    elif inp[0] == 'p' and len(inp) == 1:
        return PrintCommand(*inp)
    elif inp[0] == 'c' and len(inp) == 3:
        return ChooseCommand(*inp)
    elif inp[0] == 'r' and len(inp) == 1:
        return ResignCommand(*inp)
    else:
        return None

class MarkCommand:
    def __init__(self, _, x, y):
        self._x = int(x) - 1
        self._y = int(y) - 1
    def do_command(self, game):
        game.mark(self, x=self._x, y=self._y)
        return True

class PrintCommand:
    def __init__(self, _):
        pass
    def do_command(self, game):
        game.printgrid()
        return True

class ChooseCommand:
    def __init__(self, _, x, y):
        self._x = int(x) - 1
        self._y = int(y) - 1
    def do_command(self, game):
        return game.pick((self._x, self._y))

class ResignCommand:
    def __init__(self, _):
        pass
    def do_command(self, game):
        print('\nResigning!\n')
        self.resign()
        self.printgrid()
        return False

def play():
    Game().play2()

if __name__ == "__main__":
    play()