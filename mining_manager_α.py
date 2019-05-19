import sys
import tkinter as tk
from calculate.organize import DataManage
from calculate.setting import InitOrePrice
from calculate.calculater import BalanceCalculate
from calculate.write import WriteFile

root = tk.Tk()

#表示関係
# title
root.title(u'minig_manager[α]')

#window size
root.geometry('800x500')

#Paste
Paste_label = tk.Label(text = u'戦利品ウィンドウをペースト')
Paste_label.place(x = 30,y = 30)
Paste_list = tk.Text()
Paste_list.place(x = 30,y = 60)

#title
Title_label = tk.Label(text = u'出力ファイルタイトル')
Title_label.place(x = 630,y = 30)
Title_entry = tk.Entry(width = 20)
Title_entry.place(x = 630,y = 60)

#ignore
Ignore_label = tk.Label(text = u'除外キャラクター')
Ignore_label.place(x = 630,y = 240)
Ignore_list = tk.Text(width = 18,height = 8)
Ignore_list.place(x = 630,y = 270)


#処理関係
#ボタン押下時の処理
def Button_pushed():

    #各入力データの取得
    Title = Title_entry.get()
    Loot = Paste_list.get('1.0', 'end -1c')
    Ignore = Ignore_list.get('1.0', 'end -1c')

    #各入力データの整理
    data_organize = DataManage(Loot,Title,Ignore)
    loot_list = data_organize.LootTrim()
    ignore_list = data_organize.IgnoreTrim()
    Trimed_list = data_organize.ReflectIgnore(loot_list,ignore_list)

    calculate = BalanceCalculate(Trimed_list)
    balances = calculate.balances()

    write_file = WriteFile(balances,Title)
    write_file.output()

#submit_button
submit_button = tk.Button(text = u'出力',width = 10,command = Button_pushed,fg = "#ff0000")
submit_button.place(x = 650,y = 450)

root.mainloop()
