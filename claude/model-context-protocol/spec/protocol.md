# Protocol overview (minimal subset)

This repo implements a small, working subset of an MCP-style protocol: enough
to register tools on a server, list them from a client, and call one with
arguments — all in-process, in Python, with no network dependency required.

## Message shapes

**List tools request → response**

```json
// request
{"type": "list_tools"}

// response
{"type": "list_tools_result", "tools": [
  {"name": "add", "description": "Add two numbers", "parameters": ["a", "b"]}
]}
```

**Call tool request → response**

```json
// request
{"type": "call_tool", "name": "add", "arguments": {"a": 2, "b": 3}}

// response
{"type": "call_tool_result", "value": 5}
```

## Transport

The reference implementation in `sdk/python/` uses an in-process
`Server`/`Client` pair connected by a simple queue, so the whole thing runs
with `python examples/basic_server.py` and no sockets. A real deployment
would swap the transport for stdio or HTTP+SSE while keeping the same
message shapes.
