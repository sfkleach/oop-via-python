from _collections_abc import Sequence, MutableSequence

class Freezable(MutableSequence):

    def __init__(self, lst, frozen=False, inextensible=False):
        self._list = list(lst)
        self._frozen = Frozen(self)
        self._liquid = Liquid(self)
        self._inextensible = Inextensible(self)
        self._state = self._frozen if frozen else self._liquid

    def freeze(self):
        self._state = self._frozen

    def thaw(self, inextensible=False):
        self._state = self._inextensible if inextensible else self._liquid

    def __getitem__(self, n):
        return self._state.__getitem__(n)

    def __len__(self):
        return self._state.__len__()

    def __setitem__(self, n, x):
        self._state.__setitem__(n, x)

    def __delitem__(self, n):
        self._state.__delitem__(n)

    def insert(self, index, value):
        self._state.insert(index, value)

class AbsFreezableState(Sequence):

    def __getitem__(self, n):
        return self._list.__getitem__(n)

    def __len__(self):
        return self._list.__len__()   

class Frozen( AbsFreezableState, Sequence ):

    def __init__(self, context):
        self._list = context._list

class Liquid( AbsFreezableState, MutableSequence ):

    def __init__(self, context):
        self._list = context._list

    def __setitem__(self, n, x):
        self._list.__setitem__(n, x)

    def __delitem__(self, n):
        self._list.__delitem__(n)

    def insert(self, index, value):
        self._list.insert(index, value)

class Inextensible( AbsFreezableState, MutableSequence ):

    def __init__(self, context):
        self._list = context._list

    def __setitem__(self, n, x):
        self._list.__setitem__(n, x)

    def __delitem__(self, n):
        raise Exception(f'Trying to delete from an inextensible list')

    def insert(self, index, value):
        raise Exception(f'Trying to extend an inextensible list')
