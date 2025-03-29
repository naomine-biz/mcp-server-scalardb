#!/usr/bin/env python3
"""
ScalarDB Cluster MCP Server

This MCP server provides tools and resources for interacting with ScalarDB Cluster.
"""

import sys

from connection import initialize_connection
from mcp.server.fastmcp import FastMCP
from tools import (
    execute_query,
    execute_transaction,
    get_schema,
    list_namespaces,
    list_tables,
)

# Create an MCP server
mcp = FastMCP("ScalarDB-Cluster")

# Initialize connection to ScalarDB Cluster
if not initialize_connection():
    print(
        "Failed to connect to ScalarDB Cluster. Tools will not work properly.",
        file=sys.stderr,
    )
    # Don't exit here to allow MCP dev mode to work

# Register tools
mcp.tool()(get_schema)
mcp.tool()(list_namespaces)
mcp.tool()(list_tables)
mcp.tool()(execute_query)
mcp.tool()(execute_transaction)


if __name__ == "__main__":
    # Let the MCP SDK handle the command line arguments
    # Run the MCP server
    mcp.run()
