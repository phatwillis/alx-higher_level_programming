#!/usr/bin/node

const squareParent = require('./5-square');
module.exports = class Square extends squareParent {
  charPrint(c) {
    if (c === undefined) {
        c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
    } 
  }
};
