from typing import List
from typing_extensions import Protocol

class TryAddable(Protocol):
    def try_add(self, page: int) -> bool:
        pass

class RangeOfPages:

    def __init__(self, start, length=1):
        self._start = start
        self._stop = start + length
 
    def start(self):
        return self._start

    def stop(self):
        return self._stop

    def count(self):
        return self._stop - self._start

    def try_add(self, page):
        is_next = page == self._stop
        if is_next:
            self._stop += 1
        return is_next

class TryAddRefusnik:
    def try_add(self, page):
        return False

def pages_to_ranges( pages_list: List[int] ) -> List[RangeOfPages]:
    sofar: List[RangeOfPages] = []
    last_in_sofar: TryAddable = TryAddRefusnik()
    for p in pages_list:
        if not last_in_sofar.try_add(p):
            rng: RangeOfPages = RangeOfPages(p)
            last_in_sofar = rng
            sofar.append(rng)
    return sofar
