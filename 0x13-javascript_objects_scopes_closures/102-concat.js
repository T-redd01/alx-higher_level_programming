#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const file1Cont = fs.readFile(args[0]);
const file2Cont = fs.readFile(args[1]);
const concated = file1Cont + file2Cont;

fs.writeFile(args[2], concated);
