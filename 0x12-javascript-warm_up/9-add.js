#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const i = process.argv[2] ? parseInt(process.argv[2]) : NaN;
const j = process.argv[3] ? parseInt(process.argv[3]) : NaN;

add(i, j);
