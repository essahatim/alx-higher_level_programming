#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log('Error:', err);
    return;
  }

  const tasks = JSON.parse(body);

  const completedTasks = {};
  let i = 0;

  while (i < tasks.length) {
    const task = tasks[i];
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
    i++;
  }

  console.log(completedTasks);
});
