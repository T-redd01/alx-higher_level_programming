#!/usr/bin/node

const args = process.argv.slice(2);
let num = parseInt(args[0], 10);

if (isNaN(num)) {
  console.log('Not a number');
} else {
	console.log('My number: ', num);
}