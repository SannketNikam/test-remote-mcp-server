# Sample Server *******************************************8

from fastmcp import FastMCP
import random
import json

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")

# Tool: Add two numbers
@mcp.tool
def add(a: int, b: int) -> int:

    """
    Add two numbers together
    
    Args:
        a: First Number
        b: Second Number

    Returns:
        The sum of a and b
    """

    return a + b

# Tool: Generate a random number
@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:

    """
    Generate a random number within a range.

    Args:
        min_val: Minimum Value (default: 1)
        max_val: Maximum Value (default: 100)

    Returns:
        A random integer between min_val and max_val
    """

    return random.randint(min_val, max_val)

# Resource: Server Information
@mcp.resource("info://server")
def server_info() -> str:

    """
    Get information about the server.
    """

    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Your Name"
    }

    return json.dumps(info, indent=2)

# Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000) # Remote Server -> Transport: http
    # mcp.run() # Local Server -> Transport: stdio

# CMD: fastmcp run server.py --transport http --host 0.0.0.0 --port 8000
# Alternate CMD: uv run server.py
# MCP Inspector: uv run fastmcp dev server.py | This opens in browser just like FastAPI's page