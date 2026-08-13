#!/usr/bin/env node

import { existsSync } from "node:fs";
import { rename, rm } from "node:fs/promises";
import { createRequire } from "node:module";
import { extname, resolve } from "node:path";

const rawArguments = process.argv.slice(2);
const force = rawArguments.includes("--force");
const argumentsWithoutFlags = rawArguments.filter((argument) => argument !== "--force");

if (argumentsWithoutFlags.length !== 2) {
  fail("Usage: node create_review_sheet.mjs <preview.png> <review.png> [--force]");
}

const inputPath = resolve(argumentsWithoutFlags[0]);
const outputPath = resolve(argumentsWithoutFlags[1]);

if (extname(inputPath).toLowerCase() !== ".png") {
  fail("The preview must be a PNG file.");
}
if (extname(outputPath).toLowerCase() !== ".png") {
  fail("The review sheet must be a PNG file.");
}
if (!existsSync(inputPath)) {
  fail(`Preview does not exist: ${inputPath}`);
}
if (existsSync(outputPath) && !force) {
  fail(`Review sheet already exists: ${outputPath}. Pass --force only when replacement is intended.`);
}

const require = createRequire(import.meta.url);
let sharp;
try {
  sharp = require("sharp");
} catch {
  fail(
    "Sharp is unavailable. Locate the configured workspace Node packages and expose them through NODE_PATH; do not install dependencies without permission."
  );
}

const metadata = await sharp(inputPath).metadata();
if (metadata.width !== 1280 || metadata.height !== 640) {
  fail(`Preview must be exactly 1280x640; got ${metadata.width}x${metadata.height}.`);
}

const thumbnail = await sharp(inputPath)
  .resize(320, 160, { fit: "fill" })
  .png({ compressionLevel: 9 })
  .toBuffer();

const backdrop = Buffer.from(`
  <svg xmlns="http://www.w3.org/2000/svg" width="720" height="224" viewBox="0 0 720 224">
    <rect width="720" height="224" rx="16" fill="#d0d7de"/>
    <rect x="12" y="12" width="342" height="200" rx="12" fill="#ffffff"/>
    <rect x="366" y="12" width="342" height="200" rx="12" fill="#0d1117"/>
    <g font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="700" letter-spacing="1.5">
      <text x="22" y="31" fill="#57606a">LIGHT SURROUND</text>
      <text x="376" y="31" fill="#8c959f">DARK SURROUND</text>
    </g>
  </svg>
`);

const temporaryPath = `${outputPath}.tmp-${process.pid}.png`;

try {
  const result = await sharp(backdrop)
    .composite([
      { input: thumbnail, left: 22, top: 42 },
      { input: thumbnail, left: 376, top: 42 },
    ])
    .png({ compressionLevel: 9 })
    .toFile(temporaryPath);

  if (existsSync(outputPath)) {
    await rm(outputPath);
  }
  await rename(temporaryPath, outputPath);
  process.stdout.write(
    JSON.stringify({
      output: outputPath,
      width: result.width,
      height: result.height,
      previewWidth: 320,
      previewHeight: 160,
      bytes: result.size,
    }) + "\n"
  );
} catch (error) {
  if (existsSync(temporaryPath)) {
    await rm(temporaryPath, { force: true });
  }
  fail(error instanceof Error ? error.message : String(error));
}

function fail(message) {
  process.stderr.write(`repo-cover: ${message}\n`);
  process.exit(1);
}
