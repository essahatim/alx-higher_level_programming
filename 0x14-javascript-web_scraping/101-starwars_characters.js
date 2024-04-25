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
  const fetchCharacter = (index) => {
    if (index === charactersUrls.length) {
      return;
    }

    const characterUrl = charactersUrls[index];
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.log('Error:', err);
        return;
      }
      console.log(JSON.parse(body).name);
      fetchCharacter(index + 1);
    });
  };

  fetchCharacter(0);
});

