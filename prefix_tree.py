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


def size(tree: PrefixTree):
        return tree.is_end + sum(map(lambda x: size(x), tree.branches))


def height(tree: PrefixTree):
    ...


def strings(tree: PrefixTree):
    ...


def subtree(tree: PrefixTree):
    ...


def has(tree: PrefixTree):
    ...


def predict(tree: PrefixTree):
    ...


def ptree_repr(tree: PrefixTree):
    # TODO make nicer
    if tree.is_end:
        return repr(PrefixTree.end) + repr(tree.branches)
    else:
        return repr(tree.branches)


PrefixTree.__repr__ = ptree_repr


if __name__ == "__main__":
    w = ["cat", "category", "catapult", "cocoa", "dog", "dogma", "mouse", "tree"]
    t = PrefixTree(w)

    print(t)
