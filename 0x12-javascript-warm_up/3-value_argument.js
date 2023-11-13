#!/usr/bin/node

const args = process.argv.slice(2);
let len = 0;

for (len in args) {
  if (len === 0) {
    break;
  }
}

if (len === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
