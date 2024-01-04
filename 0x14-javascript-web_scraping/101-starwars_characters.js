#!/usr/bin/node

const request = require('request');

function getCharacterName (character) {
  return new Promise((resolve, reject) => {
    request.get(character, (err, res, content) => {
      if (err) {
        reject(err);
      }
      resolve(JSON.parse(content).name);
    });
  });
}

async function getFilmNames (url) {
  try {
    const film = await new Promise((resolve, reject) => {
      request(url, (err, response, body) => {
        if (err) {
          reject(err);
          return;
        }

        if (response.statusCode !== 200) {
          reject(new Error('Error code: ' + response.statusCode));
          return;
        }

        resolve(JSON.parse(body));
      });
    });

    for (const j in film.characters) {
      const character = film.characters[j];
      const name = await getCharacterName(character);
      console.log(name);
    }
  } catch (err) {
    console.log(err);
  }
}

getFilmNames('https://swapi-api.alx-tools.com/api/films/' + process.argv[2]);
