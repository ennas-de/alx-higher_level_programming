#!/usr/bin/node

const esrever = function(list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};

modules.exports = {
  esrever
}