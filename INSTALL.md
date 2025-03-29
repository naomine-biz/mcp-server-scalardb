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
git clone https://github.com/naomine-biz/mcp-server-scalardb.git
cd mcp-server-scalardb
```

### 2. Python 仮想環境のセットアップと依存関係のインストール

Python仮想環境を作成し、必要なパッケージをインストールします：

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境のアクティベート
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# 依存関係のインストール
pip install -r src/requirements.txt
```

仮想環境を使用することで、システム全体のPython環境に影響を与えずに依存関係をインストールできます。

#### 依存関係の更新

依存関係が更新された場合や、既に仮想環境を作成している場合は、以下のコマンドで依存関係を更新できます：

```bash
# 仮想環境のアクティベート（まだアクティベートしていない場合）
source venv/bin/activate

# 依存関係の更新
pip install -r src/requirements.txt --upgrade
```

### 3. npx パッケージとしてインストール

ローカルディレクトリをnpxパッケージとしてインストールするには、以下のコマンドを実行します：

```bash
# package.jsonがない場合は作成
npm init -y

# bin フィールドを追加して、start_server.shを実行可能にする
npm pkg set bin.scalardb-cluster-mcp="./src/start_server.sh"

# パッケージをローカルにインストール
npm install
```

これにより、`npx scalardb-cluster-mcp`コマンドを使用してローカルでサーバーを起動できるようになります。

### 4. npm グローバルパッケージとしてインストール

このパッケージをグローバルにインストールして、システム全体で使用できるようにするには、以下のコマンドを実行します：

```bash
# リポジトリのルートディレクトリで実行
npm install -g .
```

インストール後、任意のディレクトリから以下のコマンドでサーバーを起動できます：

```bash
scalardb-cluster-mcp
```

注意: グローバルインストールを行う前に、`src/start_server.sh`に実行権限があることを確認してください：

```bash
chmod +x src/start_server.sh
```

## 使用方法

### 環境変数の設定

ScalarDB Clusterに接続するには、以下の環境変数を設定します：

```bash
export SCALARDB_CLUSTER_ENDPOINT="localhost:60053"
```

### サーバーの起動

#### 仮想環境を使用する方法（推奨）

サーバーを起動するには以下の方法があります：

1. **start_server.shスクリプトを使用（最も簡単）**:

```bash
# スクリプトは自動的に仮想環境を検出してアクティベートします
./src/start_server.sh
```

2. **手動で仮想環境をアクティベートしてからPythonスクリプトを実行**:

```bash
# 仮想環境のアクティベート
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Pythonスクリプトを直接実行
python src/main.py
```

#### npxパッケージを使用する方法

インストール後、以下のコマンドでサーバーを起動できます：

```bash
npx scalardb-cluster-mcp
```

注意: npxパッケージを使用する場合も、内部的にstart_server.shスクリプトが実行され、自動的に仮想環境が使用されます。

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
chmod +x src/start_server.sh
```

### 接続エラー

ScalarDB Clusterに接続できない場合は、以下を確認してください：

1. ScalarDB Clusterが実行中であること
2. `SCALARDB_CLUSTER_ENDPOINT`環境変数が正しく設定されていること
3. ファイアウォールやネットワーク設定が接続を許可していること

## アンインストール

パッケージをアンインストールするには：

```bash
# プロジェクトディレクトリで実行
npm uninstall
```
