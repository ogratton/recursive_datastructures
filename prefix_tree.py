from typing import List


class PrefixTree:

    class End(object):
        def __repr__(self):
            return "*"

    end = End()

    def __init__(self, words):

        self.is_end = False
        if "" in words:
            self.is_end = True
            words.remove("")
        self.branches = []

        heads = set(map(lambda x: x[0], words))
        for head in heads:
            tails = list(map(lambda x: x[1:], filter(lambda x: x[0] == head, words)))
            self.branches.append((head, PrefixTree(tails)))


def size(tree: PrefixTree) -> int:
    return tree.is_end + sum(map(lambda x: size(x[1]), tree.branches))


def height(tree: PrefixTree) -> int:
    if not tree.branches:
        return 0
    return max([1 + height(t) for _, t in tree.branches])


def has(tree: PrefixTree, word: str) -> bool:
    if word == "":
        return tree.is_end

    head, tail = word[0], word[1:]
    for c, t in tree.branches:
        if c == head:
            return has(t, tail)
    return False


def strings(tree: PrefixTree) -> List[str]:
    # TODO this is silly and can be cut down
    if tree.is_end:
        res = [""]
        missing = [[c+s for s in strings(t)] for c, t in tree.branches]
        for m in missing:
            res += m
        return res
    return [c+tail for c, t in tree.branches for tail in strings(t)]


def predict(tree: PrefixTree) -> List[str]:
    ...


def subtree(tree: PrefixTree) -> PrefixTree:
    ...


def ptree_repr(tree: PrefixTree) -> str:
    # TODO make nicer
    if tree.is_end:
        return repr(PrefixTree.end) + repr(tree.branches)
    else:
        return repr(tree.branches)


PrefixTree.__repr__ = ptree_repr


if __name__ == "__main__":
    wo = ["cat", "category", "categories", "catapult", "catholic", "cocoa", "dog", "dogma", "mouse", "tree", "trees"]
    # wo = ["a"]
    tr = PrefixTree(wo)

    print(tr)
    print(size(tr))
    print(height(tr))
    print(strings(tr))
    print(has(tr, "cocoa"))
