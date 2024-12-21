#!/usr/bin/node

exports.esrever = function (list) {
    const newArray = [];
    while (list.length > 0) {
      newArray.push(list.pop());
    }
    return (newArray);
  };
