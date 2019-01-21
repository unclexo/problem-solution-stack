/**
 * Write a function that takes an integer N and
 * returns a NxN spiral matrix
 * 
 * Example: matrix(2)
 * [
 * 	[1, 2]
 * 	[4, 3]
 * ]
 * 
 * @param {Integer} n 
 * 
 * @returns {Array}
 */

function matrix(n) {

	const results = [];

	for (let i = 0; i < n; i++) {
		results[i] = [];
	}

	let counter = 1,
		startRow = 0,
		endRow = n - 1,
		startColumn = 0,
		endColumn = n - 1;

	while (startColumn <= endColumn && startRow <= endRow) {

		for (let i = startColumn; i <= endColumn; i++) {
			results[startRow][i] = counter;
			counter++;
		}

		startRow++;

		for (let i = startRow; i <= endRow; i++) {
			results[i][endColumn] = counter;
			counter++;
		}

		endColumn--;

		for (let i = endColumn; i >= startColumn; i--) {
			results[endRow][i] = counter;
			counter++;
		}

		endRow--;

		for (let i = endRow; i >= startRow; i--) {
			results[i][startColumn] = counter;
			counter++;
		}

		startColumn++;
	}

	return results;
}

console.log(matrix(3));