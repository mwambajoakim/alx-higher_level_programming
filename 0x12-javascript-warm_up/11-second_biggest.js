#!/usr/bin/node
const args = process.argv.slice(2);
const num = args.map(Number);
const sorted = num.sort((a, b) => a - b);
let secondLargest = sorted[0];

if (num.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < sorted.length - 1; i++) {
    secondLargest = sorted[i];
  }
  console.log(secondLargest);
}
