#!/usr/bin/node
class Rectangle {
  width;
  height;
  constructor (width, height) {
    if (typeof width !== 'number' || typeof height !== 'number' || width <= 0 || height <= 0) {
      return {};
    }
    this.width = width;
    this.height = height;
  }
}
module.exports = Rectangle;
