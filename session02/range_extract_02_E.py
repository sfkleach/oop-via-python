# Alternative design using empty ranges.
# I have elected to make empty range have no start or finish.

from typing import List, Protocol, Iterable

class RangeOfPages:

    def __init__(self, start: int, length:int=1):
        if length >= 1:
            self._start: int = start
            self._stop: int = start + length
        elif length == 0:
            self._start = start
            self._stop = start
        else:
            raise Exception("Trying to construct a range of negative length")

    def is_empty(self) -> bool:
        return self._stop == self._start

    def start(self) -> int:
        if self.is_empty():
            raise IndexError("empty RangeOfPages has no start")
        return self._start

    def stop(self) -> int:
        if self.is_empty():
            raise IndexError("empty RangeOfPages has no end")
        return self._stop

    def finish(self) -> int:
        return self.stop() - 1

    def try_add(self, page: int) -> bool:
        if self.is_empty():
            # Can always add a page to an empty set. 
            # Alter the _start so that it is correctly positioned for this addition.
            self._start = page 
            self._stop = page   # It is still of 0-length at this point.
        is_next = page == self._stop
        if is_next:
            self._stop += 1
        return is_next

    def count(self) -> int:
        # Works even when empty.
        return self._stop - self._start

    def __iter__(self) -> Iterable[int]:
        # Works even when empty.
        return iter(range(self._start, self._stop))

    def str_parts(self) -> Iterable[str]:
        if self.count() <= 2:
            yield from map(str, self)
        else:
            yield f"{self.start()}-{self.finish()}"

def pages_to_ranges( pages_list: List[int] ) -> List[RangeOfPages]:
    sofar: List[RangeOfPages] = [ RangeOfPages(0, 0) ]
    for p in pages_list:
        if not sofar[-1].try_add(p):
            sofar.append(RangeOfPages(p))
    return sofar

def range_extract( pages_list: List[int] ) -> List[str]:
    return ','.join(p for r in pages_to_ranges(pages_list) for p in r.str_parts())

if __name__ == '__main__':
    for lst in [
        [],
        [-8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
        [0, 1, 2, 4, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39]
    ]:
        print( f"Pages  : {lst}" )
        print( f"Extract: {range_extract(lst)}" )