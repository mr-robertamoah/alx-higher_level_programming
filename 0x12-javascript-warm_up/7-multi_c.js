#!/usr/bin/node
const myNum = process.argv[2] ? parseInt(process.argv[2]) : null;
if (myNum === null || isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
}
