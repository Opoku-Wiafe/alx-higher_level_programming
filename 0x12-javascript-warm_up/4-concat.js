#!/usr/bin/node
const userArgs = process.argv.slice(2);
const firstArg = userArgs[0];
const secondArg = userArgs[1];
// print condition using coalescing (??) and ($) accept input

console.log(`${firstArg ?? 'undefined'} is ${secondArg ?? 'undefined'}`);
