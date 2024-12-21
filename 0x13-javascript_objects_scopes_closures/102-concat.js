#!/usr/bin/node

const file = process.argv.slice(2);

const fs = require('fs');

fs.writeFileSync(file[2], fs.readFileSync(file[0], 'utf-8') + fs.readFileSync(file[1], 'utf-8'));
