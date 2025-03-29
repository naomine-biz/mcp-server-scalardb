"""
Query-related tools for ScalarDB Cluster MCP Server

This module contains tools for executing queries against ScalarDB Cluster.
"""

import base64
import sys
import time
from typing import Any, Dict

import scalardb_cluster_sql_pb2
from connection import get_sql_stub
from utils.validators import (
    contains_disallowed_keyword,
    contains_semicolon,
    is_select_query,
)


def execute_query(namespace: str, query: str) -> Dict[str, Any]:
    """
    Execute a query against ScalarDB.

    Args:
        namespace: The namespace to execute the query against.
        query: The SQL query to execute.

    Returns:
        Dict containing query results.
    """
    try:
        print(
            f"execute_query: Executing SQL against {namespace}: {query}",
            file=sys.stderr,
        )

        # 1. Check if it starts with SELECT
        if not is_select_query(query):
            return {
                "success": False,
                "error": "For security reasons, only SELECT operations are allowed. Only read-only queries (SELECT) can be executed.",
                "namespace": namespace,
                "query": query,
            }

        # 2. Check that it doesn't contain semicolons (prohibit multiple statements)
        if contains_semicolon(query):
            return {
                "success": False,
                "error": "For security reasons, multiple SQL statements (separated by semicolons) are not allowed.",
                "namespace": namespace,
                "query": query,
            }

        # 3. Check that it doesn't contain prohibited keywords
        has_disallowed, keyword = contains_disallowed_keyword(query)
        if has_disallowed:
            return {
                "success": False,
                "error": f"For security reasons, queries containing the {keyword} keyword are not allowed.",
                "namespace": namespace,
                "query": query,
            }

        # Start measuring execution time
        start_time = time.time()

        # Get SQL stub
        sql_stub = get_sql_stub()

        # Create request header
        request_header = scalardb_cluster_sql_pb2.RequestHeader()

        # Create ExecuteRequest
        execute_request = scalardb_cluster_sql_pb2.ExecuteRequest(
            request_header=request_header, sql=query, default_namespace_name=namespace
        )

        # Execute SQL
        print("execute_query: Executing SQL...", file=sys.stderr)
        execute_response = sql_stub.Execute(execute_request)

        # End measuring execution time
        end_time = time.time()
        execution_time_ms = int((end_time - start_time) * 1000)

        # Process results
        result_set = execute_response.result_set

        # Column definitions
        column_definitions = {}

        # Get records
        rows = []
        for record in result_set.records:
            row = {}
            for column in record.columns:
                # Get column name
                column_name = column.name

                # Get value and type (convert appropriately based on data type)
                value = None
                type = None
                if column.value.HasField("boolean_value"):
                    value = column.value.boolean_value
                    type = "boolean".upper()
                elif column.value.HasField("int_value"):
                    value = column.value.int_value
                    type = "int".upper()
                elif column.value.HasField("bigint_value"):
                    value = column.value.bigint_value
                    type = "bigint".upper()
                elif column.value.HasField("float_value"):
                    value = column.value.float_value
                    type = "float".upper()
                elif column.value.HasField("double_value"):
                    value = column.value.double_value
                    type = "double".upper()
                elif column.value.HasField("text_value"):
                    value = column.value.text_value
                    type = "text".upper()
                elif column.value.HasField("blob_value"):
                    # Base64 encode binary data for return
                    value = base64.b64encode(column.value.blob_value).decode("utf-8")
                    type = "blob".upper()
                elif column.value.HasField("date_value"):
                    value = column.value.date_value
                    type = "date".upper()
                elif column.value.HasField("time_value"):
                    value = column.value.time_value
                    type = "time".upper()
                elif column.value.HasField("timestamp_value"):
                    value = column.value.timestamp_value
                    type = "timestamp".upper()
                elif column.value.HasField("timestamptz_value"):
                    value = column.value.timestamptz_value
                    type = "timestamptz".upper()

                # Get column definition
                if (
                    column_name not in column_definitions
                    or column_definitions[column_name]["type"] != type
                ):
                    column_definitions[column_name] = {
                        "type": type,
                    }

                row[column_name] = value

            rows.append(row)

        print(
            f"execute_query: SQL execution complete. Retrieved {len(rows)} records.",
            file=sys.stderr,
        )

        # Return results
        return {
            "success": True,
            "columns": column_definitions,
            "rows": rows,
            "execution_time_ms": execution_time_ms,
            "row_count": len(rows),
        }
    except Exception as e:
        print(f"execute_query: An error occurred: {e}", file=sys.stderr)
        return {
            "success": False,
            "error": str(e),
            "namespace": namespace,
            "query": query,
        }
