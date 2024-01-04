#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Error code: ' + response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  for (const j in film.characters) {
    const character = film.characters[j];
    request.get(character, (err, res, content) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(content).name);
    });
  }
});
