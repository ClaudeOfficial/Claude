"""A minimal MCP-style server: register tools, list them, call them."""

from dataclasses import dataclass
from typing import Callable


@dataclass
class Tool:
    name: str
    description: str
    fn: Callable
    parameters: list[str]


class Server:
    def __init__(self, name: str):
        self.name = name
        self._tools: dict[str, Tool] = {}

    def tool(self, description: str = ""):
        """Decorator to register a function as a callable tool."""

        def decorator(fn: Callable):
            params = list(fn.__code__.co_varnames[: fn.__code__.co_argcount])
            self._tools[fn.__name__] = Tool(
                name=fn.__name__, description=description, fn=fn, parameters=params
            )
            return fn

        return decorator

    def handle(self, message: dict) -> dict:
        if message["type"] == "list_tools":
            return {
                "type": "list_tools_result",
                "tools": [
                    {"name": t.name, "description": t.description, "parameters": t.parameters}
                    for t in self._tools.values()
                ],
            }
        if message["type"] == "call_tool":
            tool = self._tools.get(message["name"])
            if tool is None:
                return {"type": "error", "message": f"Unknown tool: {message['name']}"}
            try:
                value = tool.fn(**message.get("arguments", {}))
            except TypeError as e:
                return {"type": "error", "message": str(e)}
            return {"type": "call_tool_result", "value": value}
        return {"type": "error", "message": f"Unknown message type: {message['type']}"}
