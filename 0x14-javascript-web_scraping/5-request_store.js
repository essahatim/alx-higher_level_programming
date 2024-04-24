#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(`Content saved to ${process.argv[3]}`);
  });
});
