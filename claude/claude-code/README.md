# claude-code

A small, dependency-free command-line tool for poking around a codebase:
summarize file counts, search across files, and do a safe find-and-replace
with a dry-run preview. No API calls, no natural-language parsing — just a
genuinely useful little utility, kept intentionally simple.

## Install

```bash
git clone https://github.com/YOUR_USERNAME/claude-code
cd claude-code
npm link   # makes the `claude-code` command available globally
```

Or just run it directly with Node:

```bash
node bin/claude-code.js summary .
```

## Usage

```bash
claude-code summary [dir]
claude-code search <pattern> [dir]
claude-code replace <find> <replaceWith> [dir] [--dry-run]
```

### Examples

```bash
$ claude-code summary .
Files: 12
  .js           7
  .md           2
  .json         3

$ claude-code search "TODO" .
src/index.js:42: // TODO: handle symlinks
2 match(es)

$ claude-code replace "foo" "bar" . --dry-run
Would modify 3 file(s). Re-run without --dry-run to apply.
```

## Tests

```bash
npm test
```

## Project structure

```
bin/
  claude-code.js   # CLI entry point — argument parsing and output formatting
src/
  index.js          # the actual logic: walk, summarize, search, replaceAcrossFiles
tests/
  index.test.js     # dependency-free tests using Node's built-in assert module
```

## License

MIT — see [LICENSE](LICENSE).
