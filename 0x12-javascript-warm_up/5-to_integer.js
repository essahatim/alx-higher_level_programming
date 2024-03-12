#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', number);
}
