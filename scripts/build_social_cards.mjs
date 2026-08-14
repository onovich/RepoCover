#!/usr/bin/env node

import { existsSync } from "node:fs";
import { mkdir, rm } from "node:fs/promises";
import { createRequire } from "node:module";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const root = resolve(scriptDirectory, "..");
const outputDirectory = resolve(root, process.argv[2] || "assets/social");
const force = process.argv.includes("--force");

const require = createRequire(import.meta.url);
let sharp;
try {
  sharp = require("sharp");
} catch {
  fail("Sharp is unavailable. Expose the configured workspace packages through NODE_PATH.");
}

const examples = [
  "prismdraft.png",
  "littlepng.png",
  "deskmochi.png",
  "audiotrim.png",
  "beat.png",
  "justgoal-skill.png",
  "knot.png",
  "ping.png",
];

const cards = [
  {
    filename: "repocover-x-en.png",
    width: 1280,
    height: 640,
    locale: "en",
    columns: 3,
    rows: 2,
    files: examples.slice(0, 6),
    title: ["Different repositories. Different covers."],
    subtitle: "RepoCover reads the project first. Editable SVG + validated 1280 × 640 PNG.",
  },
  {
    filename: "repocover-linkedin-en.png",
    width: 1200,
    height: 627,
    locale: "en",
    columns: 3,
    rows: 2,
    files: examples.slice(0, 6),
    title: ["Different repositories. Different covers."],
    subtitle: "RepoCover reads the project first. Editable SVG + validated 1280 × 640 PNG.",
  },
  {
    filename: "repocover-linkedin-zh.png",
    width: 1200,
    height: 627,
    locale: "zh",
    columns: 3,
    rows: 2,
    files: examples.slice(0, 6),
    title: ["不同的项目，应该有不同的封面。"],
    subtitle: "RepoCover 会先读懂项目，再决定怎么呈现。",
  },
  {
    filename: "repocover-square-en.png",
    width: 1080,
    height: 1080,
    locale: "en",
    columns: 2,
    rows: 3,
    files: examples.slice(0, 6),
    title: ["Different projects.", "Different covers."],
    subtitle: "RepoCover reads the project first, then chooses the visual approach.",
  },
  {
    filename: "repocover-square-zh.png",
    width: 1080,
    height: 1080,
    locale: "zh",
    columns: 2,
    rows: 3,
    files: examples.slice(0, 6),
    title: ["不同的项目，", "应该有不同的封面。"],
    subtitle: "RepoCover 会先读懂项目，再决定怎么呈现。",
  },
  {
    filename: "repocover-portrait-en.png",
    width: 1080,
    height: 1350,
    locale: "en",
    columns: 2,
    rows: 4,
    files: examples,
    title: ["Different projects.", "Different covers."],
    subtitle: "One Skill, eight real repository covers.",
  },
  {
    filename: "repocover-portrait-zh.png",
    width: 1080,
    height: 1350,
    locale: "zh",
    columns: 2,
    rows: 4,
    files: examples,
    title: ["不同的项目，", "应该有不同的封面。"],
    subtitle: "一个 Skill，8 个真实仓库封面。",
  },
  {
    filename: "repocover-product-hunt-gallery.png",
    width: 1270,
    height: 760,
    locale: "en",
    columns: 3,
    rows: 2,
    files: examples.slice(0, 6),
    title: ["Different repositories. Different covers."],
    subtitle: "RepoCover reads the project before it designs the GitHub Social Preview.",
    footer: "EDITABLE SVG  ·  VALIDATED 1280 × 640 PNG  ·  GITHUB.COM/ONOVICH/REPOCOVER",
  },
];

await mkdir(outputDirectory, { recursive: true });
const results = [];

for (const card of cards) {
  const output = resolve(outputDirectory, card.filename);
  if (existsSync(output) && !force) {
    fail(`Output already exists: ${output}. Pass --force to replace it.`);
  }
  if (existsSync(output)) {
    await rm(output);
  }
  results.push(await renderCard(card, output));
}

const thumbnailOutput = resolve(outputDirectory, "repocover-product-hunt-thumbnail.png");
if (existsSync(thumbnailOutput) && !force) {
  fail(`Output already exists: ${thumbnailOutput}. Pass --force to replace it.`);
}
if (existsSync(thumbnailOutput)) {
  await rm(thumbnailOutput);
}
results.push(await renderThumbnail(thumbnailOutput));

process.stdout.write(`${JSON.stringify(results)}\n`);

