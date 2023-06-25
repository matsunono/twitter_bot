# twitter_bot

## 日本語
### 概要
twitter API v2に対応した自動つぶやきBotです．
'bot_tweet.py', 'bot_tweet_gui.py'が自動つぶやきBot本体です．
'sheet2txt.py', 'sheet2txt_gui.py'はExcelシートの各セルを自動つぶやきBotが対応しているtxt形式に変換するプログラムです．

使用時に行う作業として，'bot_tweet_gui.py'の以下5行にAPI Keyを入力してください．
* bearar_token = 'hogehoge'
* consumer_key = 'piyopiyo'
* consumer_secret = 'piyopiyo'
* access_token_key = 'hugahuga'
* access_token_secret = 'hugahuga'

この作業は今後は個人でAPI Keyを保存したファイルからの読み込みに変更予定です．
