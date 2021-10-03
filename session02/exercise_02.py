
# Exercise 02
#   * Extend RangeOfPages to support an empty range
#   * Hint: It should generate no strParts
#   * Question: What is the start() of an empty range? Should it be allowed?
#   * Stretch goal: Alter the algorithm to use the empty range
#   * Reflect on the different approaches

from typing import List, Protocol, Iterable

class TryAddable(Protocol):
    def try_add(self, page: int) -> bool:
        pass

class TryAddRefusnik:
    def try_add( self, page: int ) -> bool:
        return False

class RangeOfPages:

    def __init__(self: int, start: int, length:int=1):
        self._start: int = start
        self._stop: int = start + length
 
    def start(self) -> int:
        return self._start

    def finish(self) -> int:
        return self._stop - 1

    def stop(self) -> int:
        return self._stop

    def count(self) -> int:
        return self._stop - self._start

    def try_add(self, page: int) -> bool:
        is_next = page == self._stop
        if is_next:
            self._stop += 1
        return is_next

    def strParts(self) -> Iterable[str]:
        if self.count() <= 2:
            yield from map(str, range(self.start(), self.stop()))
        else:
            yield f"{self.start()}-{self.finish()}"

def pages_to_ranges( pages_list: List[int] ) -> List[RangeOfPages]:
    sofar: List[RangeOfPages] = []
    last_in_sofar: TryAddable = TryAddRefusnik()
    for p in pages_list:
        if not last_in_sofar.try_add(p):
            rng: RangeOfPages = RangeOfPages(p)
            last_in_sofar = rng
            sofar.append(rng)
    return sofar

def range_extract( pages_list: List[int] ) -> List[str]:
    return ','.join(p for r in pages_to_ranges(pages_list) for p in r.strParts())
