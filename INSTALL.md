# ScalarDB Cluster MCP Server インストールガイド

このガイドでは、ScalarDB Cluster MCP Serverをnpxパッケージとしてインストールして使用する方法を説明します。

## 前提条件

- Node.js 16.x 以上
- npm 7.x 以上
- Python 3.8 以上
- pip 20.x 以上

## インストール手順

### 1. リポジトリのクローン

まず、リポジトリをローカルマシンにクローンします：

```bash
git clone https://github.com/your-username/scalardb-cluster-mcp-server.git
cd scalardb-cluster-mcp-server
```

### 2. Python 依存関係のインストール

必要なPythonパッケージをインストールします：

```bash
pip install -r requirements.txt
```

### 3. npx パッケージとしてインストール

ローカルディレクトリをnpxパッケージとしてインストールするには、以下のコマンドを実行します：

```bash
# package.jsonがない場合は作成
npm init -y

# bin フィールドを追加して、start_server.shを実行可能にする
npm pkg set bin.scalardb-cluster-mcp="./start_server.sh"

# パッケージをグローバルにインストール
npm install -g .
```

これにより、`scalardb-cluster-mcp`コマンドがグローバルに利用可能になります。

## 使用方法

### 環境変数の設定

ScalarDB Clusterに接続するには、以下の環境変数を設定します：

```bash
export SCALARDB_CLUSTER_ENDPOINT="localhost:60053"
```

### サーバーの起動

インストール後、以下のコマンドでサーバーを起動できます：

```bash
npx scalardb-cluster-mcp
```

または、グローバルにインストールした場合：

```bash
scalardb-cluster-mcp
```

### Claude Desktop との統合

Claude Desktopの設定ファイル（通常は`~/Library/Application Support/Claude/claude_desktop_config.json`）に以下の設定を追加します：

```json
{
  "mcpServers": {
    "scalardb-cluster": {
      "command": "npx",
      "args": ["scalardb-cluster-mcp"],
      "env": {
        "SCALARDB_CLUSTER_ENDPOINT": "localhost:60053"
      },
      "disabled": false
    }
  }
}
```

## トラブルシューティング

### 権限エラー

`start_server.sh`の実行権限がない場合は、以下のコマンドで権限を付与します：

```bash
chmod +x start_server.sh
```

### 接続エラー

ScalarDB Clusterに接続できない場合は、以下を確認してください：

1. ScalarDB Clusterが実行中であること
2. `SCALARDB_CLUSTER_ENDPOINT`環境変数が正しく設定されていること
3. ファイアウォールやネットワーク設定が接続を許可していること

## アンインストール

パッケージをアンインストールするには：

```bash
npm uninstall -g scalardb-cluster-mcp
```
