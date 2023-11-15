#!/usr/bin/node

exports.logMe = function (item) {
  console.log(incr() + ': ' + item);
};

const incr = (function () {
  let counter = 0;
  return function () {
    let num = counter;
    counter += 1;
    return num;
  }
}) ();
