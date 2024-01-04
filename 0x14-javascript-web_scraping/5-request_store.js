#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];
request(url)
  .on('error', err => {
    console.log(err);
  })
  .pipe(fs.createWriteStream(file));
