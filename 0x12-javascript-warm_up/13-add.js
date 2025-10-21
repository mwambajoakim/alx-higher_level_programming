#!/usr/bin/node
exports.add = function add (a, b) {
  return a + b;
};

const add = require('./13-add').add;
console.log(add(3, 5));
