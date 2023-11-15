#!/usr/bin/node

const Square = require("./5-square.js");

class Square extends Square {
  charPrint (c) {
    let charac = c;
    let i;

    if (c === undefined) {
      charac = "X";
    }
	
    for (i = 0; i < this.height; i++) {
      console.log(charac.repeat(this.width);
    }
  }
}