async function renderCard(card, output) {
  const outer = card.width >= 1200 ? 42 : 46;
  const gap = card.width >= 1200 ? 18 : 18;
  const headerHeight = card.width >= 1200 ? 196 : 274;
  const footerHeight = card.footer ? 104 : 0;
  const gridBottom = card.height - outer - footerHeight;
  const cardWidth = Math.floor((card.width - outer * 2 - gap * (card.columns - 1)) / card.columns);
  const availableGridHeight = gridBottom - headerHeight;
  const cardHeight = Math.floor((availableGridHeight - gap * (card.rows - 1)) / card.rows);
  const titleSize = card.width >= 1200 ? 48 : card.locale === "zh" ? 58 : 64;
  const titleLineHeight = Math.round(titleSize * 1.02);
  const titleStartY = card.width >= 1200 ? 110 : 128;
  const titleMarkup = card.title.map((line, index) =>
    `<text x="${outer}" y="${titleStartY + index * titleLineHeight}" class="title">${escapeXml(line)}</text>`,
  ).join("");
  const subtitleY = titleStartY + (card.title.length - 1) * titleLineHeight + (card.width >= 1200 ? 52 : 42);
  const background = Buffer.from(`
  <svg xmlns="http://www.w3.org/2000/svg" width="${card.width}" height="${card.height}" viewBox="0 0 ${card.width} ${card.height}">
    <style>
      .eyebrow { font: 800 15px Consolas, monospace; letter-spacing: 3px; fill: #78c7e3; }
      .title { font: 900 ${titleSize}px ${card.locale === "zh" ? "'Microsoft YaHei', 'Segoe UI', sans-serif" : "Arial, sans-serif"}; letter-spacing: ${card.locale === "zh" ? "-2px" : "-3px"}; fill: #fffdf9; }
      .subtitle { font: 500 ${card.width >= 1200 ? 20 : 18}px ${card.locale === "zh" ? "'Microsoft YaHei', 'Segoe UI', sans-serif" : "Arial, sans-serif"}; fill: #abc9d5; }
      .footer { font: 800 14px Consolas, monospace; letter-spacing: 1.8px; fill: #082635; }
    </style>
    <rect width="${card.width}" height="${card.height}" fill="#082635"/>
    <circle cx="${card.width - 38}" cy="32" r="180" fill="#164e68"/>
    <circle cx="${card.width + 8}" cy="-8" r="104" fill="#ff7048" fill-opacity="0.18"/>
    <text x="${outer + 74}" y="63" class="eyebrow">REPOCOVER · GITHUB SOCIAL PREVIEW</text>
    ${titleMarkup}
    <text x="${outer}" y="${subtitleY}" class="subtitle">${escapeXml(card.subtitle)}</text>
    ${card.footer ? `<rect x="${outer}" y="${card.height - 82}" width="${card.width - outer * 2}" height="48" rx="15" fill="#78c7e3"/><text x="${outer + 24}" y="${card.height - 51}" class="footer">${escapeXml(card.footer)}</text>` : ""}
  </svg>`);

  const composites = [{ input: background, left: 0, top: 0 }];
  for (const [index, filename] of card.files.entries()) {
    const column = index % card.columns;
    const row = Math.floor(index / card.columns);
    const left = outer + column * (cardWidth + gap);
    const top = headerHeight + row * (cardHeight + gap);
    const image = await sharp(resolve(root, "examples", filename))
      .resize(cardWidth, cardHeight, { fit: "contain", background: "#082635" })
      .png()
      .toBuffer();
    const frame = Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${cardWidth}" height="${cardHeight}"><rect x="1" y="1" width="${cardWidth - 2}" height="${cardHeight - 2}" rx="13" fill="none" stroke="#78c7e3" stroke-opacity="0.44" stroke-width="2"/></svg>`);
    composites.push({ input: image, left, top });
    composites.push({ input: frame, left, top });
  }

  const mark = await sharp(resolve(root, "assets", "repo-cover-mark.svg"))
    .resize(54, 54)
    .png()
    .toBuffer();
  composites.push({ input: mark, left: outer, top: 31 });

  const result = await sharp({
    create: { width: card.width, height: card.height, channels: 4, background: "#082635" },
  })
    .composite(composites)
    .png({ compressionLevel: 9, quality: 94 })
    .toFile(output);

  return { output, width: result.width, height: result.height, bytes: result.size };
}

async function renderThumbnail(output) {
  const background = Buffer.from(`
  <svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">
    <rect width="240" height="240" rx="48" fill="#082635"/>
    <circle cx="214" cy="30" r="94" fill="#164e68"/>
    <circle cx="226" cy="10" r="54" fill="#ff7048" fill-opacity="0.28"/>
  </svg>`);
  const mark = await sharp(resolve(root, "assets", "repo-cover-mark.svg"))
    .resize(136, 136)
    .png()
    .toBuffer();
  const result = await sharp({
    create: { width: 240, height: 240, channels: 4, background: "#082635" },
  })
    .composite([
      { input: background, left: 0, top: 0 },
      { input: mark, left: 52, top: 52 },
    ])
    .png({ compressionLevel: 9, quality: 94 })
    .toFile(output);
  return { output, width: result.width, height: result.height, bytes: result.size };
}

function escapeXml(value) {
  return value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
}

function fail(message) {
  process.stderr.write(`repo-cover: ${message}\n`);
  process.exit(1);
}
