"""Run with: PYTHONPATH=. python sdk/python/test_protocol.py"""

import sys

from sdk.python.client import Client
from sdk.python.server import Server


def _make_server():
    server = Server("test-server")

    @server.tool(description="Add two numbers")
    def add(a, b):
        return a + b

    return server


def test_list_tools_returns_registered_tool():
    client = Client(_make_server())
    tools = client.list_tools()
    assert len(tools) == 1
    assert tools[0]["name"] == "add"


def test_call_tool_returns_correct_value():
    client = Client(_make_server())
    assert client.call_tool("add", a=2, b=3) == 5


def test_call_unknown_tool_raises():
    client = Client(_make_server())
    try:
        client.call_tool("nonexistent", a=1)
        assert False, "expected RuntimeError"
    except RuntimeError as e:
        assert "Unknown tool" in str(e)


def test_call_tool_with_wrong_arguments_raises():
    client = Client(_make_server())
    try:
        client.call_tool("add", a=1)  # missing 'b'
        assert False, "expected RuntimeError"
    except RuntimeError:
        pass


def _run_all():
    tests = [v for k, v in list(globals().items()) if k.startswith("test_")]
    failures = 0
    for t in tests:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"FAIL  {t.__name__}: {e}")
    print(f"\n{len(tests) - failures}/{len(tests)} tests passed")
    return failures


if __name__ == "__main__":
    sys.exit(1 if _run_all() else 0)
