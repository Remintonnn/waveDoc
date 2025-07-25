import json
# -*- coding: utf-8 -*-
class _Configs:
    def __init__(self):
        self.debug = _Config(False)
        self.WaveStartFormat = _Config(r"%Mon%D %H:%Min %Dif浪潮%Mode第%C波開打")
        self.WaveEndFormat = _Config(r"浪潮%Mode第%C波結束")
        self.WaveVideoTitleFormat = _Config(r"%B %Mon%D %H-%Min-%C %Dif%Mode")
        self.AutoRefreshWaveInfo = _Config(True)
        self.AutoResetWaveRequestFinishMsg = _Config(True)
        self.RequestFinishHeader = _Config("[訂單已完成]")
        self.TestWaveRawMsg = _Config([m.strip() for m in getTestMsgs()])
        self.AMtext = _Config(["早上","上午","凌晨","中午","am"])
        self.PMtext = _Config(["下午","晚上","pm"])
        self.yesterdayText = _Config(["yesterday","昨天"])
        # print("\n-----------\n".join(self.TestWaveRawMsg.get()))
        # print(len(self.TestWaveRawMsg.get()))
        self.load()
    def save(self):
        data = { k:v.get() for k, v in self.__dict__.items() if isinstance(v, _Config) and not k.startswith('_')}
        configStr = json.dumps(data, indent=4, ensure_ascii=False)
        with open('config.json', 'w', encoding='utf-8') as f:
            f.write(configStr)
    def load(self):
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for k, v in data.items():
                    if hasattr(self, k) and isinstance(getattr(self, k), _Config):
                        getattr(self, k).set(v)
        except FileNotFoundError:
            print("Configuration file not found. Using default settings.")
        except json.JSONDecodeError:
            print("Error decoding configuration file. Using default settings.")

class _Config:
    def __init__(self,defaultValue):
        self.defaultValue = defaultValue
        self.value = defaultValue
    def reset(self):
        self.value = self.defaultValue
    def set(self, value):
        self.value = value
    def get(self):
        return self.value
    def isDefault(self):
        return self.value == self.defaultValue

def getTestMsgs():
    return [
"""
森息機長 咖啡
[FOOB]
 — Yesterday at 22:56
遊戲ID：_Coffee_Fubuki
浪潮難度：超困難
訂單模式(代/陪打)：代打
次數：3次
""","""
Mantou_god — Yesterday at 16:30
遊戲ID：Mantou_god
浪潮難度：超困難
訂單模式(代/陪打)：代打
次數：3次
補貨的
""","""
紙鳶 — Yesterday at 15:21
遊戲ID：YUQUANG1
浪潮難度：超困難
訂單模式(代/陪打)：代打
次數：3次
""","""
TNT — 7/23/2025 15:58
遊戲ID：Wewe0705
浪潮難度：超困難
訂單模式(代/陪打)：代打
次數：3
""","""
波
[BRUH]
 — 2025/7/17 晚上10:42
spike好嚴重:noo~1:
""","""
波
[BRUH]
 — 2025/7/21 晚上11:23
84
""","""
波
[BRUH]
 — 昨天 晚上10:53
oh
""","""
波
[BRUH]
 — 下午4:54
:_pepe_magnifyingglass: 
"""
]


confingInstance = _Configs()


# Tooltip storage

# %C = 當前波數, %Dif = 浪潮難度, %Mode = 訂單模式, %B = 買家ID
# %Mon = 月份, %D = 日期, %H = 小時, %Min = 分鐘
# 文字太長可以使用滾輪查看其他行
# 換行符號會被當空格, 把欄位清空來回復預設值
# (欄位只有在你取消聚焦時會被儲存到設定/回復預設)

# WHY YOU WANT MODDED MENDING ON YOUR SWORD?
# IS NOT GOOD ENOUGH AS PROCURED FROM MOJANG STUDIO GAMES?
# YOU THINK NEEDS IMPROVEMENT?
# THEN MAYBE YOU FIND JOB WITH COMPANY OF SWEDEN! YOU HAVE DRINKS WITH MARKUS ALEXEJ PERSSON,
# TRADE STORY OF MANY GAMES DESIGNED AND DETAILS OF SCHOOL FOR WEAPONMAKING!

# OR MAYBE YOU NOT DO THIS. PROBABLY IS BECAUSE YOU NEVER MAKE GAME IN WHOLE LIFE.
# YOU LOOK AT FINE MINECRAFT ITEMS, THINK IT NEED CRAZY SHIT STICK ON ALL SIDES OF WEAPON.
# YOU HAVE DISEASE OF AMERICAN CAPITALIST,
# CHANGE THING THAT IS FINE FOR NO REASON EXCEPT TO LOOK DIFFERENT FROM COMRADE.
# YOU PUT CHEAP BOOK OF VAMPIRE SLAVE FACTORY ON ONE SIDE, YOU PUT BAD VERSION OF FIRE OF ASPECT ON OTHER SIDE,
# YOU PUT THE BRAIN POWER ON BOTTOM SO YOU ARE LIKE AMERICAN SCIENCE GUY NEIL TYSON.
# MAYBE YOU PUT SEX DILDO ON TOP TO FUCK YOURSELF IN ASSHOLE FOR MAKING SHAMEFUL TRAVESTY OF WEAPON OF MARKUS ALEXEJ PERSSON, NO?

# VANILLA IS FINE.
# YOU FUCK IT,
# IT ONLY GET EXPENSIVE AND YOU STILL DIE WHEN PING HIGH.
# GO TO HYPIXEL SKYWAR, PRACTICE WITH MANY MONTH OF YOUR LIFE.
# THEN YOU NOT NEED DUMB SHIT PUT ON SIDE OF WEAPON.
