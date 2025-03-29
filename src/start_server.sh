#!/bin/bash

# Start the ScalarDB Cluster MCP server

# スクリプトのディレクトリを取得
SCRIPT_DIR="$(dirname "$0")"
# リポジトリのルートディレクトリを取得（スクリプトは src/ ディレクトリにある）
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
# 仮想環境のパス
VENV_DIR="$ROOT_DIR/venv"

# 仮想環境が存在するか確認
if [ ! -d "$VENV_DIR" ]; then
    echo "仮想環境が見つかりません。新しく作成します: $VENV_DIR"
    python -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "エラー: 仮想環境の作成に失敗しました。"
        exit 1
    fi
    echo "仮想環境を作成しました: $VENV_DIR"
fi

# 仮想環境をアクティベート
if [ -f "$VENV_DIR/bin/activate" ]; then
    # macOS/Linux
    source "$VENV_DIR/bin/activate"
elif [ -f "$VENV_DIR/Scripts/activate" ]; then
    # Windows（Git Bash等で実行する場合）
    source "$VENV_DIR/Scripts/activate"
else
    echo "エラー: 仮想環境のアクティベーションスクリプトが見つかりません。"
    exit 1
fi

# スクリプトのディレクトリに移動
cd "$SCRIPT_DIR"

# 必要なパッケージをインストール
echo "必要なパッケージをインストールしています..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "エラー: パッケージのインストールに失敗しました。"
    exit 1
fi
echo "パッケージのインストールが完了しました。"

# Pythonスクリプトを実行
python main.py
