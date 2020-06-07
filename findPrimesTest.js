'use strict';
var findPrimes = require('./findPrimes');


let max = parseInt(process.argv[2]);
let primeNumbers = findPrimes(max);
console.log(primeNumbers.length);
