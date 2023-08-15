#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

const a = process.argv[2] ? parseInt(process.argv[2]) : NaN;

console.log(factorial(a));
