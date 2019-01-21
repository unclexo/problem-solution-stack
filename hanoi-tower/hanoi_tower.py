def tower(disc, a, b, c):
    if disc < 1:
        return
    tower(disc-1, a, c, b)
    print('Move disc {} from peg {} to peg {}'.format(disc, a, c))
    tower(disc-1, b, a, c)


def main():

    tower(3, 'A', 'B', 'C')


if __name__ == '__main__':
    main()
