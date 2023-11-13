#!/usr/bin/node

const args = process.argv.slice(2);
let len = 0;
let i;

for (i in args) {
  len++;
  break;
}

if (len === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
