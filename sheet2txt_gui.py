import PySimpleGUI as sg
import sheet2txt

# テーマカラー
sg.theme('DarkBlue')
# ウィンドウ内のレイアウト
layout = [  [sg.Text('Excelファイルをtextファイルに変換するよ')],
            [sg.Text('変換するファイル'), sg.InputText(key = '-File_Place-'),sg.FileBrowse(key = '-File-', target= '-File_Place-')],
            [sg.Button('START', key = '-Btn_Start-'), sg.Button('Cancel', key = '-Btn_Cancel-')] ]

# ウィンドウを生成する
window = sg.Window('Excel To Text', layout)

# "events"を処理するためのイベントループとインプットの"valuesを取得する処理
while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == '-Btn_Cancel-': # if user closes window or clicks cancel
        break
    elif event == '-Btn_Start-': # if user clicks START
        in_path = values['-File_Place-']
        sheet2txt.Read_Book(in_path)

window.close()