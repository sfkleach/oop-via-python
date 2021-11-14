class Range:
 
    def __init__(self, low, hi):
        self._low = low
        self._high = hi + 1
 
    @staticmethod
    def makeRanges(low, hi):
        if hi - low == 1:
            yield Range(low, low)
            yield Range(hi, hi)
        else:
            yield Range(low, hi)

    def __len__(self):
        return self._high - self._low

    def __str__(self):
        if len(self) == 1:
            return f'{self._low}'
        else:
            return f'{self._low}-{self._high-1}'
 
class Cursor:
    def __init__(self, lst):
        self._lenlst = len(lst)
        self._i = 0
        self._lst = lst
    def bump(self):
        self._i += 1
    def __bool__(self):
        return self._i < self._lenlst
    def current(self):
        return self._lst[self._i]
    def hasNext(self):
        return self._i + 1 < self._lenlst
    def next(self):
        return self._lst[self._i + 1]
 
class IntervalFinder(Cursor):
 
    def __init__(self, lst):
        super().__init__(lst)
 
    def advance(self):
        while self.hasNext() and self.current() + 1 == self.next():
            self.bump()
 
    def findBoundsAndBump(self):
        low = self.current()
        self.advance()
        hi = self.current()
        self.bump()
        return (low, hi)
 
class RangeExtractor:
 
    def __init__(self, lst):
        self._cursor = IntervalFinder(lst)
 
    def rangeExtract(self):
        while self._cursor:
            (low, hi) = self._cursor.findBoundsAndBump()
            yield from Range.makeRanges(low, hi)
 
def range_extract(lst):
    return RangeExtractor(lst).rangeExtract()

def pages_to_ranges_string(lst):
   return ','.join(map(str, range_extract(lst)))
