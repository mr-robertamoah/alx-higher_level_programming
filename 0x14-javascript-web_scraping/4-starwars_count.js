#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Error code: ' + response.statusCode);
    return;
  }

  console.log(JSON.parse(body).results.filter(res => {
    return res.characters.includes(character);
  }).length);
});
