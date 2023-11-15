#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ocs = 0;
  let i;

  for (i in list) {
    if (list[i] === searchElement) {
      ocs++;
    }
  }
  return ocs;
};
