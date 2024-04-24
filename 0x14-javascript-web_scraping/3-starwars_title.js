#!/usr/bin/node
const request = require('request');

const api_Url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(api_Url, (err, response, body) => {
  if (err) {
    console.err(err);
  }
  if (response.statusCode !== 200) {
    console.err(`Error: Status code ${response.statusCode}`);
  }
  console.log(JSON.parse(body).title);
});
