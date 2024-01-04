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
  let characters = []
  for (const j in film.characters) {
    const character = film.characters[j];
    request.get(character, (err, res, content) => {
      if (err) {
        console.log(err);
        return;
      }
      characters.push({name: JSON.parse(content).name, id: j + 1});
    });
  }
  console.log(characters)
  characters = characters.sort((a, b) => a.id - b.id)
  for (let i in characters) {
    console.log(characters[i].name)
  }
});
