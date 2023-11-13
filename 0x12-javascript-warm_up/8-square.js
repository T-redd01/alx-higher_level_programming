#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0], 10);
let i = 0;

if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (i < num) {
    console.log('X'.repeat(num));
    i++;
  }
}
