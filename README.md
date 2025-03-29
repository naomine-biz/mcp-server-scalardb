# ScalarDB Cluster MCP Server

ScalarDB Cluster 用の Model Context Protocol (MCP) サーバーです。このサーバーは、ScalarDB Cluster との対話を可能にするツールとリソースを提供します。

## 機能

この MCP サーバーは以下の機能を提供します：

### ツール

- `get_schema(namespace)`: 指定された名前空間のスキーマ情報を取得します
- `list_namespaces()`: 利用可能な名前空間の一覧を取得します
- `list_tables(namespace)`: 指定された名前空間内のテーブル一覧を取得します
- `execute_query(namespace, query)`: ScalarDB に対して SELECT クエリを実行します
- `execute_transaction(namespace, statements)`: ScalarDB に対して複数のステートメント（INSERT, UPDATE, DELETE）をトランザクションとして実行します

## インストール

詳細なインストール手順については、[INSTALL.md](INSTALL.md)を参照してください。

必要な依存関係をインストールします：

```bash
pip install -r src/requirements.txt
```

## 使用方法

### 環境変数の設定

ScalarDB Cluster への接続には、以下の環境変数を設定する必要があります：

```bash
export SCALARDB_CLUSTER_ENDPOINT="localhost:60053"
```

### 開発モード

開発モードでサーバーを起動するには：

```bash
python src/main.py
```

または、提供されているスクリプトを使用：

```bash
./src/start_server.sh
```

### Claude Desktop との統合

Claude Desktop でこのサーバーを使用するには、Claude Desktop の設定ファイルにこのサーバーを追加します。

### MCP Inspector でのテスト

MCP Inspector を使用してサーバーをテストするには：

```bash
mcp dev src/main.py
```

## 実装の詳細

このサーバーは ScalarDB Cluster の gRPC API を使用して、データベースとの対話を行います。セキュリティ上の理由から、`execute_query` は SELECT クエリのみを許可し、`execute_transaction` は INSERT、UPDATE、DELETE ステートメントのみを許可します。

## 例

### スキーマ情報の取得

```python
# ツール: get_schema
# パラメータ:
# - namespace: "my_namespace"
```

### 名前空間の一覧取得

```python
# ツール: list_namespaces
```

### テーブルの一覧取得

```python
# ツール: list_tables
# パラメータ:
# - namespace: "my_namespace"
```

### クエリの実行

```python
# ツール: execute_query
# パラメータ:
# - namespace: "my_namespace"
# - query: "SELECT * FROM users LIMIT 10"
```

### トランザクションの実行

```python
# ツール: execute_transaction
# パラメータ:
# - namespace: "my_namespace"
# - statements: [
#     "INSERT INTO users (id, name) VALUES (1, 'Alice')",
#     "UPDATE users SET age = 30 WHERE id = 1"
#   ]
```

## 依存関係

- Python 3.8 以上
- MCP SDK 1.5.0 以上
- Uvicorn 0.27.0 以上
- Protobuf 5.29.3
