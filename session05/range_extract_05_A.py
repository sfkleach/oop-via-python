def range_extract(lst):
    """Yield 2-tuple ranges or 1-tuple single elements from list of increasing ints"""
    lenlst = len(lst)
    i = 0
    while i < lenlst:
        low = lst[i]
        while i <lenlst-1 and lst[i]+1 == lst[i+1]: 
            i += 1
        hi = lst[i]
        if hi - low >= 2:
            yield (low, hi)
        elif hi - low == 1:
            yield (low,)
            yield (hi,)
        else:
            yield (low,)
        i += 1
 
def stringr(ranges):
    return ','.join( (('%i-%i' % r) if len(r) == 2 else '%i' % r) for r in ranges )

def pages_to_ranges_string(pages):
    return stringr(range_extract(pages))
