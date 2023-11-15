#!/usr/bin/node

const SquareO = require('./5-square.js');

class Square extends SquareO {
  charPrint (c) {
    let charac = c;
    let i;

    if (c === undefined) {
      charac = 'X';
    }

    for (i = 0; i < this.height; i++) {
      console.log(charac.repeat(this.width));
    }
  }
}

module.exports = Square;
