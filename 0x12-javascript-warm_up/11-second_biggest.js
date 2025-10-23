#!/usr/bin/node
const args = process.argv.slice(2);
const num = args.map(Number);
let secondLargest = num[0];

if (num.length <= 1) {
  console.log(0);
} else {
  num.sort();
  for (let i = 0; i < num.length - 1; i++) {
    secondLargest = num[i];
  }
  console.log(secondLargest);
}
