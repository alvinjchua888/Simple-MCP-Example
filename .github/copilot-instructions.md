# Math MCP Server - Workspace Instructions

This workspace contains a Model Context Protocol (MCP) server that provides basic mathematical operations.

## Project Overview

- **Type**: MCP Server (Python)
- **Purpose**: Provide basic math functions (add, multiply, subtract, divide) via MCP
- **SDK**: mcp (Python SDK with FastMCP)
- **Transport**: STDIO

## Project Structure

- `server.py` - Main server implementation with four math tools
- `pyproject.toml` - Project dependencies and configuration
- `.vscode/mcp.json` - VS Code MCP configuration

## Available Tools

1. **add** - Adds two numbers
2. **multiply** - Multiplies two numbers
3. **subtract** - Subtracts two numbers
4. **divide** - Divides two numbers (with zero-division protection)

## Development Commands

- `uv sync` - Install dependencies
- `uv run math-mcp-server` - Run the server directly
- `npx @modelcontextprotocol/inspector uv --directory . run math-mcp-server` - Test with MCP Inspector

## MCP Configuration

The server is configured in `.vscode/mcp.json` and can be used with any MCP-compatible client like Claude Desktop or VS Code with MCP support.
