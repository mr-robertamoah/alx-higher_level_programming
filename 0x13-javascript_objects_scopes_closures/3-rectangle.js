#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    w = parseInt(w);
    h = parseInt(h);

    if (!isNaN(w) && w > 0 && !isNaN(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    for (let i = 0; i < this.h; i++) {
      x = '';
      for (let j = 0; j < this.w; j++) {
        x = x + 'X';
      }
      console.log(x);
    }
  }
}

module.exports = Rectangle;
