const assert = require("assert");
const fs = require("fs");
const os = require("os");
const path = require("path");
const { summarize, search, replaceAcrossFiles } = require("../src/index.js");

function makeTempDir() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "claude-code-test-"));
  fs.writeFileSync(path.join(dir, "a.txt"), "hello TODO world\n");
  fs.writeFileSync(path.join(dir, "b.md"), "nothing here\n");
  fs.mkdirSync(path.join(dir, "sub"));
  fs.writeFileSync(path.join(dir, "sub", "c.txt"), "another TODO\n");
  return dir;
}

function test(name, fn) {
  try {
    fn();
    console.log(`PASS  ${name}`);
    return true;
  } catch (err) {
    console.log(`FAIL  ${name}: ${err.message}`);
    return false;
  }
}

const results = [];

results.push(
  test("summarize counts files by extension", () => {
    const dir = makeTempDir();
    const result = summarize(dir);
    assert.strictEqual(result.totalFiles, 3);
    assert.strictEqual(result.byExtension[".txt"], 2);
    assert.strictEqual(result.byExtension[".md"], 1);
  })
);

results.push(
  test("search finds matching lines across nested files", () => {
    const dir = makeTempDir();
    const matches = search(dir, "TODO");
    assert.strictEqual(matches.length, 2);
  })
);

results.push(
  test("replaceAcrossFiles with dryRun does not modify files", () => {
    const dir = makeTempDir();
    const count = replaceAcrossFiles(dir, "TODO", "DONE", { dryRun: true });
    assert.strictEqual(count, 2);
    const content = fs.readFileSync(path.join(dir, "a.txt"), "utf8");
    assert.ok(content.includes("TODO"));
  })
);

results.push(
  test("replaceAcrossFiles actually writes changes", () => {
    const dir = makeTempDir();
    replaceAcrossFiles(dir, "TODO", "DONE", { dryRun: false });
    const content = fs.readFileSync(path.join(dir, "a.txt"), "utf8");
    assert.ok(content.includes("DONE"));
    assert.ok(!content.includes("TODO"));
  })
);

const passed = results.filter(Boolean).length;
console.log(`\n${passed}/${results.length} tests passed`);
process.exit(passed === results.length ? 0 : 1);
