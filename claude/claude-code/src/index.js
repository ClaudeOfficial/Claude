const fs = require("fs");
const path = require("path");

const DEFAULT_IGNORE = new Set(["node_modules", ".git", "dist", "build"]);

/**
 * Recursively walk a directory, returning a flat list of file paths.
 */
function walk(dir, ignore = DEFAULT_IGNORE) {
  const results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (ignore.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...walk(full, ignore));
    } else {
      results.push(full);
    }
  }
  return results;
}

/**
 * Summarize a directory: file count by extension.
 */
function summarize(dir) {
  const files = walk(dir);
  const byExt = {};
  for (const file of files) {
    const ext = path.extname(file) || "(no ext)";
    byExt[ext] = (byExt[ext] || 0) + 1;
  }
  return { totalFiles: files.length, byExtension: byExt };
}

/**
 * Search for a literal string or regex across all files in a directory.
 * Returns an array of { file, line, text } matches.
 */
function search(dir, pattern) {
  const isRegex = pattern.startsWith("/") && pattern.lastIndexOf("/") > 0;
  const matcher = isRegex
    ? new RegExp(pattern.slice(1, pattern.lastIndexOf("/")), pattern.slice(pattern.lastIndexOf("/") + 1))
    : null;

  const matches = [];
  for (const file of walk(dir)) {
    let content;
    try {
      content = fs.readFileSync(file, "utf8");
    } catch {
      continue; // binary or unreadable file
    }
    const lines = content.split("\n");
    lines.forEach((line, i) => {
      const hit = isRegex ? matcher.test(line) : line.includes(pattern);
      if (hit) matches.push({ file, line: i + 1, text: line.trim() });
    });
  }
  return matches;
}

/**
 * Find-and-replace a literal string across all files in a directory.
 * Returns the number of files modified. Set dryRun to preview without writing.
 */
function replaceAcrossFiles(dir, find, replaceWith, { dryRun = false } = {}) {
  let modifiedCount = 0;
  for (const file of walk(dir)) {
    let content;
    try {
      content = fs.readFileSync(file, "utf8");
    } catch {
      continue;
    }
    if (!content.includes(find)) continue;
    modifiedCount += 1;
    if (!dryRun) {
      fs.writeFileSync(file, content.split(find).join(replaceWith), "utf8");
    }
  }
  return modifiedCount;
}

module.exports = { walk, summarize, search, replaceAcrossFiles };
