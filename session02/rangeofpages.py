class RangeOfPages:

    def __init__(self, start, length=1):
        self._start = start
        self._stop = start + length
 
    def start(self):
        return self._start

    def finish(self):
        return self._stop - 1

    def stop(self):
        return self._stop

    def count(self):
        return self._stop - self._start

    def try_add(self, page):
        is_next = page == self._stop
        if is_next:
            self._stop += 1
        return is_next

    def __str__(self):
        if self.count() == 1:
            return str(self.start())
        elif self.count() == 2:
            return f"{self.start()},{self.finish()}"
        else:
            return f"{self.start()}-{self.finish()}"

def pages_to_ranges( L ):
    sofar = []
    for i in L:
        if not( sofar and sofar[-1].try_add(i) ):
            sofar.append(RangeOfPages(i))
    return sofar

def stringify( L ):
    return ','.join(map(str,L))

def range_extract( L ):
    return stringify(pages_to_ranges(L))


if __name__ == '__main__':
    for lst in [[-8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7,
                 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
                [0, 1, 2, 4, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39]]:
        print(range_extract(lst))
