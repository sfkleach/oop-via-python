from __future__ import annotations
from typing import Iterable, List

class RangeOfPages:
    
    def __init__(self, start, length):
        if length < 1:
            raise ValueError("trying to construct RangeOfPages with non-positive length")
        self._start = start
        self._length = length

    def low(self):
        return self._start
    
    def high(self):
        return self._start + self._length - 1

    def __iter__(self):
        return iter(range(self._start, self._start + self._length))

    def strParts(self) -> Iterable[str]:
        if self._length <= 2:
            yield from map(str, self)
        else:
            yield f"{self.low()}-{self.high()}"

class RangeOfPagesBuilder:

    def __init__(self, page=None):
        self._start = None if page is None else page
        self._length = 0 if page is None else 1

    def is_empty(self):
        return self._length == 0
    
    def try_add(self, page: int) -> bool:
        if self.is_empty():
            self._start = page            
        is_next = self._start + self._length == page
        if is_next:
            self._length += 1
        return is_next
    
    def newRangeOfPages(self) -> RangeOfPages:
        "Will raise RuntimeError if no pages have been added"
        if self.is_empty():
            raise ValueError("no pages were added")
        else:
            return RangeOfPages(self._start, self._length)

class ExtractBuilder:
    
    def __init__(self):
        self._rpbuilder = RangeOfPagesBuilder()
        self._extract_sofar = []

    def _flush(self):
        self._extract_sofar.append(self._rpbuilder.newRangeOfPages())

    def add(self, page: int):
        if not self._rpbuilder.try_add(page):
            self._flush()
            self._rpbuilder = RangeOfPagesBuilder(page)

    def add_all(self, pages: Iterable[int]):
        for p in pages:
            self.add( p )

    def newExtract(self) -> List[RangeOfPages]:
        try:
            self._flush()
        except ValueError:
            pass
        L = self._extract_sofar
        self._extract_sofar = []
        return L 

def range_extract( pages_list: List[int] ) -> List[str]:
    ex_builder = ExtractBuilder()
    ex_builder.add_all(pages_list)
    ranges = ex_builder.newExtract()
    return ','.join(p for r in ranges for p in r.strParts())

if __name__ == '__main__':
    for lst in [
        [],
        [-8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
        [0, 1, 2, 4, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39]
    ]:
        print( f"Pages  : {lst}" )
        print( f"Extract: {range_extract(lst)}" )
