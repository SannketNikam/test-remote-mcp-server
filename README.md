# Basic Setup

- Install uv
- Create a project folder named fastmcp-demo-server
- Open the folder in VS Code
- Open terminal
- Execute the command: uv init
- uv add fastmcp
- Fastmcp version
- Create a basic server
- Test the server -uv run fastmcp dev main.py (MCP Inspector CMD)
- Run the server -uv run fastmcp run main.py
- Add the server to claude desktop - uv run fastmcp install claude-desktop main.py (For local server)

<i>Use the same steps from above to create a Remote MCP Server and follow the below steps and for Local MCP Server just follow till the upper step.</i>

- Test the server using MCP Inspector | This opens in browser just like FastAPI's page
- Create a GitHub repo
- git init
- git add
- git commit -m "Initial commit: Simple MCP Server"
- git remote add origin https://github.com/YourUsername/simple-mcp-server.git
- git push -u origin main
- Create an account on FastMCP Cloud
- Deploy on FastMCP Cloud


```python
import random
from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP(name="Demo Server")

@mcp.tool
def roll_dice(n_dice: int=1) -> list[int]:
    """Roll n_dice 6 sided dice and return the results."""
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.toll
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

if __name___ == "__main__":
    mcp.run()
```