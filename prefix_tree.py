"""
In Minecraft, a chest has 27 slots, and a prefix tree of the English Scrabble dictionary only needs
a character for each of the 26 letters of the alphabet and one terminal character (e.g. *)

Chests can be stored within chests, so we can make a whole tree inside a single Minecraft block(!)
Actually, we need a way of traversing the tree, which will probably involve command blocks and
dispensers and stuff (I don't remember how Minecraft works)
"""

from typing import List


class PrefixFreeTree:

    def __init__(self, words):

        self.is_end = False
        if "" in words:
            self.is_end = True
            words.remove("")
        self.branches = []

        heads = set(map(lambda x: x[0], words))
        for head in heads:
            tails = list(map(lambda x: x[1:], filter(lambda x: x[0] == head, words)))
            self.branches.append((head, PrefixFreeTree(tails)))


def size(tree: PrefixFreeTree) -> int:
    return tree.is_end + sum(map(lambda x: size(x[1]), tree.branches))


def height(tree: PrefixFreeTree) -> int:
    if not tree.branches:
        return 0
    return max([1 + height(t) for _, t in tree.branches])


def has(tree: PrefixFreeTree, word: str) -> bool:
    if word == "":
        return tree.is_end

    head, tail = word[0], word[1:]
    for c, t in tree.branches:
        if c == head:
            return has(t, tail)
    return False


def strings(tree: PrefixFreeTree) -> List[str]:
    # TODO this is silly and can be cut down
    if tree.is_end:
        res = [""]
        missing = [[c+s for s in strings(t)] for c, t in tree.branches]
        for m in missing:
            res += m
        return res
    return [c+tail for c, t in tree.branches for tail in strings(t)]


def predict(tree: PrefixFreeTree) -> List[str]:
    ...


def subtree(tree: PrefixFreeTree) -> PrefixFreeTree:
    ...


def ptree_repr(tree: PrefixFreeTree) -> str:
    # TODO make nicer
    if tree.is_end:
        return '*' + repr(tree.branches)
    else:
        return repr(tree.branches)


PrefixFreeTree.__repr__ = ptree_repr


if __name__ == "__main__":
    wo = ["cat", "category", "categories", "catapult", "catholic", "cocoa", "dog", "dogma", "mouse", "tree", "trees"]
    # wo = ["a"]
    tr = PrefixFreeTree(wo)

    print(tr)
    print(size(tr))
    print(height(tr))
    print(strings(tr))
    print(has(tr, "cocoa"))
