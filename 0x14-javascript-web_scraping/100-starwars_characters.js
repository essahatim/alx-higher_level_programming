#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
    return;
  }
  const charactersUrls = JSON.parse(body).characters;

  charactersUrls.forEach(characterUrl => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.err('Error:', err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
