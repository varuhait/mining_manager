#各種手動入力データ

#jita_buy 鉱石価格
class InitOrePrice:
    #jitabuy係数
    buy_coefficient = 0.9
    #燃料代
    fuel_tax = 0.05
    #ミネラル,月資源価格の初期設定
    materials = {
    #月じゃない
    'Tritanium' : 4.60,
    'Pyerite' : 3.92,
    'Mexallon' : 57.06,
    'Isogen' : 15.89,
    'Nocxium' : 299.68,
    'Zydrine' : 501.61,
    'Megacyte' : 437.70,
    'Morhphite' : 8038.95,

    #月
    'Atmostpheric Gases' : 137.93,
    'Evaporite Deposits' : 2198.95,
    'Hydrocarbons' : 190.97,
    'Silicates' : 2184.92,
    'Cobalt' : 2068.95,
    'Scandium' : 3196.95,
    'Titanium' : 4397.97,
    'Tungsten' : 8898.85,
    'Cadmium' : 12500.01,
    'Vanadium' : 8746.96,
    'Chromium' : 14769.97,
    'Platinum' : 14999.97,
    'Caesium' : 12999.97,
    'Technetium' : 18477.93,
    'Hafnium' : 17844.93,
    'Mercury' : 9908.06,
    'Promethium' : 95634.00,
    'Dysprosium' : 91799.00,
    'Neodymium' : 90798.68,
    'Thulium' : 43997.45,
    }

    standard_ore_price = {
    #月じゃない
    'Arkonor': (materials['Tritanium']*22000 + materials['Mexallon']*2500 + materials['Megacyte']*320) /100,

    'Bistot': (materials['Pyerite']*12000 + materials['Zydrine']*450 + materials['Megacyte']*100) /100,

    'Crokite': (materials['Tritanium']*21000 + materials['Nocxium']*760 + materials['Zydrine']*135) /100,

    'Dark Ochre': (materials['Tritanium']*10000 + materials['Isogen']*1600 + materials['Nocxium']*120) /100,

    'Gneiss' : (materials['Pyerite']*2200 + materials['Mexallon']*2400 + materials['Isogen']*300) /100,

    'Hedbergite' : (materials['Pyerite']*1000 + materials['Isogen']*200 + materials['Nocxium']*100 + materials['Zydrine']*19) /100,

    'Hemorphite' : (materials['Tritanium']*2200 + materials['Isogen']*100 + materials['Nocxium']*120 + materials['Zydrine']*15) /100,

    'Jaspet' : (materials['Mexallon']*350 + materials['Nocxium']*75 + materials['Zydrine']*8) /100,

    'Kernite' : (materials['Tritanium']*134 + materials['Mexallon']*267 + materials['Isogen']*134) *1.2,

    'Mercoxit' : materials['Morhphite']*300 /100,

    'Omber' : (materials['Tritanium']*800 + materials['Pyerite']*100 + materials['Isogen']*85) /100,

    'Plagioclase' : (materials['Tritanium']*107 + materials['Pyerite']*213 + materials['Mexallon']*107) /100,

    'Pyroxeres' : (materials['Tritanium']*351 + materials['Pyerite']*25 + materials['Mexallon']*50 + materials['Nocxium']*5) /100,

    'Scordite' : (materials['Tritanium']*346 + materials['Pyerite']*173) /100,

    'Spodumain' : (materials['Tritanium']*56000 + materials['Pyerite']*12050 + materials['Mexallon']*2100 + materials['Isogen']*450) /100,

    'Veldspar' : materials['Tritanium']*415 /100,
    #月
    'Bitumens' : (materials['Tritanium']*6000 + materials['Pyerite']*6000 + materials['Mexallon']*400 + materials['Hydrocarbons']*65) /100,

    'Carnotite' : (materials['Mexallon']*1000 + materials['Isogen']*1250 + materials['Zydrine']*50 + materials['Atmostpheric Gases']*15 + materials['Cobalt']*10 + materials['Technetium']*50) /100,

    'Chromite' : (materials['Pyerite']*5000 + materials['Mexallon']*1250 + materials['Isogen']*750 + materials['Nocxium']*50 + materials['Hydrocarbons']*10 + materials['Chromium']*40) /100,

    'Cinnabar' : (materials['Mexallon']*1500 + materials['Isogen']*750 + materials['Megacyte']*50 + materials['Mercury']*50 + materials['Tungsten']*10 + materials['Evaporite Deposits']*15) /100,

    'Cobaltite' : (materials['Tritanium']*7500 + materials['Pyerite']*10000 + materials['Mexallon']*500 + materials['Cobalt']*40) /100,

    'Coesite' : (materials['Tritanium']*10000 + materials['Pyerite']*2000 + materials['Mexallon']*400 + materials['Silicates']*65) /100,

    'Euxenite' : (materials['Tritanium']*10000 + materials['Pyerite']*7500 + materials['Mexallon']*500 + materials['Scandium']*40) /100,

    'Loparite' : (materials['Nocxium']*100 + materials['Zydrine']*200 + materials['Megacyte']*50 + materials['Promethium']*22 +materials['Platinum']*10 + materials['Scandium']*20 + materials['Hydrocarbons']*20) /100,

    'Monazite' : (materials['Nocxium']*50 + materials['Zydrine']*150 + materials['Megacyte']*150 + materials['Neodymium']*22 + materials['Chromium']*10 + materials['Tungsten']*20 + materials['Evaporite Deposits']*20) /100,

    'Otavite' : (materials['Tritanium']*5000 + materials['Mexallon']*1500 + materials['Isogen']*500 + materials['Nocxium']*50) /100,

    'Pollucite' : (materials['Mexallon']*1250 + materials['Isogen']*1000 + materials['Zydrine']*50 + materials['Caesium']*50 + materials['Scandium']*10 + materials['Hydrocarbons']*15) /100,

    'Scheelite' : (materials['Tritanium']*12500 + materials['Pyerite']*5000 + materials['Mexallon']*500 + materials['Tungsten']*40) /100,

    'Sperrylite' : (materials['Tritanium']*5000 + materials['Mexallon']*1000 + materials['Isogen']*1000 + materials['Zydrine']*50 + materials['Platinum']*40 + materials['Evaporite Deposits']*10) /100,

    'Sylvite' : (materials['Tritanium']*8000 + materials['Pyerite']*4000 + materials['Mexallon']*400 + materials['Evaporite Deposits']*65) /100,

    'Titanite' : (materials['Tritanium']*15000 + materials['Pyerite']*2500 + materials['Mexallon']*500 + materials['Titanium']*40) /100,

    'Vanadinite' : (materials['Pyerite']*5000 + materials['Mexallon']*750 + materials['Isogen']*1250 + materials['Zydrine']*50 + materials['Vanadium']*40 + materials['Silicates']*10) /100,

    'Xenotime' : (materials['Nocxium']*50 + materials['Zydrine']*100 + materials['Megacyte']*200 + materials['Dysprosium']*22 + materials['Vanadium']*10 + materials['Cobalt']*20 + materials['Atmostpheric Gases']*20) /100,

    'Ytterbite' : (materials['Nocxium']*200 + materials['Zydrine']*100 + materials['Megacyte']*50 + materials['Thulium']*22 + materials['Cadmium']*10 + materials['Titanium']*20 + materials['Silicates']*20) /100,

    'Zeolites' : (materials['Tritanium']*4000 + materials['Pyerite']*8000 + materials['Mexallon']*400 + materials['Atmostpheric Gases']*65) /100,

    'Zircon' : (materials['Mexallon']*1750 + materials['Isogen']*500 + materials['Megacyte']*50 + materials['Hafnium']*50 + materials['Titanium']*10 + materials['Silicates']*15) /100,
    }

    all_ore_price = {
    #月じゃない
    'Arkonor' : standard_ore_price['Arkonor'],
    'Crimson Arkonor' : standard_ore_price['Arkonor']*1.05,
    'Prime Arkonor' : standard_ore_price['Arkonor']*1.10,
    'Flawless Arkonor' : standard_ore_price['Arkonor']*1.15,

    'Bistot' : standard_ore_price['Bistot'],
    'Triclinic Bistot' : standard_ore_price['Bistot']*1.05,
    'Monoclinic Bistot' : standard_ore_price['Bistot']*1.10,
    'Cubic Bistot' : standard_ore_price['Bistot']*1.15,

    'Crokite' : standard_ore_price['Crokite'],
    'Sharp Crokite' : standard_ore_price['Crokite']*1.05,
    'Crystaline Crokite' : standard_ore_price['Crokite']*1.10,
    'Pellucid Crokite' : standard_ore_price['Crokite']*1.15,

    'Dark Ochre' : standard_ore_price['Dark Ochre'],
    'Onyx Ochre' : standard_ore_price['Dark Ochre']*1.05,
    'Obsidian Ochre' : standard_ore_price['Dark Ochre']*1.10,
    'Jet Ochre' : standard_ore_price['Dark Ochre']*1.15,

    'Gneiss' : standard_ore_price['Gneiss'],
    'Iridescent Gneiss' : standard_ore_price['Gneiss']*1.05,
    'Prismatic Gneiss' : standard_ore_price['Gneiss']*1.10,
    'Brilliant Gneiss' : standard_ore_price['Gneiss']*1.15,

    'Hedbergite' : standard_ore_price['Hedbergite'],
    'Virtric Hedbergite' : standard_ore_price['Hedbergite']*1.05,
    'Glazed Hedbergite' : standard_ore_price['Hedbergite']*1.10,
    'Lustrous Hedbergite' : standard_ore_price['Hedbergite']*1.15,

    'Hemorphite' : standard_ore_price['Hemorphite'],
    'Vivid Hemorphite' : standard_ore_price['Hemorphite']*1.05,
    'Radiant Hemorphite' : standard_ore_price['Hemorphite']*1.10,
    'Scintillating Hemorphite' : standard_ore_price['Hemorphite']*1.15,

    'Jaspet' : standard_ore_price['Jaspet'],
    'Pure Jaspet' : standard_ore_price['Jaspet']*1.05,
    'Pristine Jaspet' : standard_ore_price['Jaspet']*1.10,
    'Immaculate Jaspet' : standard_ore_price['Jaspet']*1.15,

    'Kernite' : standard_ore_price['Kernite'],
    'Luminous Kernite' : standard_ore_price['Kernite']*1.05,
    'Fiery Kernite' : standard_ore_price['Kernite']*1.10,
    'Resplendant Kernite' : standard_ore_price['Kernite']*1.15,

    'Mercoxit' : standard_ore_price['Mercoxit'],
    'Magma Mercoxit' : standard_ore_price['Mercoxit']*1.05,
    'Vitreous Mercoxit' : standard_ore_price['Mercoxit']*1.10,

    'Omber' : standard_ore_price['Omber'],
    'Silvery Omber' : standard_ore_price['Omber']*1.05,
    'Golden Omber' : standard_ore_price['Omber']*1.10,
    'Platinoid Omber' : standard_ore_price['Omber']*1.15,

    'Plagioclase' : standard_ore_price['Plagioclase'],
    'Azure Plagioclase' : standard_ore_price['Plagioclase']*1.05,
    'Rich Plagioclase' : standard_ore_price['Plagioclase']*1.10,
    'Sparkling Plagioclase' : standard_ore_price['Plagioclase']*1.15,

    'Pyroxeres' : standard_ore_price['Pyroxeres'],
    'Solid Pyroxeres' : standard_ore_price['Pyroxeres']*1.05,
    'Viscous Pyroxeres' : standard_ore_price['Pyroxeres']*1.10,
    'Opulent Pyroxeres' : standard_ore_price['Pyroxeres']*1.15,

    'Scordite' : standard_ore_price['Scordite'],
    'Condensed Scordite' : standard_ore_price['Scordite']*1.05,
    'Massive Scordite' : standard_ore_price['Scordite']*1.10,
    'Glossy Scordite' : standard_ore_price['Scordite']*1.15,

    'Spodumain' : standard_ore_price['Spodumain'],
    'Bright Spodumain' : standard_ore_price['Spodumain']*1.05,
    'Gleaming Spodumain' : standard_ore_price['Spodumain']*1.10,
    'Dazzling Spodumain' : standard_ore_price['Spodumain']*1.15,

    'Veldspar' : standard_ore_price['Veldspar'],
    'Concentrated Veldspar' : standard_ore_price['Veldspar']*1.05,
    'Dense Veldspar' : standard_ore_price['Veldspar']*1.10,
    'Stable Veldspar' : standard_ore_price['Veldspar']*1.15,

    #月
    'Bitumens' : standard_ore_price['Bitumens'],
    'Brimful Bitumens' : standard_ore_price['Bitumens']*1.15,
    'Glistening Bitumens' : standard_ore_price['Bitumens']*2.00,

    'Carnotite' : standard_ore_price['Carnotite'],
    'Replete Carnotite' : standard_ore_price['Carnotite']*1.15,
    'Glowing Carnotite' : standard_ore_price['Carnotite']*2.00,

    'Chromite' : standard_ore_price['Chromite'],
    'Lavish Chromite' : standard_ore_price['Chromite']*1.15,
    'Shirmmering Chromite' : standard_ore_price['Chromite']*2.00,

    'Cinnabar' : standard_ore_price['Cinnabar'],
    'Replate Cinnabar' : standard_ore_price['Cinnabar']*1.15,
    'Glistening Cinnabar' : standard_ore_price['Cinnabar']*2.00,

    'Cobaltite' : standard_ore_price['Cobaltite'],
    'Copious Cobaltite' : standard_ore_price['Cobaltite']*1.15,
    'Twinkling Cobaltite' : standard_ore_price['Cobaltite']*2.00,

    'Coesite' : standard_ore_price['Coesite'],
    'Brimful Coesite' : standard_ore_price['Coesite']*1.15,
    'Glistening Coesite' : standard_ore_price['Coesite']*2.00,

    'Euxenite' : standard_ore_price['Euxenite'],
    'Copious Euxenite' : standard_ore_price['Euxenite']*1.15,
    'Twinkling Euxenite' : standard_ore_price['Euxenite']*2.00,

    'Loparite' : standard_ore_price['Loparite'],
    'Bountiful Loparite' : standard_ore_price['Loparite']*1.15,
    'Shining Loparite' : standard_ore_price['Loparite']*2.00,

    'Monazite' : standard_ore_price['Monazite'],
    'Bountiful Monazite' : standard_ore_price['Monazite']*1.15,
    'Shining Monazite' : standard_ore_price['Monazite']*2.00,

    'Otavite' : standard_ore_price['Otavite'],
    'Lavish Otavite' : standard_ore_price['Otavite']*1.15,
    'Shimmering Otavite' : standard_ore_price['Otavite']*2.00,

    'Pollucite' : standard_ore_price['Pollucite'],
    'Replate Pollucite' : standard_ore_price['Pollucite']*1.15,
    'Glowing Pollucite' : standard_ore_price['Pollucite']*2.00,

    'Scheelite' : standard_ore_price['Scheelite'],
    'Copious Scheelite' : standard_ore_price['Scheelite']*1.15,
    'Twinkling Scheelite' : standard_ore_price['Scheelite']*2.00,

    'Sperrylite' : standard_ore_price['Sperrylite'],
    'Lavish Sperrylite' : standard_ore_price['Sperrylite']*1.15,
    'Shimmering Sperrylite' : standard_ore_price['Sperrylite']*2.00,

    'Sylvite' : standard_ore_price['Sylvite'],
    'Brimful Sylvite' : standard_ore_price['Sylvite']*1.15,
    'Glistening Sylvite' : standard_ore_price['Sylvite']*2.00,

    'Titanite' : standard_ore_price['Titanite'],
    'Copious Titanite' : standard_ore_price['Titanite']*1.15,
    'Twinkling Titanite' : standard_ore_price['Titanite']*2.00,

    'Vanadinite' : standard_ore_price['Vanadinite'],
    'Lavish Vanadinite' : standard_ore_price['Vanadinite']*1.15,
    'Shimmering Vanadinite' : standard_ore_price['Vanadinite']*2.00,

    'Xenotime' : standard_ore_price['Xenotime'],
    'Bountiful Xenotime' : standard_ore_price['Xenotime']*1.15,
    'Shining Xenotime' : standard_ore_price['Xenotime']*2.00,

    'Ytterbite' : standard_ore_price['Ytterbite'],
    'Bountiful Ytterbite' : standard_ore_price['Ytterbite']*1.15,
    'Shining Ytterbite' : standard_ore_price['Ytterbite']*2.00,

    'Zeolites' : standard_ore_price['Zeolites'],
    'Brimful Zeolites' : standard_ore_price['Zeolites']*1.15,
    'Glistening Zeolites' : standard_ore_price['Zeolites']*2.00,

    'Zircon' : standard_ore_price['Zircon'],
    'Replate Zircon' : standard_ore_price['Zircon']*1.15,
    'Glowing Zircon' : standard_ore_price['Zircon']*2.00,

    }
