#!/usr/bin/node
const args = process.argv.slice(2);
const line = 'C is fun';
const numberTimes = parseInt(args[0]);

if (numberTimes) {
  for (let i = 0; i < numberTimes; i++) {
    console.log(line);
  }
} else {
  console.log('Missing number of occurrences');
}
