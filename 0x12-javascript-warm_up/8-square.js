#!/usr/bin/node

const firstArg = process.argv[2];
const size = parseInt(firstArg);

if (!isNaN(size)) {
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
} else {
  console.log('Missing size');
}
