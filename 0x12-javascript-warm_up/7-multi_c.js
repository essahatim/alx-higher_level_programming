#!/usr/bin/node

const x = parseInt(process.argv[2]);
let i = 0;

if (!isNaN(x)) {
  for (; i < x; i++) {
    console.log('C is fun');		  
  }
} else {
  console.log('Missing number of occurrences');
}
