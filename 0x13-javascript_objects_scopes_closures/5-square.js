#!/usr/bin/node
// first export the previous class
const Rectangle = require('./4-rectangle');

// then let Square inherit from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
