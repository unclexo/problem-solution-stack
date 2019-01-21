/**
 * Write a function that takes a parameter N
 * and returns the number of primes in N
 * 
 * @param {Integer} n 
 * 
 * @returns {Integer}
 */

function prime(n) {
	// Creates an empty array
	primes = [];

	// Stores temporarily all numbers as prime
	for (let i = 0; i < n + 1; i++) {
		primes[i] = true;
	}

	// Makes 0 and 1 False as they are not prime number
	primes[0] = primes[1] = false;

	// Sieves all prime numbers
	// Sets false to those are not prime numbers
	for (let i = 2; i * i < n; i++) {
		if (primes[i]) {
			for (let j = i; j * i < n + 1; j++) {
				primes[j * i] = false;
			}
		}
	}

	// Counts prime numbers
	countPrimes = 0;
	for (let k = 0; k < primes.length; k++) {
		if (primes[k]) countPrimes++;
	}

	// Returns the counted numbers
	return countPrimes;
}

console.log(prime(50));