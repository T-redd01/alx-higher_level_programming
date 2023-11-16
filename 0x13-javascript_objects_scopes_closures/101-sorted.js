#!/usr/bin/node

const dict = require('./101-data.js').dict;
let new_dict = {};
const keys = Object.keys(dict);

for (key in keys) {
  if (new_dict[dict[keys[key]]] === undefined) {
    new_dict[dict[keys[key]]] = [];
    new_dict[dict[keys[key]]].push(keys[key]);
  } else {
    new_dict[dict[keys[key]]].push(keys[key]);
    new_dict[dict[keys[key]]].sort();
  }
}

console.log(new_dict);
