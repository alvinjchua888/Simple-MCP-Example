#!/usr/bin/env python3
"""Math MCP Server - Provides basic mathematical operations."""

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("math-mcp-server")


@mcp.tool()
async def add(a: float, b: float) -> str:
    """
    Add two numbers together.
    
    Args:
        a: First number to add
        b: Second number to add
    """
    result = a + b
    return f"{a} + {b} = {result}"


@mcp.tool()
async def multiply(a: float, b: float) -> str:
    """
    Multiply two numbers together.
    
    Args:
        a: First number to multiply
        b: Second number to multiply
    """
    result = a * b
    return f"{a} × {b} = {result}"


@mcp.tool()
async def subtract(a: float, b: float) -> str:
    """
    Subtract the second number from the first.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
    """
    result = a - b
    return f"{a} - {b} = {result}"


@mcp.tool()
async def divide(a: float, b: float) -> str:
    """
    Divide the first number by the second.
    
    Args:
        a: Number to be divided (numerator)
        b: Number to divide by (denominator)
    """
    if b == 0:
        raise ValueError("Error: Cannot divide by zero")
    
    result = a / b
    return f"{a} ÷ {b} = {result}"
