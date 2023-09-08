#!/usr/bin/node
const myNum = process.argv[2] ? parseInt(process.argv[2]) : null;
if (myNum === null || isNaN(myNum)) {
  console.log('Missing size');
} else {
  let x;
  for (let i = 0; i < myNum; i++) {
    x = '';
    for (let i = 0; i < myNum; i++) {
      x = x + 'X';
    }
    console.log(x);
  }
}
