#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].unshift(userId);
}

console.log(newDict);
