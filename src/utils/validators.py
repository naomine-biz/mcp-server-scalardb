"""
Validator functions for ScalarDB Cluster MCP Server

This module contains validation functions for SQL queries and transactions.
"""

import re


def is_select_query(query):
    """
    Check if the query is a SELECT query.

    Args:
        query: The SQL query to check.

    Returns:
        bool: True if the query is a SELECT query, False otherwise.
    """
    query_upper = query.strip().upper()
    return query_upper.startswith("SELECT")


def contains_semicolon(query):
    """
    Check if the query contains a semicolon.

    Args:
        query: The SQL query to check.

    Returns:
        bool: True if the query contains a semicolon, False otherwise.
    """
    return ";" in query


def contains_disallowed_keyword(query):
    """
    Check if the query contains a disallowed keyword.

    Args:
        query: The SQL query to check.

    Returns:
        tuple: (bool, keyword) where bool is True if the query contains a disallowed keyword,
               and keyword is the disallowed keyword found (or None if no disallowed keyword is found).
    """
    disallowed_keywords = [
        "UPDATE",
        "DELETE",
        "INSERT",
        "DROP",
        "ALTER",
        "CREATE",
        "TRUNCATE",
        "GRANT",
        "REVOKE",
        "EXEC",
        "EXECUTE",
        "UNION",
    ]

    query_upper = query.strip().upper()

    for keyword in disallowed_keywords:
        if contains_word(query_upper, keyword):
            return True, keyword

    return False, None


def contains_word(text, word):
    """
    Check if the text contains the word as a whole word.

    Args:
        text: The text to check.
        word: The word to look for.

    Returns:
        bool: True if the text contains the word, False otherwise.
    """
    pattern = r"\b" + re.escape(word) + r"\b"
    return bool(re.search(pattern, text))


def is_allowed_transaction_statement(statement):
    """
    Check if the statement is allowed in a transaction.

    Args:
        statement: The SQL statement to check.

    Returns:
        bool: True if the statement is allowed, False otherwise.
    """
    statement_upper = statement.strip().upper()
    allowed_operations = ["INSERT", "UPDATE", "DELETE"]

    for operation in allowed_operations:
        if statement_upper.startswith(operation):
            return True

    return False
