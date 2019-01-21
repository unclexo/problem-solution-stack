from random import randrange
from ArrayStack import ArrayStack


def reverse_file(filename):
    """ Overwrites given file with its content line-by-line reversed """
    s = ArrayStack()
    original = open(filename)
    for line in original:
        s.push(line.rstrip('\n'))
    original.close()

    new_filename = 'new_{}.txt'.format(randrange(0, 100, 2))
    output = open(new_filename, 'w')
    while not s.isEmpty():
        output.write(s.pop() + '\n')
    output.close()


def main():
    reverse_file('file.txt')


if __name__ == '__main__':
    main()