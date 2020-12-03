# Docker alpine-pyodbc


## 実行
```
# Dockerイメージをビルド。初回とDockerfile変更時のみ。
docker-compose build

# コンテナ起動＆ログイン
docker-compose run --rm pyodbc

### 以降はDockerコンテナの中での作業。

# お試し用 python を実行
python3 sample.py

# 終了時。Dockerコンテナから抜ける。
exit
```

## 参考
[ODBC Driver 17 to Alpine](https://docs.microsoft.com/ja-jp/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#alpine17)
