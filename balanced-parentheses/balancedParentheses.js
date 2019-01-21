/**
 * Write a function that takes an arithmatic expression
 * as parameter and returns true on balanced parentheses,
 * false otherwise.
 * 
 * Example: '[(3-4)+(x+6)]', '[{(a+b) * (c/d)}]' etc.
 * 
 * @param {String} expr 
 * 
 * @return {Boolean}
 */

function is_matched(expr) {
  const left = '({[';
  const right = ')}]';
  const a = [];

  for (let c of expr) {
    if (left.indexOf(c) !== -1) {
      a.push(c);
    } else if (right.indexOf(c) !== -1) {
      if (a.length === 0) {
        return false;
      }

      if (right.indexOf(c) !== left.indexOf(a.pop())) {
        return false;
      }
    }
  }

  return a.length === 0;
}

const expr = '[(3-4)+(x+6)]';
console.log(is_matched(expr));