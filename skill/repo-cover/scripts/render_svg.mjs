#!/usr/bin/env node

import { existsSync } from "node:fs";
import { rename, rm } from "node:fs/promises";
import { createRequire } from "node:module";
import { extname, resolve } from "node:path";

const rawArguments = process.argv.slice(2);
const force = rawArguments.includes("--force");
const argumentsWithoutFlags = rawArguments.filter((argument) => argument !== "--force");

if (argumentsWithoutFlags.length !== 2) {
  fail("Usage: node render_svg.mjs <source.svg> <output.png> [--force]");
}

const sourcePath = resolve(argumentsWithoutFlags[0]);
const outputPath = resolve(argumentsWithoutFlags[1]);

if (extname(sourcePath).toLowerCase() !== ".svg") {
  fail("The source must be an SVG file.");
}
if (extname(outputPath).toLowerCase() !== ".png") {
  fail("The output must be a PNG file.");
}
if (!existsSync(sourcePath)) {
  fail(`Source file does not exist: ${sourcePath}`);
}
if (existsSync(outputPath) && !force) {
  fail(`Output already exists: ${outputPath}. Pass --force only when replacement is intended.`);
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

const temporaryPath = `${outputPath}.tmp-${process.pid}.png`;

try {
  const result = await sharp(sourcePath)
    .resize(1280, 640, { fit: "fill" })
    .png({ compressionLevel: 9, palette: true, quality: 100 })
    .toFile(temporaryPath);

  if (existsSync(outputPath)) {
    await rm(outputPath);
  }
  await rename(temporaryPath, outputPath);
  process.stdout.write(
    JSON.stringify({
      output: outputPath,
      format: result.format,
      width: result.width,
      height: result.height,
      bytes: result.size
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
