"""Run with: python examples/basic_server.py"""

from sdk.python.client import Client
from sdk.python.server import Server

server = Server("demo-server")


@server.tool(description="Add two numbers")
def add(a, b):
    return a + b


@server.tool(description="Reverse a string")
def reverse(text):
    return text[::-1]


if __name__ == "__main__":
    client = Client(server)

    print("Available tools:")
    for tool in client.list_tools():
        print(f"  - {tool['name']}({', '.join(tool['parameters'])}): {tool['description']}")

    print("\nCalling add(2, 3) ->", client.call_tool("add", a=2, b=3))
    print("Calling reverse('mcp') ->", client.call_tool("reverse", text="mcp"))
