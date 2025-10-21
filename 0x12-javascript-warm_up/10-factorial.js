#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0]);

function fact (a) {
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(fact(args[0]));
}
