import sys
import os
from dotenv import load_dotenv

# アプリケーションのパスを設定
sys.path.insert(0, "/var/www/num-0145/")

# .envファイルを読み込む
load_dotenv(os.path.join('/var/www/num-0145', '.env'))

# Flaskアプリケーションのインポート
from app import app as application  # 'myapp'はアプリケーションのPythonファイル名

if __name__ == "__main__":
    application.run()
