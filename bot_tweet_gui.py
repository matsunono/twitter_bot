import PySimpleGUI as sg
import bot_tweet

twrand_num = 0
main_flag = False
tw_flag = False

# テーマカラー
sg.theme('DarkBlue')
# ウィンドウ内のレイアウト
layout = [  [sg.Text('ランダムにツイートするよ')],
            [sg.Text('API Keyの保存フォルダ'), sg.InputText(key = '-KeyFile_Place-'),sg.FolderBrowse(key = '-KeyFolder-', target= '-KeyFile_Place-')],
            [sg.Text('ツイート用ファイルの保存フォルダ'), sg.InputText(key = '-TwFile_Place-'),sg.FolderBrowse(key = '-TwFolder-', target= '-TwFile_Place-')],
            [sg.Text('ツイート頻度'), sg.Spin(values=[i for i in range(1, 25)], key='-Spin_Freq-', size = 2), sg.Text('時間ごと')],
            [sg.Button('START', key = '-Btn_Start-'),sg.Button('STOP', key = '-Btn_Stop-', disabled = True), sg.Button('Cancel', key = '-Btn_Cancel-')] ]

# ウィンドウを生成する
window = sg.Window('Auto Tweet', layout)

# "events"を処理するためのイベントループとインプットの"valuesを取得する処理
while True:
    event, values = window.read(timeout=10)

    if event == sg.WIN_CLOSED or event == '-Btn_Cancel-': # if user closes window or clicks cancel
        break
    elif event == '-Btn_Start-': # if user clicks START
        tw_in_path = values['-TwFile_Place-']
        key_in_path = values['-KeyFile_Place-']
        freq = values['-Spin_Freq-']
        tw_flag = True
        window['-Btn_Start-'].update(disabled=True)
        window['-Btn_Stop-'].update(disabled=False)
        bearar_token = bot_tweet.Read_Text(key_in_path + '/bearar_token.txt')
        consumer_key = bot_tweet.Read_Text(key_in_path + '/consumer_key.txt')
        consumer_secret = bot_tweet.Read_Text(key_in_path + '/consumer_secret.txt')
        access_token_key = bot_tweet.Read_Text(key_in_path + '/access_token_key.txt')
        access_token_secret = bot_tweet.Read_Text(key_in_path + '/access_token_secret.txt')
        client = bot_tweet.Set_Client(bearar_token, 
                                        consumer_key, 
                                        consumer_secret, 
                                        access_token_key, 
                                        access_token_secret)
    elif event == '-Btn_Stop-': # if user clicks STOP
        tw_flag = False
        window['-Btn_Start-'].update(disabled=False)
        window['-Btn_Stop-'].update(disabled=True)

    if tw_flag: # from when start is pressed until when stop is pressed
        main_flag, twrand_num = bot_tweet.Tweet_Commander(client, 
                                                                  tw_in_path, 
                                                                  main_flag, 
                                                                  twrand_num, 
                                                                  freq)

window.close()