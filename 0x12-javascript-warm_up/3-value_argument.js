#!/usr/bin/node
const userArgs = process.argv.slice(2);
const firstArg = userArgs[0];

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
