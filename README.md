# コンテナ起動手順

## .envファイルをPJディレクトリに作成
```
MYSQL_DB_NAME=＜アプリで使用するテーブルの名前＞
MYSQL_TEST_DB_NAME=test_＜アプリで使用するテーブルの名前＞
MYSQL_ROOT_PASSWORD=＜rootユーザーのパスワード＞
MYSQL_APP_USER=＜appユーザーの名前＞
MYSQL_APP_USER_PASSWORD=＜appユーザーのパスワード＞
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_ENGINE=django.db.backends.mysql
```

## dockerコマンドを実行
```
mkdir -p mysql/data
docker build -t django_mysql_image .
docker container run \
  --name django_mysql_container \
  -p 8081:8080 \
  -v /path/to/your/local/directory:/var/lib/mysql \
  django_mysql_image
```

# docker hubからイメージを取得して実行
```
docker pull genji1/django-tutorial
docker container run \
  --name django_mysql_container \
  -p 8081:8080 \
  -v /path/to/your/local/directory:/var/lib/mysql \
  genji1/django-tutorial
```

# APIの使用方法

## 1. 登録された衣服の一覧を取得

### リクエスト
- **メソッド**: GET
- **エンドポイント**: `/api/clothes/`
- **リクエストパラメータ**: なし

### レスポンス
- **ステータスコード**: 200 OK
- **レスポンスボディ**:
    ```json
    [
      {
        "id": 1,
        "name": "シャツ",
        "price": 3000,
        "description": "コットンシャツ"
      },
      {
        "id": 2,
        "name": "ジーンズ",
        "price": 5000,
        "description": "デニムジーンズ"
      }
      // その他の衣服情報
    ]
    ```

## 2. 新しい衣服を登録

### リクエスト
- **メソッド**: POST
- **エンドポイント**: `/api/clothes/`
- **リクエストボディ**:
    ```json
    {
        "name": "Tシャツ",
        "price": 2000,
        "description": "綿100%のTシャツ"
    }
    ```

### レスポンス
- **ステータスコード**: 201 Created
- **レスポンスボディ**:
    ```json
    {
      "id": 3,
      "name": "Tシャツ",
      "price": 2000,
      "description": "綿100%のTシャツ"
    }
    ```

## 3. 登録済み衣服の値段を変更

### リクエスト
- **メソッド**: PUT
- **エンドポイント**: `/api/clothes/{id}/`
- **リクエストパラメータ**:
  - id: 変更したい衣服のID (例: 1)
- **リクエストボディ**:
    ```json
    {
      "price": 3500
    }
    ```

### レスポンス
- **ステータスコード**: 200 OK
- **レスポンスボディ**:
    ```json
    {
      "id": 1,
      "name": "シャツ",
      "price": 3500,
      "description": "コットンシャツ"
    }
    ```

## 4. 登録済み衣服を削除

### リクエスト
- **メソッド**: DELETE
- **エンドポイント**: `/api/clothes/{id}/`
- **リクエストパラメータ**:
  - id: 削除したい衣服のID (例: 2)

### レスポンス
- **ステータスコード**: 204 No Content
- **レスポンスボディ**: なし
