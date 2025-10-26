#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (typeof width !== 'number' || typeof height !== 'number' || width <= 0 || height <= 0) {
      return;
    }
    this.width = width;
    this.height = height;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
