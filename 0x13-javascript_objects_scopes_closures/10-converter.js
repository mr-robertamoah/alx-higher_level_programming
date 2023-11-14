#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    return parseInt(num, 10).toString(base);
  };
};
