/**
 * Write a function that takes a parameter S
 * and returns all the permutations of S
 * 
 * Example: for 'abc' -
 * ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
 * 
 * @param {String} s
 * 
 * @returns {Array} 
 */

function permute(s) {
    let permutations = [];

    if (s.length === 1) {
        return s;
    }

    // permute every letter in string one by one 
    // i.e. for 'abc' first a then b and then c
    for (let i = 0; i < s.length; i++) {
        let letter = s[i];

        // Don't repeat yourself. For example, 'aa', 'bbb' etc
        // if (s.indexOf(letter) !== i) {
        //   continue;
        // }

        for (let permutation of permute(s.slice(0, i) + s.slice(i + 1))) {
            permutations.push(letter + permutation);
        }
    }

    return permutations;
}

console.log(permute('abc')); // ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']