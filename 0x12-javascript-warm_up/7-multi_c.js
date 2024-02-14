#!/usr/bin/node
const userArgs = process.argv.slice(2);
const show = parseInt(userArgs[0]);

if (!isNaN(show)) {
  for (let i = 0; i < show; i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurrences');
