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


def strings(tree: PrefixTree) -> List[str]:
    # TODO broken
    if tree.is_end:
        missing = [[c+s for s in strings(t)] for c, t in tree.branches]
        if missing:
            print(missing)
        return [""]
    return [c+tail for c, t in tree.branches for tail in strings(t)]


def subtree(tree: PrefixTree) -> PrefixTree:
    ...


def has(tree: PrefixTree) -> bool:
    ...


def predict(tree: PrefixTree) -> List[str]:
    ...


def ptree_repr(tree: PrefixTree) -> str:
    # TODO make nicer
    if tree.is_end:
        return repr(PrefixTree.end) + repr(tree.branches)
    else:
        return repr(tree.branches)


PrefixTree.__repr__ = ptree_repr


if __name__ == "__main__":
    wo = ["cat", "category", "categories", "catapult", "cocoa", "dog", "dogma", "mouse", "tree", "trees"]
    # wo = ["a"]
    tr = PrefixTree(wo)

    print(tr)
    print(size(tr))
    print(height(tr))
    print(strings(tr))
