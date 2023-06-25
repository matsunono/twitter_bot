# twitter_bot

## 日本語
### 概要
twitter API v2に対応した自動つぶやきBotです．
'bot_tweet.py', 'bot_tweet_gui.py'が自動つぶやきBot本体です．
'sheet2txt.py', 'sheet2txt_gui.py'はExcelシートの各セルを自動つぶやきBotが対応しているtxt形式に変換するプログラムです．

使用時に行う作業として，'bot_tweet_gui.py'の以下33~37行目にAPI Keyが保存されたファイル名を入力してください．
デフォルトは'bearar_token.txt', 'consumer_key.txt', 'consumer_secret.txt', 'access_token_key.txt', 'access_token_secret.txt'です．
**API Keyが保存されたファイルがあるフォルダとツイート内容のファイルがあるフォルダは必ず分けてください．**
