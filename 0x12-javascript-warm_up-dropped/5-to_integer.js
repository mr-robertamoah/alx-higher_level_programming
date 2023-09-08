#!/usr/bin/node
const myNum = process.argv[2] ? parseInt(process.argv[2]) : null;
if (myNum === null || isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
