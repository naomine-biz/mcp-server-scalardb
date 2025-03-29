"""
Transaction-related tools for ScalarDB Cluster MCP Server

This module contains tools for executing transactions against ScalarDB Cluster.
"""

import sys
import time
from typing import Any, Dict, List

import scalardb_cluster_sql_pb2
from connection import get_sql_stub
from utils.validators import contains_semicolon, is_allowed_transaction_statement


def execute_transaction(namespace: str, statements: List[str]) -> Dict[str, Any]:
    """
    Execute multiple SQL statements in a single transaction.

    Args:
        namespace: The namespace to execute the statements against.
        statements: A list of SQL statements (INSERT, UPDATE, DELETE) to execute in a transaction.

    Returns:
        Dict containing the result of the transaction.
    """
    try:
        print(
            f"execute_transaction: Executing transaction against {namespace}: {statements}",
            file=sys.stderr,
        )

        # Start measuring execution time
        start_time = time.time()

        # Get SQL stub
        sql_stub = get_sql_stub()

        # Create request header
        request_header = scalardb_cluster_sql_pb2.RequestHeader()

        # 1. Begin transaction
        begin_request = scalardb_cluster_sql_pb2.BeginRequest(
            request_header=request_header
        )
        begin_response = sql_stub.Begin(begin_request)
        transaction_id = begin_response.transaction_id
        print(
            f"execute_transaction: Transaction started with ID: {transaction_id}",
            file=sys.stderr,
        )

        try:
            # 2. Execute each SQL statement
            results = []
            for i, statement in enumerate(statements):
                # Check if operation is allowed
                if not is_allowed_transaction_statement(statement):
                    # Rollback transaction
                    rollback_request = scalardb_cluster_sql_pb2.RollbackRequest(
                        request_header=scalardb_cluster_sql_pb2.RequestHeader(),
                        transaction_id=transaction_id,
                    )
                    sql_stub.Rollback(rollback_request)

                    return {
                        "success": False,
                        "error": f"Statement {i + 1} is not allowed. Only INSERT, UPDATE, and DELETE operations are allowed in transactions.",
                        "namespace": namespace,
                        "statements": statements,
                    }

                # Check that it doesn't contain semicolons
                if contains_semicolon(statement):
                    # Rollback transaction
                    rollback_request = scalardb_cluster_sql_pb2.RollbackRequest(
                        request_header=scalardb_cluster_sql_pb2.RequestHeader(),
                        transaction_id=transaction_id,
                    )
                    sql_stub.Rollback(rollback_request)

                    return {
                        "success": False,
                        "error": f"Statement {i + 1} contains a semicolon. Multiple SQL statements per line are not allowed.",
                        "namespace": namespace,
                        "statements": statements,
                    }

                # Execute SQL
                execute_request = scalardb_cluster_sql_pb2.ExecuteRequest(
                    request_header=scalardb_cluster_sql_pb2.RequestHeader(),
                    transaction_id=transaction_id,
                    sql=statement,
                    default_namespace_name=namespace,
                )

                print(
                    f"execute_transaction: Executing SQL ({i + 1}/{len(statements)}): {statement}",
                    file=sys.stderr,
                )
                # We don't use the execute_response result, but execution is necessary for error checking
                sql_stub.Execute(execute_request)

                # Record result
                results.append({"statement": statement, "success": True})

            # 3. Commit transaction
            commit_request = scalardb_cluster_sql_pb2.CommitRequest(
                request_header=scalardb_cluster_sql_pb2.RequestHeader(),
                transaction_id=transaction_id,
            )
            sql_stub.Commit(commit_request)
            print("execute_transaction: Transaction commit complete", file=sys.stderr)

            # End measuring execution time
            end_time = time.time()
            execution_time_ms = int((end_time - start_time) * 1000)

            # Return results
            return {
                "success": True,
                "transaction_id": transaction_id,
                "results": results,
                "execution_time_ms": execution_time_ms,
                "statement_count": len(statements),
            }

        except Exception as e:
            # Rollback transaction if an error occurred
            try:
                rollback_request = scalardb_cluster_sql_pb2.RollbackRequest(
                    request_header=scalardb_cluster_sql_pb2.RequestHeader(),
                    transaction_id=transaction_id,
                )
                sql_stub.Rollback(rollback_request)
                print(
                    "execute_transaction: Transaction rollback complete",
                    file=sys.stderr,
                )
            except Exception as rollback_error:
                print(
                    f"execute_transaction: An error occurred during rollback: {rollback_error}",
                    file=sys.stderr,
                )

            raise e

    except Exception as e:
        print(f"execute_transaction: An error occurred: {e}", file=sys.stderr)
        return {
            "success": False,
            "error": str(e),
            "namespace": namespace,
            "statements": statements,
        }
