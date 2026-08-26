# model-context-protocol

A minimal, working reference implementation of an MCP-style protocol: a
`Server` that registers Python functions as tools, and a `Client` that can
list and call them. Runs entirely in-process with no network setup, so it's
easy to read start to finish and adapt to a real transport later.

## Quickstart

```bash
git clone https://github.com/YOUR_USERNAME/model-context-protocol
cd model-context-protocol
PYTHONPATH=. python examples/basic_server.py
```

```
Available tools:
  - add(a, b): Add two numbers
  - reverse(text): Reverse a string

Calling add(2, 3) -> 5
Calling reverse('mcp') -> pcm
```

## Writing your own tools

```python
from sdk.python.server import Server
from sdk.python.client import Client

server = Server("my-server")

@server.tool(description="Multiply two numbers")
def multiply(a, b):
    return a * b

client = Client(server)
client.call_tool("multiply", a=4, b=5)  # -> 20
```

## Tests

```bash
PYTHONPATH=. python sdk/python/test_protocol.py
```

## Project structure

```
spec/protocol.md        # the message shapes this implementation follows
sdk/python/server.py     # tool registration + message handling
sdk/python/client.py      # list_tools / call_tool convenience wrapper
examples/basic_server.py   # a runnable end-to-end demo
```

## From here to a real deployment

Swap the direct `Client(server)` in-process call for a real transport (stdio
or HTTP + server-sent events) that serializes the same `list_tools` /
`call_tool` message dicts to JSON — the `Server.handle()` method doesn't
need to change.

## License

MIT — see [LICENSE](LICENSE).
