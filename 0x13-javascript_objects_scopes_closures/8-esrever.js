#!/usr/bin/node
exports.esrever = function (list) {
  const nList = [];
  for (let i = 0; i < list.length; i++) {
    nList.unshift(list[i]);
  }
  return nList;
};
