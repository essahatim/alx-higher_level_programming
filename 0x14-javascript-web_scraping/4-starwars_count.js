#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: Status code ${response.statusCode}`);
  }

  let i = 0;

  JSON.parse(body).results.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${'18'}/`)) {
      i++;
    }
  });

  console.log(i);
});
