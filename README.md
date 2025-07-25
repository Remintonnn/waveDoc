# 簡介
(這玩意主要是自用的 soooooo)  
Anyway, 他可以自動提取訂單訊息的裡的資訊, 和生成處裡訂單需要的相關文本, UI長這樣:  

<img width="360" alt="image" src="https://github.com/user-attachments/assets/7b378656-86eb-41d2-b58e-4d3126c5c5a6" /><br>
(特別感謝[PAGE](https://page.sourceforge.net/)提供簡易快速的GUI製作)

# 如何下載和打開
方案A: 直接下載原代碼
  - clone這個專案
  - 安裝python(此專案寫於Python 3.12.4)
  - pip install 這個專案有用到的套件
  - 用python打開waveTicket.pyw
  - 📈
方案B: 下載exe
  - 去[這邊](google.com)把exe檔案抓下來(只有windows的)
  - 點下載下來的檔案兩下
  - 📈
注意: 在開關程式後他會生成一個config.json在旁邊, 可以手動編輯, 但亂改程式會💥,
      若把它部分條目刪掉那些條目會回復預設, 全刪會全部回復

# Work flow
1. 連使用者名稱一起複製訂單訊息, 把它貼到"浪單訊息"標籤下面的文字框裡, 讓程式開始解析訂單資訊
2. 用"複製/mail new ID"等按鈕生成處裡訂單所需相關文本
3. 處裡訂單
4. 使用右下角的按鈕紀錄訂單結果, 並複製訊息
5. 📈

# 其他操作細項
- 把鼠標停在訊息生成格式那邊會有提示框說明訊息格式的寫法
- 再結單訊息上點擊可以直接切換進行中場次
