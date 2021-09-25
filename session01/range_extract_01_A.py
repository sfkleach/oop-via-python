# Invents a new kind of object that will represent a
# contiguous set of N page-numbers.
class RangeOfPages:

    # This initialiser will run as part of calling
    #   RangeOfPages( start, length )
    def __init__(self, start, length=1):
        # We give the range two fields called _start and _stop.
        # The leading underscore is a hint to the read that these
        # fields are 'hidden' and only to be used inside the class
        # definition.
        self._start = start
        self._stop = start + length
 
    # It is not uncommon to have methods that have names very 
    # similar to the fields. But the methods are part of the 
    # public behaviour and the fields are part of the implementation.
    def start(self):
        return self._start

    # These methods are called using a different syntax from
    # the definition
    #   r = RangeOfPages(120, 4)
    #   s = r.stop()        <- this is how you call it.
    def stop(self):
        return self._stop
