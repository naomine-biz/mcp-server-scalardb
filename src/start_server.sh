#!/bin/bash

# Start the ScalarDB Cluster MCP server

# スクリプトのディレクトリを取得
SCRIPT_DIR="$(dirname "$0")"
# リポジトリのルートディレクトリを取得（スクリプトは src/ ディレクトリにある）
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
# 仮想環境のパス
VENV_DIR="$ROOT_DIR/venv"

# 仮想環境が存在するか確認
if [ -d "$VENV_DIR" ]; then
    echo "仮想環境を使用します: $VENV_DIR"

    # 仮想環境をアクティベート
    if [ -f "$VENV_DIR/bin/activate" ]; then
        # macOS/Linux
        source "$VENV_DIR/bin/activate"
    elif [ -f "$VENV_DIR/Scripts/activate" ]; then
        # Windows（Git Bash等で実行する場合）
        source "$VENV_DIR/Scripts/activate"
    else
        echo "警告: 仮想環境のアクティベーションスクリプトが見つかりません。システムのPythonを使用します。"
    fi
else
    echo "警告: 仮想環境が見つかりません。システムのPythonを使用します。"
    echo "仮想環境を作成するには: python -m venv $VENV_DIR"
fi

# スクリプトのディレクトリに移動
cd "$SCRIPT_DIR"

# Pythonスクリプトを実行
python main.py
