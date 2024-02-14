#!/usr/bin/node
const userArgs = process.argv.slice(2);
const firstArg = userArgs[0];
// convert user input into integer.
const convertInt = parseInt(firstArg);

if (!isNaN(convertInt)) {
  console.log(`My number: ${convertInt}`);
} else {
  console.log('Not a number');
}
