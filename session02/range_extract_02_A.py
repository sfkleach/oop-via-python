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

def pages_to_ranges( pages_list ):
    sofar = []
    last_in_sofar = None
    for p in pages_list:
        if not last_in_sofar or not last_in_sofar.try_add(p):
            last_in_sofar = RangeOfPages(p)
            sofar.append(last_in_sofar)
    return sofar
