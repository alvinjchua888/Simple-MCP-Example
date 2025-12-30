#!/usr/bin/env node

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create server instance
const server = new McpServer({
  name: "math-mcp-server",
  version: "1.0.0",
});

// Register the add tool
server.registerTool(
  "add",
  {
    title: "Addition Tool",
    description: "Add two numbers together",
    inputSchema: {
      a: z.number().describe("First number to add"),
      b: z.number().describe("Second number to add"),
    },
  },
  async ({ a, b }) => ({
    content: [
      {
        type: "text",
        text: `${a} + ${b} = ${a + b}`,
      },
    ],
  })
);

// Register the multiply tool
server.registerTool(
  "multiply",
  {
    title: "Multiplication Tool",
    description: "Multiply two numbers together",
    inputSchema: {
      a: z.number().describe("First number to multiply"),
      b: z.number().describe("Second number to multiply"),
    },
  },
  async ({ a, b }) => ({
    content: [
      {
        type: "text",
        text: `${a} × ${b} = ${a * b}`,
      },
    ],
  })
);

// Register the subtract tool
server.registerTool(
  "subtract",
  {
    title: "Subtraction Tool",
    description: "Subtract the second number from the first",
    inputSchema: {
      a: z.number().describe("Number to subtract from"),
      b: z.number().describe("Number to subtract"),
    },
  },
  async ({ a, b }) => ({
    content: [
      {
        type: "text",
        text: `${a} - ${b} = ${a - b}`,
      },
    ],
  })
);

// Register the divide tool
server.registerTool(
  "divide",
  {
    title: "Division Tool",
    description: "Divide the first number by the second",
    inputSchema: {
      a: z.number().describe("Number to be divided (numerator)"),
      b: z.number().describe("Number to divide by (denominator)"),
    },
  },
  async ({ a, b }) => {
    if (b === 0) {
      return {
        content: [
          {
            type: "text",
            text: "Error: Cannot divide by zero",
          },
        ],
        isError: true,
      };
    }
    return {
      content: [
        {
          type: "text",
          text: `${a} ÷ ${b} = ${a / b}`,
        },
      ],
    };
  }
);

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Math MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Fatal error in main():", error);
  process.exit(1);
});
