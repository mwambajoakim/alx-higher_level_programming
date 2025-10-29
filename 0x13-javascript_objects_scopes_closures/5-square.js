#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.width = 2 * this.width;
    this.width = 2 * this.width;
  }
}
module.exports = Square;
