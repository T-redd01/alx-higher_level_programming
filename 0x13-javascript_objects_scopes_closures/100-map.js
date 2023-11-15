#!/usr/bin/node

const list = require("./100-data.js");
const newList = list.map(myFunc);

function myFunc (num, index) {
  return num * index;
}

console.log(list);
console.log(newList);
