# 気象庁 週間天気 スクレイピング

気象庁の週間天気予報ページをスクレイピングして、JSON で返却するアプリケーションです。

<https://www.jma.go.jp/bosai/forecast/>

## 使い方

### 全地点の予報を取得する

<http://localhost:5000> のようにエンドポイントなしでアクセスすると、すべての地点の週間天気予報を返却します。

### 指定した地点の予報を取得する

<http://localhost:5000/sapporo> のようにエンドポイントを指定すると、指定した地点の週間天気予報のみを返却します。

存在しない地点名を指定すると、400エラーが返ります。

### 使用できる地点一覧

| 地点名 | エンドポイント名 |
| --- | --- |
| 釧路 | kushiro |
| 旭川 | asahikawa |
| 札幌 | sapporo |
| 青森 | aomori |
| 秋田 | akita |
| 仙台 | sendai |
| 新潟 | niigata |
| 金沢 | kanazawa |
| 東京 | toukyou |
| 宇都宮 | utsunomiya |
| 長野 | nagano |
| 名古屋 | nagoya |
| 大阪 | oosaka |
| 高松 | takamatsu |
| 松江 | matsue |
| 広島 | hiroshima |
| 高知 | kouchi |
| 福岡 | fukuoka |
| 鹿児島 | kagoshima |
| 奄美 | amami |
| 那覇 | naha |
| 石垣 | ishigaki |

## はじめに

本アプリケーションはDocker上で動作します。

リポジトリをクローンし、build してから立ち上げてください。

```
$ docker compose build
$ docker compose up -d
```

## 所感

- Python 独自の構文に未だに翻弄されています
- MVCを意識しました。が、少し乱れている気がします
- 気象庁がCSRになっていて、スクレイピングにChrome Engineを使用せざるをえず、Docker上で動作させるのに少し手間取りました
- 地点名の英語表記やIDが取得できなかったため、pykakasiでローマ字変換しエンドポイントにしました
- エラー時HTTPエラーをしっかり返すように実装しています
- 総工数1日工ちょっとかかりました。まだまだなので精進します
