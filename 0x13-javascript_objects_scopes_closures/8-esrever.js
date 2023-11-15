#!/usr/bin/node

exports.esrever = function (list) {
  const halflen = list.length / 2;
  let i = 0;
  let j = list.length - 1;
  let tmp;

  while (i < halflen) {
    tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
    i++;
    j--;
  }
  return list;
};
