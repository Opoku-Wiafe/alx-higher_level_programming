#!/usr/bin/node
const userArgs = process.argv.slice(2);
const argsLen = userArgs.length;

if (argsLen === 0) {
  console.log('No argument');
} else if (argsLen === 1) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
