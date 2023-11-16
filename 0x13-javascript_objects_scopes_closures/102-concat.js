#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
/*const file1Cont = fs.readFile(args[0], (err, data) => {
  if (err) {
    console.log(err);
  }
});
const file2Cont = fs.readFile(args[1], (err, data) => {
  if (err) {
    console.log(err)
  }
});
const concated = file1Cont + file2Cont;*/
let cont;
fs.readFileSync(args[0], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
	cont = data;
  }
});
console.log(cont);
//fs.writeFile(args[2], concated);
