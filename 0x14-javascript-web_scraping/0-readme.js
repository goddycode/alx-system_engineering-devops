#!/usr/bin/node

const fs = require('fs').promises;

async function readAndPrintFile(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    process.stdout.write(data);
  } catch (err) {
    console.error('Error:', err.message);
    process.exit(1);
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: node read_file.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
readAndPrintFile(filePath);

