# Multimedia_Project
# 🎮 接球大作戰 Pro (Catch Ball Pro)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/library-Pygame-green)](https://www.pygame.org/)

這是一款基於 **Python** 與 **Pygame** 開發的街機風格接球遊戲。本專案的核心特色在於使用「插件式架構」實現高度解耦的邏輯設計，並整合了 RPG 式的永續養成系統與直覺的交互體驗。

---

## 🌟 核心特色

### 1. 插件化系統架構 (Plugin-Based Architecture)
* **邏輯解耦**：將玩家控制、敵人生成與分數邏輯完全拆分為獨立插件（`player.py`, `enemy.py`, `score.py`）。
* **動態擴充**：主引擎 `main.py` 透過統一介面調度插件，無需修改核心代碼即可新增球種或功能。

### 2. 永續養成與經濟系統
* **倍增式升級成本**：商店升級門檻隨等級指數成長 ($Cost = Base \times 2^{Level}$)，有效平衡遊戲中後期的難度曲線。
* **多維度強化**：玩家可針對「移動速度」、「生命上限」與「磁鐵引力範圍」進行永久性強化。

### 3. 直覺的交互設計
* **創新拖曳換裝**：支援 Windows `DROPFILE` 事件，玩家可直接將圖片檔案拖入遊戲視窗，即時更換角色造型。
* **進階技能機制**：實作具備冷卻時間 (CD) 的「衝刺 (Dash)」系統，增加高難度關卡下的操作深度。

### 4. 遊戲性與反饋
* **動態難度決策**：設計多種球種，包含「加分金球」、「補血藍球」與「高傷害炸彈」，考驗玩家的反應與決策。
* **震撼視覺反饋**：整合「螢幕震動 (Screen Shake)」特效，強化接到炸彈或漏接時的打擊感。

---

## 🛠️ 技術實作細節
* **單一 EXE 封裝技術**：透過 `sys._MEIPASS` 動態路徑轉換，實現單一執行檔包含所有音效、圖片與插件資源。
* **介面漢化與美化**：使用微軟正黑體確保中文顯示，並採用 Flat UI 風格設計圓角按鈕與漸層背景。

---

## 🚀 快速開始

### 環境需求
* Python 3.8+
* Pygame 2.0+

### 安裝與執行
1. **複製專案**：`git clone https://github.com/您的帳號/catch-ball-pro.git`
2. **安裝依賴**：`pip install pygame`
3. **啟動遊戲**：`python main.py`

### 打包單一 EXE 指令
```bash
python -m PyInstaller --noconsole --onefile --name "接球大作戰Pro" --icon=app.ico --add-data "player.py;." --add-data "enemy.py;." --add-data "score.py;." --add-data "bgm.mp3;." --add-data "catch.wav;." --add-data "gameover.wav;." main.py
