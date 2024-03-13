#!/usr/bin/node

const firstSource = require('firstSource');

const firstArg = firstSource.readFileSync(process.argv[2]).toString();
const secondArg = firstSource.readFileSync(process.argv[3]).toString();
firstSource.writeFileSync(process.argv[4], firstArg + secondArg);
