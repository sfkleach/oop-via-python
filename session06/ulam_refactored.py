# Step 1: Enclass
# Step 2: Move parameters into constructor
# Step 3: Extract is_prime
# Step 4: Extract calc_cell_str

from math import sqrt
 
class Ulam:

    def __init__(self, n, symbol='# ', start=1, space=None):
        self._n = n
        self._symbol = symbol
        self._start = start
        self._space = space

    def cell(self, x, y):
        d, y, x = 0, y - self._n//2, x - (self._n - 1)//2
        l = 2*max(abs(x), abs(y))
        d = (l*3 + x + y) if y >= x else (l - x - y)
        return (l - 1)**2 + d + self._start - 1

    def calc_is_prime(self):
        top = self._start + self._n*self._n + 1
        is_prime = [False,False,True] + [True,False]*(top//2)
        for x in range(3, 1 + int(sqrt(top))):
            if not is_prime[x]: continue
            for i in range(x*x, top, x*2):
                is_prime[i] = False   
        return is_prime

    def calc_cell_str(self):
        space = self._space
        symbol = self._symbol
        
        cell_str = lambda x, p: f(x) if p else space
        f = lambda _: symbol # how to show prime cells
    
        if space == None: space = ' ' * len(symbol)
    
        if not len(symbol): # print numbers instead
            max_str = len(str(self._n*self._n + self._start - 1))
            if space == None: space = '.' * max_str + ' '
            f = lambda x: ('%' + str(max_str) + 'd ')%x

        return cell_str

    def show_spiral(self):
        is_prime = self.calc_is_prime()
        cell_str = self.calc_cell_str()    
        for y in range(self._n):
            print(''.join(cell_str(v, is_prime[v]) for v in [self.cell(x, y) for x in range(self._n)]))
        print()
 
Ulam(10, symbol=u'♞', space=u'♘').show_spiral() # black are the primes
Ulam(9, symbol='', space=' - ').show_spiral()
# for filling giant terminals
#show_spiral(1001, symbol='*', start=42)