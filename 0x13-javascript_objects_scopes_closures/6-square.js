#!/usr/bin/node

// import the old square in task 5 and store in SquareOld
const SquareOld = require('./5-square');

// extend the SquareOld
class Square extends SquareOld {
  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
