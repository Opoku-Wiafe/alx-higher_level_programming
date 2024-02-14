#!/usr/bin/node
const { argv } = require('process');
const checkValue = parseInt(argv[2], 10);
function factorial (checkValue) {
  if (checkValue <= 1) return 1;
  return checkValue * factorial(checkValue - 1);
}
if (isNaN(checkValue)) console.log(1);
else console.log(factorial(checkValue));
// n * (n-1) * (n-2) ... (1) formula for fact.
