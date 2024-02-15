#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // first lets initialize a counter to do the work
  let countChecker = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      countChecker++;
    }
  }
  return countChecker;
};
