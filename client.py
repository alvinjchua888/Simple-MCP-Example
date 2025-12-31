#!/usr/bin/env python3
"""MCP Client for Math Server - Backend module to interact with the MCP math server."""

import asyncio
from contextlib import asynccontextmanager
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MathClient:
    """Client for interacting with the Math MCP Server."""
    
    def __init__(self):
        self.session = None
        self.client = None
        
    @asynccontextmanager
    async def connect(self):
        """Connect to the Math MCP Server."""
        import os
        import sys
        
        # Get the absolute path to server.py
        server_path = os.path.join(os.path.dirname(__file__), "server.py")
        
        server_params = StdioServerParameters(
            command=sys.executable,  # Use current Python interpreter
            args=[server_path],
            env=None
        )
        
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                self.session = session
                yield session
    
    async def list_tools(self):
        """List all available tools from the server."""
        if not self.session:
            raise RuntimeError("Client not connected. Use 'async with client.connect()' first.")
        
        response = await self.session.list_tools()
        return response.tools
    
    async def call_tool(self, tool_name: str, arguments: dict):
        """
        Call a tool on the server.
        
        Args:
            tool_name: Name of the tool to call (e.g., 'add', 'multiply')
            arguments: Dictionary of arguments for the tool
            
        Returns:
            The result from the tool call
        """
        if not self.session:
            raise RuntimeError("Client not connected. Use 'async with client.connect()' first.")
        
        result = await self.session.call_tool(tool_name, arguments)
        return result
    
    async def add(self, a: float, b: float):
        """Add two numbers."""
        result = await self.call_tool("add", {"a": a, "b": b})
        return self._extract_result(result)
    
    async def subtract(self, a: float, b: float):
        """Subtract two numbers."""
        result = await self.call_tool("subtract", {"a": a, "b": b})
        return self._extract_result(result)
    
    async def multiply(self, a: float, b: float):
        """Multiply two numbers."""
        result = await self.call_tool("multiply", {"a": a, "b": b})
        return self._extract_result(result)
    
    async def divide(self, a: float, b: float):
        """Divide two numbers."""
        result = await self.call_tool("divide", {"a": a, "b": b})
        return self._extract_result(result)
    
    async def sqrt(self, a: float):
        """Calculate square root."""
        result = await self.call_tool("sqrt", {"a": a})
        return self._extract_result(result)
    
    async def to_integer(self, a: float):
        """Convert to integer."""
        result = await self.call_tool("to_integer", {"a": a})
        return self._extract_result(result)
    
    def _extract_result(self, result):
        """Extract the text content from the tool result."""
        if hasattr(result, 'content') and len(result.content) > 0:
            return result.content[0].text
        return str(result)


# Synchronous wrapper functions for Streamlit
def run_async(coro):
    """Run an async coroutine in a synchronous context."""
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)


async def _perform_operation(operation: str, a: float, b: float = None):
    """Perform a math operation using the MCP client."""
    client = MathClient()
    async with client.connect():
        if operation == "add":
            return await client.add(a, b)
        elif operation == "subtract":
            return await client.subtract(a, b)
        elif operation == "multiply":
            return await client.multiply(a, b)
        elif operation == "divide":
            return await client.divide(a, b)
        elif operation == "sqrt":
            return await client.sqrt(a)
        elif operation == "to_integer":
            return await client.to_integer(a)
        else:
            raise ValueError(f"Unknown operation: {operation}")


def perform_operation(operation: str, a: float, b: float = None):
    """Synchronous wrapper for performing operations."""
    return run_async(_perform_operation(operation, a, b))


async def _get_available_tools():
    """Get list of available tools from the server."""
    client = MathClient()
    async with client.connect():
        return await client.list_tools()


def get_available_tools():
    """Synchronous wrapper for getting available tools."""
    return run_async(_get_available_tools())
