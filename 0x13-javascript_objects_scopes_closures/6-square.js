#!/usr/bin/node
const SquarePrev = require('./5-square');
class Square extends SquarePrev {
  charPrint (C) {
    if (C === undefined) {
      C = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(C.repeat(this.width));
    }
  }
}
module.exports = Square;
