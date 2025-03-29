#!/usr/bin/env python3
"""
ScalarDB Cluster Connection Module

This module handles the connection to ScalarDB Cluster.
"""

import os
import sys

import grpc

# Import ScalarDB Cluster gRPC modules
import scalardb_cluster_pb2
import scalardb_cluster_pb2_grpc
import scalardb_cluster_sql_pb2_grpc

# ScalarDB Cluster endpoint configuration
SCALARDB_CLUSTER_ENDPOINT = os.getenv("SCALARDB_CLUSTER_ENDPOINT")

# Initialize connection and stubs as None
channel = None
admin_stub = None
sql_stub = None

# Connection status
is_connected = False


def initialize_connection():
    """Initialize connection to ScalarDB Cluster"""
    global channel, admin_stub, sql_stub, is_connected

    try:
        # Create a gRPC channel and client stubs for ScalarDB Cluster
        print(f"Connecting to ScalarDB Cluster: {SCALARDB_CLUSTER_ENDPOINT}")
        channel = grpc.insecure_channel(SCALARDB_CLUSTER_ENDPOINT)
        admin_stub = scalardb_cluster_pb2_grpc.DistributedTransactionAdminStub(channel)
        sql_stub = scalardb_cluster_sql_pb2_grpc.SqlTransactionStub(channel)

        # Connection test
        request_header = scalardb_cluster_pb2.RequestHeader()
        request = scalardb_cluster_pb2.GetNamespaceNamesRequest(
            request_header=request_header
        )
        admin_stub.GetNamespaceNames(request)
        print("Successfully connected to ScalarDB Cluster")
        is_connected = True
        return True
    except Exception as e:
        print(f"Failed to connect to ScalarDB Cluster: {e}", file=sys.stderr)
        is_connected = False
        return False


def get_admin_stub():
    """Get the admin stub"""
    if not is_connected:
        initialize_connection()
    return admin_stub


def get_sql_stub():
    """Get the SQL stub"""
    if not is_connected:
        initialize_connection()
    return sql_stub
