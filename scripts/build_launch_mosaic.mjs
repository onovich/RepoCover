#!/usr/bin/env node

import { existsSync } from "node:fs";
import { rm } from "node:fs/promises";
import { createRequire } from "node:module";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const root = resolve(scriptDirectory, "..");
const output = resolve(root, process.argv[2] || "assets/launch-mosaic.png");
const force = process.argv.includes("--force");

if (existsSync(output) && !force) {
  fail(`Output already exists: ${output}. Pass --force to replace it.`);
}

const require = createRequire(import.meta.url);
let sharp;
try {
  sharp = require("sharp");
} catch {
  fail("Sharp is unavailable. Expose the configured workspace packages through NODE_PATH.");
}

const examples = [
  ["PrismDraft", "3D identity", "prismdraft.png"],
  ["LittlePNG", "product UI", "littlepng.png"],
  ["DeskMochi", "character asset", "deskmochi.png"],
  ["AudioTrim", "real workflow", "audiotrim.png"],
  ["Beat", "cold start", "beat.png"],
  ["JustGoal.skill", "semantic topology", "justgoal-skill.png"],
  ["Knot", "geometric relations", "knot.png"],
  ["Ping", "bounded reconstruction", "ping.png"],
];

const width = 1600;
const height = 1000;
const cardWidth = 350;
const cardHeight = 175;
const gapX = 26;
const gapY = 66;
const startX = 62;
const startY = 230;

const cardMarkup = examples.map(([name, mode], index) => {
  const column = index % 4;
  const row = Math.floor(index / 4);
  const x = startX + column * (cardWidth + gapX);
  const y = startY + row * (cardHeight + gapY);
  return `
    <rect x="${x - 2}" y="${y - 2}" width="${cardWidth + 4}" height="${cardHeight + 4}" rx="16" fill="#78c7e3" fill-opacity="0.38"/>
    <text x="${x}" y="${y + cardHeight + 26}" class="name">${escapeXml(name)}</text>
    <text x="${x + cardWidth}" y="${y + cardHeight + 26}" text-anchor="end" class="mode">${escapeXml(mode)}</text>`;
}).join("");

const background = Buffer.from(`
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
  <style>
    .eyebrow { font: 800 18px Consolas, monospace; letter-spacing: 4px; fill: #78c7e3; }
    .title { font: 900 72px Arial, sans-serif; letter-spacing: -4px; fill: #fffdf9; }
    .subtitle { font: 500 25px Arial, sans-serif; fill: #abc9d5; }
    .name { font: 800 20px Arial, sans-serif; fill: #fffdf9; }
    .mode { font: 700 15px Consolas, monospace; fill: #78c7e3; }
    .footer { font: 800 18px Consolas, monospace; letter-spacing: 3px; fill: #082635; }
  </style>
  <rect width="1600" height="1000" fill="#082635"/>
  <circle cx="1470" cy="120" r="260" fill="#164e68"/>
  <circle cx="1510" cy="50" r="145" fill="#ff7048" fill-opacity="0.17"/>
  <text x="150" y="72" class="eyebrow">CODEX SKILL · GITHUB SOCIAL PREVIEW</text>
  <text x="62" y="150" class="title">Eight repositories. Eight visual identities.</text>
  <text x="64" y="194" class="subtitle">RepoCover reads the project before it designs the cover.</text>
  ${cardMarkup}
  <rect x="62" y="801" width="1476" height="112" rx="24" fill="#78c7e3"/>
  <text x="110" y="850" class="footer">REPOSITORY EVIDENCE → EDITABLE DESIGN → 1280 × 640 VALIDATION</text>
  <text x="110" y="884" class="footer" opacity="0.72">github.com/onovich/RepoCover</text>
</svg>`);

const composites = [{ input: background, left: 0, top: 0 }];

for (const [, , filename] of examples) {
  const index = composites.length - 1;
  const column = index % 4;
  const row = Math.floor(index / 4);
  const image = await sharp(resolve(root, "examples", filename))
    .resize(cardWidth, cardHeight, { fit: "cover" })
    .png()
    .toBuffer();
  composites.push({
    input: image,
    left: startX + column * (cardWidth + gapX),
    top: startY + row * (cardHeight + gapY),
  });
}

const mark = await sharp(resolve(root, "assets", "repo-cover-mark.svg"))
  .resize(64, 64)
  .png()
  .toBuffer();
composites.push({ input: mark, left: 62, top: 34 });

if (existsSync(output)) {
  await rm(output);
}

const result = await sharp({
  create: { width, height, channels: 4, background: "#082635" },
})
  .composite(composites)
  .png({ compressionLevel: 9, quality: 94 })
  .toFile(output);

process.stdout.write(JSON.stringify({ output, width: result.width, height: result.height, bytes: result.size }) + "\n");

function escapeXml(value) {
  return value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
}

function fail(message) {
  process.stderr.write(`repo-cover: ${message}\n`);
  process.exit(1);
}
