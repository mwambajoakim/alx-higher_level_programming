#!/usr/bin/node
const args = process.argv.slice(2);
const size = parseInt(args[0]);

if (size) {
  for (let i = 0; i < size; i++) {
    console.log('x'.repeat(size));
  }
} else {
  console.log('Missing size');
}
