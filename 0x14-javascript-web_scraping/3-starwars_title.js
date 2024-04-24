#!/usr/bin/node
const request = require('request');

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(`Error: Status code ${response.statusCode}`);
    return;
  }
  console.log(JSON.parse(body).title);
});
