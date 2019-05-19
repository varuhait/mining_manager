from . import setting

#各データの整理に関するクラス
class DataManage:
    def __init__(self,loot_data,title_data,ignore_data):
        self.loot_data = loot_data
        self.title_data = title_data
        self.ignore_data = ignore_data

    #Loot品整理
    #戦利品ウィンドウからコピペしたデータから余分な部分を削除する
    def LootTrim(self):

        #リストへの整理
        Loot_info = []
        raw_loot = self.loot_data
        raw_loot = raw_loot.split("\n")
        for i in range(len(raw_loot)):
            Loot_info.append(raw_loot[i].split(" "))

        #余分な要素を削除(及び取得アイテム数のint化)
        for i in range(len(Loot_info)):
            del Loot_info[i][0]
            del Loot_info[i][-1]
            if Loot_info[i][1] == "が":
                Loot_info[i][2] = int(Loot_info[i][2].replace(",",""))
            else:
                Loot_info[i][3] = int(Loot_info[i][3].replace(",",""))
            Loot_info[i].remove("が")
            Loot_info[i].remove("x")

        return Loot_info

    #IgnorePlayer整理
    #Ignorelistからのデータをリスト化する
    def IgnoreTrim(self):
        ignore_info = []
        raw_ignore = self.ignore_data
        raw_ignore = raw_ignore.split("\n")
        for i in range(len(raw_ignore)):
            ignore_info.append(raw_ignore[i].split(" "))

        return ignore_info

    #無視プレイヤーの反映、鉱石以外のアイテムの除去、鉱石、プレイヤー名の結合
    def ReflectIgnore(self,loot_list,ignore_list):
        number = []
        count = 0

        #無視プレイヤーの反映
        for i in range(len(loot_list)):
            for j in range(len(ignore_list)):
                if loot_list[i][0] ==  ignore_list[j][0]:
                    if len(ignore_list[j]) == 1:
                        number.append(i)
                    elif loot_list[i][1] == ignore_list[j][1]:
                        number.append(i)
                    else:
                        pass
                else:
                    pass
        for i in number:
            del loot_list[i-count]
            count += 1

        #鉱石及びプレイヤー名の結合
        for i in range(len(loot_list)):
            loot_list[i][-1] = loot_list[i][-1].replace("*","")

            if type(loot_list[i][1]) is int:
                if len(loot_list[i]) == 3:
                    pass
                else:
                    loot_list[i][2] = loot_list[i][2] + ' ' + loot_list[i][3]
                    del loot_list[i][3]
            elif len(loot_list[i]) == 4:
                loot_list[i][0] = loot_list[i][0] + ' ' + loot_list[i][1]
                del loot_list[i][1]
            else:
                loot_list[i][0] = loot_list[i][0] + ' ' + loot_list[i][1]
                del loot_list[i][1]
                loot_list[i][2] = loot_list[i][2] + ' ' + loot_list[i][3]
                del loot_list[i][3]

        #鉱石以外のアイテムを無視
        ore_prices = setting.InitOrePrice()
        count = 0
        for i in range(len(loot_list)):
            if not loot_list[i-count][-1] in ore_prices.all_ore_price:
                del loot_list[i-count]
                count += 1

        return loot_list
