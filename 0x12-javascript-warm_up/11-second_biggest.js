#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 3) {
  console.log('0');
} else {
  const second = args.sort((a, b) => b - a);
  console.log(second[1]);
}

