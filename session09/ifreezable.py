from _collections_abc import MutableSequence

class Freezable(MutableSequence):

    def __init__(self, lst, frozen=False, inextensible=False):
        self._list = list(lst)
        self._frozen = frozen
        self._inextensible = inextensible

    def freeze(self):
        self._frozen = True

    def thaw(self, inextensible=False):
        self._frozen = False
        self._inextensible = inextensible

    def __getitem__(self, n):
        return self._list.__getitem__(n)

    def __len__(self):
        return self._list.__len__()

    def _raise_frozen(self):
        raise Exception(f'Trying to update a frozen list')

    def _raise_inextensible(self):
        raise Exception(f'Trying to extend an inextensible list')

    def __setitem__(self, n, x):
        if self._frozen:
            self._raise_frozen()
        self._list.__setitem__(n, x)

    def __delitem__(self, n):
        if self._frozen:
            self._raise_frozen()
        elif self._inextensible:
            self._raise_inextensible()
        self._list.__delitem__(n)

    def insert(self, index, value):
        if self._frozen:
            self._raise_frozen()
        elif self._inextensible:
            self._raise_inextensible()
        self._list.insert(index, value)
