from . import setting

#合計推定金額、個人推定金額、および比の算出
class BalanceCalculate:
    def __init__(self,loot_list):
        self.settings = setting.InitOrePrice()
        self.personal_balances = {}
        self.personal_balances_ratio = {}
        self.ore_balances = {}
        self.total_balance = 0
        self.loot_list = loot_list

    def balances(self):
        #プレイヤー、鉱石の辞書作成
        for i in range(len(self.loot_list)):
            self.personal_balances[self.loot_list[i][0]] = 0
            self.ore_balances[self.loot_list[i][-1]] = 0

        #プレイヤー、鉱石毎の値段を足し合わせる
        for i in range(len(self.loot_list)):
            self.personal_balances[self.loot_list[i][0]] += round( self.settings.all_ore_price[self.loot_list[i][2]] * self.loot_list[i][1] * self.settings.buy_coefficient *(1 - self.settings.fuel_tax))

            self.ore_balances[self.loot_list[i][2]] += round( self.settings.all_ore_price[self.loot_list[i][2]] * self.loot_list[i][1] *  self.settings.buy_coefficient)

            self.total_balance += round( self.settings.all_ore_price[self.loot_list[i][2]] * self.loot_list[i][1] *  self.settings.buy_coefficient)

        for i in self.personal_balances:
            self.personal_balances_ratio[i] = self.personal_balances[i] / self.total_balance

        all_prices = [self.personal_balances,self.ore_balances,self.personal_balances_ratio,self.total_balance]
        return all_prices
