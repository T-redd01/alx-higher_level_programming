#!/usr/bin/node

function factorials (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }
  return (num * factorials(num - 1));
}

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

console.log(factorials(num));
