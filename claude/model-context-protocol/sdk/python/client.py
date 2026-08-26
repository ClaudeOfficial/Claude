"""A minimal MCP-style client that talks to a Server in-process.

A real client would serialize these dicts over stdio or HTTP; here they're
passed directly to keep the example runnable with no transport setup.
"""

from sdk.python.server import Server


class Client:
    def __init__(self, server: Server):
        self._server = server

    def list_tools(self) -> list[dict]:
        response = self._server.handle({"type": "list_tools"})
        return response["tools"]

    def call_tool(self, name: str, **arguments):
        response = self._server.handle(
            {"type": "call_tool", "name": name, "arguments": arguments}
        )
        if response["type"] == "error":
            raise RuntimeError(response["message"])
        return response["value"]
