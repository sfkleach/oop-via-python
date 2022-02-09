from _collections_abc import MutableSequence

class Freezable(MutableSequence):

    def __init__(self, lst, frozen=False):
        self._list = list(lst)
        self._frozen = frozen

    def freeze(self):
        self._frozen = True

    def thaw(self):
        self._frozen = False

    def __getitem__(self, n):
        return self._list.__getitem__(n)

    def __len__(self):
        return self._list.__len__()

    def _raise_frozen(self):
        raise Exception(f'Trying to update a frozen list')

    def __setitem__(self, n, x):
        if self._frozen:
            self._raise_frozen()
        self._list.__setitem__(n, x)

    def __delitem__(self, n):
        if self._frozen:
            self._raise_frozen()
        self._list.__delitem__(n)

    def insert(self, index, value):
        if self._frozen:
            self._raise_frozen()
        self._list.insert(index, value)
