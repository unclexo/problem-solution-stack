def permute(s):
    permutations = []

    if len(s) == 1:
        return [s]

    # permute every letter in string one by one
    # i.e. for 'abc' first a then b and then c
    for i, letter in enumerate(s):
        
        # Don't repeat yourself. For example (i.e. 'aa', 'bbb')
        # if s.index(letter) != i:
        #    continue

        for permutation in permute(s[:i] + s[i+1:]):
            permutations += [letter + permutation]
    return permutations


def main():
    print(permute('abc'))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


if __name__ == '__main__':
    main()


