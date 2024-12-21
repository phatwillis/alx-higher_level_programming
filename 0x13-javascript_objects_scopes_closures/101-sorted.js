#!/usr/bin/node

const dataDict = require('./101-data.js').dict;

const newDict = {};
for (const key in dataDict) {
  if (!(dataDict[key] in newDict)) {
    newDict[dataDict[key]] = [];
  }
  newDict[dataDict[key]].push(key);
}
console.log(newDict);
