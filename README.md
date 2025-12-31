# Math MCP Server

A Model Context Protocol (MCP) server that provides basic mathematical operations, with a Streamlit web client for easy interaction.

## Features

This MCP server exposes six mathematical tools:

- **add**: Add two numbers together
- **multiply**: Multiply two numbers together
- **subtract**: Subtract the second number from the first
- **divide**: Divide the first number by the second (with zero-division protection)
- **sqrt**: Calculate the square root of a number
- **to_integer**: Convert a number to an integer

## Installation

This server uses Python and `uv` for dependency management. Make sure you have `uv` installed:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Install dependencies:
```bash
uv sync
```

## Usage

### Streamlit Web Client (Recommended)

The easiest way to interact with the Math MCP Server is through the Streamlit web interface:

```bash
uv run streamlit run app.py
```

This will start a web server (usually at http://localhost:8501) where you can:
- Select math operations from a dropdown menu
- Enter numbers in a user-friendly interface
- See results displayed instantly
- Get helpful error messages for invalid operations

### With Claude Desktop

Add this configuration to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "math": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/Simple MCP Example",
        "run",
        "math-mcp-server"
      ]
    }
  }
}
```

Replace `/ABSOLUTE/PATH/TO/Simple MCP Example` with the actual path to this project directory.

### With VS Code

The server is already configured in `.vscode/mcp.json`. VS Code with MCP support will automatically detect and use this configuration.

### Testing with MCP Inspector

You can test the server using the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector uv --directory . run math-mcp-server
```

## Available Tools

### add
Adds two numbers together.

**Parameters:**
- `a` (number): First number to add
- `b` (number): Second number to add

**Example:** `add(5, 3)` returns `5 + 3 = 8`

### multiply
Multiplies two numbers together.

**Parameters:**
- `a` (number): First number to multiply
- `b` (number): Second number to multiply

**Example:** `multiply(4, 7)` returns `4 × 7 = 28`

### subtract
Subtracts the second number from the first.

**Parameters:**
- `a` (number): Number to subtract from
- `b` (number): Number to subtract

**Example:** `subtract(10, 4)` returns `10 - 4 = 6`

### divide
Divides the first number by the second.

**Parameters:**
- `a` (number): Number to be divided (numerator)
- `b` (number): Number to divide by (denominator)

**Example:** `divide(20, 4)` returns `20 ÷ 4 = 5`

**Note:** Division by zero returns an error message.

### sqrt
Calculates the square root of a number.

**Parameters:**
- `a` (number): Number to calculate the square root of

**Example:** `sqrt(16)` returns `√16 = 4.0`

**Note:** Negative numbers return an error message.

### to_integer
Converts a number (including floats) to an integer. Handles edge cases like negative numbers and decimal values.

**Parameters:**
- `a` (number): Number to convert to integer

**Examples:** 
- `to_integer(3.7)` returns `3.7 → 3`
- `to_integer(-5.9)` returns `-5.9 → -5`
- `to_integer(42)` returns `42 → 42`

## Development

### Python Client Module

The `client.py` module provides a Python API for interacting with the MCP server programmatically:

```python
from client import perform_operation

# Perform operations
result = perform_operation("add", 5, 3)
print(result)  # "5.0 + 3.0 = 8.0"

result = perform_operation("sqrt", 16)
print(result)  # "√16.0 = 4.0"
```

### Run directly
To run the server directly:
```bash
uv run math-mcp-server
```

### Run the Streamlit client
To launch the web interface:
```bash
uv run streamlit run app.py
```

### Project Structure
```
.
├── server.py             # Main MCP server implementation
├── client.py             # Python client module for MCP communication
├── app.py                # Streamlit web frontend
├── pyproject.toml        # Project dependencies and configuration
└── README.md            # This file
```

## License

MIT
