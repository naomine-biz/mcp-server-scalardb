#!/bin/bash

# Start the ScalarDB Cluster MCP server

# スクリプトのディレクトリを取得（シンボリックリンクを考慮）
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "$0" || echo "$0")")" && pwd)"
# リポジトリのルートディレクトリを取得（スクリプトは src/ ディレクトリにある）
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
# 仮想環境のパス
VENV_DIR="$ROOT_DIR/venv"
# requirements.txtのパス
REQUIREMENTS_PATH="$SCRIPT_DIR/requirements.txt"

echo "スクリプトディレクトリ: $SCRIPT_DIR"
echo "requirements.txtのパス: $REQUIREMENTS_PATH"

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

# requirements.txtファイルの存在確認
if [ ! -f "$REQUIREMENTS_PATH" ]; then
    echo "エラー: requirements.txtファイルが見つかりません: $REQUIREMENTS_PATH"
    exit 1
fi

# 必要なパッケージをインストール
echo "必要なパッケージをインストールしています..."
pip install -r "$REQUIREMENTS_PATH"
if [ $? -ne 0 ]; then
    echo "エラー: パッケージのインストールに失敗しました。"
    exit 1
fi
echo "パッケージのインストールが完了しました。"

# Pythonスクリプトを実行
python "$SCRIPT_DIR/main.py"
