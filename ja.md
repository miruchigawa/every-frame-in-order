# Every Wataten Frame In Order

<img src="wataten.jpeg" width="150px" align="right" />

このコードはMoviePyとPillowを使用して、Watatenの各フレームを自動でTelegramグループやFacebookページに投稿します。 ~~このプログラムは写真をTelegramグループやチャンネルにのみ投稿することに注意してください。そして、以前はFacebookのようなプラットフォームへの投稿もサポートしていませんでした（以前はメタAPIの構成にスキルの問題がありました）。~~ 今は両方がサポートされています。

# セットアップ手順
1. このプロジェクトをクローンします
    ```bash
    git clone https://github.com/miruchigawa/every-frame-in-order
    ```
2. 必要なすべての依存関係をインストールします
    ```bash
    pip install -r REQUIREMENTS.txt
    ```
3. `config.py.example`を`config.py`にコピーし、必要なデータを入力します。
4. `chat_id`を次のURLを訪れて見つけます
    ```url
    https://api.telegram.org/bot{telegram_key}/getUpdates
    ```
5. chat_idが見つからない場合は、メッセージを送信して再確認してください。

6. プログラムを実行します
    ```bash
    python3 main.py
    ```

# 未完了の作業
- [ ] 支店/投票のサポート
- [ ] 自動クロンジョブ
- [x] チャンネルのサポート
- [x] Facebookメソッドのサポートが追加されました

質問があれば、Facebookでチャットしてください：[me](https://www.facebook.com/mirudev.jp)