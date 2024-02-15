#!/usr/bin/node

exports.esrever = function (list) {
  const _reverse = [];
  for (const ele of list) {
    _reverse.unshift(ele);
  }
  return _reverse;
};
