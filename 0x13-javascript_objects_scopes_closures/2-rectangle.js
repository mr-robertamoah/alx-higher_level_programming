#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    w = parseInt(w);
    h = parseInt(h);

    if ((!isNaN(w) && w > 0) && (!isNaN(h) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
