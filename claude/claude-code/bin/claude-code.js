#!/usr/bin/env node
const path = require("path");
const { summarize, search, replaceAcrossFiles } = require("../src/index.js");

function printHelp() {
  console.log(`claude-code — a small local coding CLI

Usage:
  claude-code summary [dir]
  claude-code search <pattern> [dir]
  claude-code replace <find> <replaceWith> [dir] [--dry-run]

Examples:
  claude-code summary .
  claude-code search "TODO" .
  claude-code replace "foo" "bar" . --dry-run
`);
}

function main(argv) {
  const [cmd, ...rest] = argv;

  if (!cmd || cmd === "--help" || cmd === "-h") {
    printHelp();
    return;
  }

  if (cmd === "summary") {
    const dir = rest[0] || ".";
    const result = summarize(path.resolve(dir));
    console.log(`Files: ${result.totalFiles}`);
    for (const [ext, count] of Object.entries(result.byExtension)) {
      console.log(`  ${ext.padEnd(12)} ${count}`);
    }
    return;
  }

  if (cmd === "search") {
    const [pattern, dir = "."] = rest;
    if (!pattern) {
      console.error("Usage: claude-code search <pattern> [dir]");
      process.exit(1);
    }
    const matches = search(path.resolve(dir), pattern);
    if (matches.length === 0) {
      console.log("No matches found.");
      return;
    }
    for (const m of matches) {
      console.log(`${m.file}:${m.line}: ${m.text}`);
    }
    console.log(`\n${matches.length} match(es)`);
    return;
  }

  if (cmd === "replace") {
    const dryRun = rest.includes("--dry-run");
    const positional = rest.filter((a) => a !== "--dry-run");
    const [find, replaceWith, dir = "."] = positional;
    if (!find || replaceWith === undefined) {
      console.error("Usage: claude-code replace <find> <replaceWith> [dir] [--dry-run]");
      process.exit(1);
    }
    const count = replaceAcrossFiles(path.resolve(dir), find, replaceWith, { dryRun });
    console.log(
      dryRun
        ? `Would modify ${count} file(s). Re-run without --dry-run to apply.`
        : `Modified ${count} file(s).`
    );
    return;
  }

  console.error(`Unknown command: ${cmd}`);
  printHelp();
  process.exit(1);
}

main(process.argv.slice(2));
