#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};
const keys = Object.keys(dict);
let key;

for (key in keys) {
  if (newDict[dict[keys[key]]] === undefined) {
    newDict[dict[keys[key]]] = [];
    newDict[dict[keys[key]]].push(keys[key]);
  } else {
    newDict[dict[keys[key]]].push(keys[key]);
    newDict[dict[keys[key]]].sort();
  }
}

console.log(newDict);
