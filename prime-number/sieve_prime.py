import math


def prime(n):
    """ Returns the number of primes from the given number """
    # Creates a list with values of True
    primes = [True] * (n + 1)

    # Makes 0 and 1 False as they are not prime number
    primes[0] = primes[1] = False

    # Sieves all primes numbers
    # Sets False to those are not primes
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False

    count_primes = 0
    for p in primes:
        if p:
            count_primes += 1

    return count_primes


def main():
    print(prime(50))


if __name__ == '__main__':
    main()
