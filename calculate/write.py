#テキストファイルへの出力
from . import setting

class WriteFile:
    def __init__(self,balances,title):
        self.settings = setting.InitOrePrice()
        self.persons = balances[0]
        self.ores = balances[1]
        self.persons_ratio = balances[2]
        self.total = balances[3]
        self.title = str(title) + '.txt'

    def output(self):
        file = open(self.title, 'w')
        file.write('総計（Jitabuy' + str(self.settings.buy_coefficient*100)  + '%）' + '\n' + "{:,}".format(self.total)+ 'ISK' '\n' + '\n')
        file.close

        file = open(self.title, 'a')
        file.write('個人毎の合計金額{Jitabuy' + str(self.settings.buy_coefficient*100)  + '%(燃料代' + str(self.settings.fuel_tax*100) + '%徴収済み)}' '\n' + '\n')
        for i in self.persons:
            file.write(i + " : " + "{:,}".format(self.persons[i]) + 'ISK' + '\n')
        else:
            file.write('\n')

        file.write('鉱石毎の合計金額（推定）' + '\n' + '\n')

        for i in self.ores:
            file.write(i + " : " + "{:,}".format(self.ores[i]) + 'ISK' + '\n')
        else:
            file.write('\n')

        file.write('個人毎合計金額/全体合計金額' + '\n' + '\n')

        for i in self.persons_ratio:
            file.write(i + " : " + str(self.persons_ratio[i]) + '\n')
        else:
            file.write('\n')
