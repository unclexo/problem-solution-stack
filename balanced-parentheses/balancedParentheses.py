from ArrayStack import ArrayStack


def is_matched(expr):
    """ Returns true if the arithmatic express is true, false otherwise """
    left = '({['
    right = ')}]'
    s = ArrayStack()
    for c in expr:
        if c in left:
            s.push(c)
        elif c in right:
            if s.is_empty():
                return False
            if right.index(c) != left.index(s.pop()):
                return False
    return s.is_empty()


def main():
    expr = '[(3-4)+(x+6)]'
    print(is_matched(expr))


if __name__ == '__main__':
    main()
