#!/usr/bin/node
const userArgs = process.argv.slice(2);
const show = parseInt(userArgs[0]);
const str = 'X';

if (!isNaN(show)) {
  for (let i = 0; i < show; i++) {
    console.log(str.repeat(show));
  }
} else console.log('Missing size');
