#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
      return;
    }
    let x;
    for (let i = 0; i < this.width; i++) {
      x = '';
      for (let j = 0; j < this.width; j++) {
        x = x + String(c);
      }
      console.log(x);
    }
  }
}

module.exports = Square;
