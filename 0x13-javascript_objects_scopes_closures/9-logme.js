#!/usr/bin/node

const incr = (function () {
  let counter = 0;
  return function () {
    let num = counter;
    counter += 1;
    return num;
  }
}


exports.logMe = function (item) {
  console.log(incr() + ': ' + item);
}
