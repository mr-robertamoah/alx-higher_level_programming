#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Code: ', response.statusCode);
    return;
  }

  const todos = JSON.parse(body);
  const result = {};
  for (const index in todos) {
    const todo = todos[index];
    if (!todo.completed) continue;
    if (!Object.keys(result).includes(todo.userId)) result[todo.userId] = 0;
    result[todo.userId] += 1;
  }

  console.log(result);
});
