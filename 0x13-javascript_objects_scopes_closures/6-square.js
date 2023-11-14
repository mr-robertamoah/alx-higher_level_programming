#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
      return;
    }
    let a;
    for (let i = 0; i < this.width; i++) {
      a = '';
      for (let j = 0; j < this.width; j++) {
        a = x + String(c);
      }
      console.log(a);
    }
  }
}

module.exports = Square;
