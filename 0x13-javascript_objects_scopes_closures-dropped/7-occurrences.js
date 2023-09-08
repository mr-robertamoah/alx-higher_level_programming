#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter((el) => el === searchElement).length;
};
