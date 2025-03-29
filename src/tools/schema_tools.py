"""
Schema-related tools for ScalarDB Cluster MCP Server

This module contains tools for retrieving schema information from ScalarDB Cluster.
"""

import json
import sys

import scalardb_cluster_pb2
from connection import get_admin_stub


def get_schema(namespace: str) -> str:
    """
    Get the schema information for a specific namespace in ScalarDB.

    Args:
        namespace: The namespace to retrieve schema information for.

    Returns:
        JSON string containing schema information.
    """
    try:
        print(f"get_schema: Retrieving schema for {namespace}", file=sys.stderr)

        # Get admin stub
        admin_stub = get_admin_stub()

        # 1. First, get the list of table names in the namespace
        request_header = scalardb_cluster_pb2.RequestHeader()
        table_names_request = scalardb_cluster_pb2.GetNamespaceTableNamesRequest(
            request_header=request_header, namespace_name=namespace
        )
        print("get_schema: Retrieving table name list...", file=sys.stderr)
        table_names_response = admin_stub.GetNamespaceTableNames(table_names_request)

        # 2. Get metadata for each table
        tables = []
        for table_name in table_names_response.table_names:
            print(
                f"get_schema: Retrieving metadata for table '{table_name}'...",
                file=sys.stderr,
            )
            metadata_request = scalardb_cluster_pb2.GetTableMetadataRequest(
                request_header=scalardb_cluster_pb2.RequestHeader(),
                namespace_name=namespace,
                table_name=table_name,
            )
            try:
                metadata_response = admin_stub.GetTableMetadata(metadata_request)
                table_metadata = metadata_response.table_metadata

                # 3. Convert table metadata to JSON format
                columns = []
                for col_name, col_type in table_metadata.columns.items():
                    columns.append(
                        {
                            "name": col_name,
                            "type": scalardb_cluster_pb2.DataType.Name(
                                col_type
                            ).replace("DATA_TYPE_", ""),
                        }
                    )

                table_info = {
                    "name": table_name,
                    "partition_key": list(table_metadata.partition_key_column_names),
                    "clustering_key": list(table_metadata.clustering_key_column_names),
                    "columns": columns,
                }

                # Add clustering order if present
                if table_metadata.clustering_orders:
                    clustering_orders = {}
                    for col_name, order in table_metadata.clustering_orders.items():
                        clustering_orders[col_name] = (
                            scalardb_cluster_pb2.ClusteringOrder.Name(order).replace(
                                "CLUSTERING_ORDER_", ""
                            )
                        )
                    table_info["clustering_orders"] = clustering_orders

                # Add secondary indexes if present
                if table_metadata.secondary_index_column_names:
                    table_info["secondary_indexes"] = list(
                        table_metadata.secondary_index_column_names
                    )

                # Add encrypted columns if present
                if table_metadata.encrypted_columns:
                    table_info["encrypted_columns"] = list(
                        table_metadata.encrypted_columns
                    )

                tables.append(table_info)
            except Exception as table_error:
                print(
                    f"get_schema: Error retrieving metadata for table '{table_name}': {table_error}",
                    file=sys.stderr,
                )
                # Record error for this table but continue processing
                tables.append({"name": table_name, "error": str(table_error)})

        # 4. Build the final schema
        schema = {"namespace": namespace, "tables": tables}
        print("get_schema: Schema construction complete", file=sys.stderr)

        return json.dumps(schema, indent=2)
    except Exception as e:
        # Return error information if an error occurred
        print(f"get_schema: Overall error: {e}", file=sys.stderr)
        error_schema = {
            "namespace": namespace,
            "error": str(e),
            "note": "An error occurred while connecting to ScalarDB.",
        }
        return json.dumps(error_schema, indent=2)


def list_namespaces() -> dict:
    """
    Get a list of all namespace names in ScalarDB Cluster.

    Returns:
        Dict containing the list of namespace names.
    """
    try:
        # Get admin stub
        admin_stub = get_admin_stub()

        # Create a request header
        request_header = scalardb_cluster_pb2.RequestHeader()

        # Create the request
        request = scalardb_cluster_pb2.GetNamespaceNamesRequest(
            request_header=request_header
        )

        # Call the gRPC method
        response = admin_stub.GetNamespaceNames(request)

        # Return the namespace names
        return {
            "success": True,
            "namespace_names": list(response.namespace_names),
            "count": len(response.namespace_names),
        }
    except Exception as e:
        # In case of error, return error information
        return {"success": False, "error": str(e)}


def list_tables(namespace: str) -> dict:
    """
    Get a list of all table names in a namespace in ScalarDB Cluster.

    Args:
        namespace: The namespace to retrieve table names for.

    Returns:
        Dict containing the list of table names in the specified namespace.
    """
    try:
        # Get admin stub
        admin_stub = get_admin_stub()

        # Create a request header
        request_header = scalardb_cluster_pb2.RequestHeader()

        # Create the request
        request = scalardb_cluster_pb2.GetNamespaceTableNamesRequest(
            request_header=request_header, namespace_name=namespace
        )

        # Call the gRPC method
        response = admin_stub.GetNamespaceTableNames(request)

        # Return the table names
        return {
            "success": True,
            "namespace": namespace,
            "table_names": list(response.table_names),
            "count": len(response.table_names),
        }
    except Exception as e:
        # In case of error, return error information
        return {"success": False, "error": str(e)}
