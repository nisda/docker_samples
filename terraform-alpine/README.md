# terraform 


## 実行
```bash
# Dockerイメージをビルド。初回とDockerfile変更時のみ。
docker-compose build

# コンテナ起動＆ログイン
docker-compose run --rm terraform

### 以降は、Dockerコンテナの中での作業になる。

# Terraform を実行
terraform init
terraform validate
terraform plan
...

# 終了時。Dockerコンテナから抜ける。
exit
```