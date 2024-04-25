#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  let i = 0;

  JSON.parse(body).results.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${'18'}/`)) {
      i++;
    }
  });

  console.log(i);
});
