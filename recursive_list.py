from typing import Union


class Rlist:
    """A recursive list consisting of a first element and the rest."""

    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest: Union['Rlist', 'EmptyList'] = empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest)


def extend_rlist(s1, s2):
    """Return an Rlist with the elements of s1 followed by those of s2."""
    if s1 is Rlist.empty:
        return s2
    else:
        return Rlist(s1.first, extend_rlist(s1.rest, s2))


def map_rlist(fn, s):
    if s is Rlist.empty:
        return s
    else:
        return Rlist(fn(s.first), map_rlist(fn, s.rest))


def filter_rlist(s, fn):
    if s is Rlist.empty:
        return s
    else:
        rest = filter_rlist(s.rest, fn)
        if fn(s.first):
            return Rlist(s.first, rest)
        else:
            return rest


def rlist_expression(s):
    """
    __repr__ of Rlist
    We can't write it inside the Rlist class because it requires a recursive call
    """
    if s.rest is Rlist.empty:
        rest = ''
    else:
        rest = ', ' + rlist_expression(s.rest)
    return f'Rlist({s.first}{rest})'


Rlist.__repr__ = rlist_expression


if __name__ == "__main__":
    lst = Rlist(3, Rlist(4, Rlist(5)))
    print(lst)
    print(extend_rlist(lst.rest, lst))
    print(map_rlist(lambda x: x**2, lst))
    print(filter_rlist(lst, lambda x: x % 2 == 1))
