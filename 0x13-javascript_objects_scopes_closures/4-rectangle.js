#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
      if (w >= 1 && h >= 1) {
        this.width = w;
        this.height = h;
      }
    }
    print() {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
    rotate() {
        let temp = this.height;
        this.height = this.width;
        this.width = temp;
    }
    double() {
        let x = this.height * 2;
        let y = this.width * 2;
        this.height = x;
        this.width = y;
    }
  };
