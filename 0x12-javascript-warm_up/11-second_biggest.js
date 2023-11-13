#!/usr/bin/node

const args = process.argv.slice(2);
let max = 0;
let sec = 0;
let i;

for (i in args) {
  args[i] = parseInt(args[i], 10);
  if (args[i] > max) {
    max = args[i];
  }
}

if (args.length < 2) {
  console.log(0);
} else {
  for (i = 0; i < args.length; i++) {
    if (args[i] > sec && args[i] < max) {
      sec = args[i];
    }
  }
  console.log(sec);
}
