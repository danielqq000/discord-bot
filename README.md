# Discord RPG Bot

這是一個基於Discord的RPG養成遊戲機器人。你可以創建角色，進行冒險，並且升級你的角色。

## 安裝

1. 克隆此儲存庫
2. 安裝依賴
    ```bash
    pip install -r requirements.txt
    ```
3. 在 `config.py` 文件中添加你的Discord Bot Token。

## 運行

```bash
python bot.py

目錄：
discord_rpg_bot/
├── bot.py
├── config.py
├── cogs/
│   ├── __init__.py
│   ├── character.py
│   ├── adventure.py
├── data/
│   ├── __init__.py
│   ├── player_data.json
├── utils/
│   ├── __init__.py
│   ├── db.py
│   ├── helpers.py
├── requirements.txt
├── README.md

bot.py: 主程序文件，包含啟動和設定機器人的基本代碼。

config.py: 配置文件，用於存儲機器人的Token和其他配置變量。

cogs/: 使用Discord Bot的"Cog"來模塊化機器人的指令和事件處理。這裡包含了不同的功能模塊，例如角色管理和冒險活動。

    character.py: 管理角色創建、查看和升級的指令。
    adventure.py: 處理冒險指令和相關邏輯。

data/: 存儲遊戲數據的文件夾，例如玩家數據的JSON文件或數據庫文件。

    player_data.json: 存儲玩家的角色信息。

utils/: 實用工具文件夾，包含輔助函數和數據庫操作。

    db.py: 處理數據庫操作的函數。
    helpers.py: 通用輔助函數。

requirements.txt: 列出項目依賴的Python庫，用於設置虛擬環境。

README.md: 項目說明文件，描述項目的目的、設置和使用方法。
