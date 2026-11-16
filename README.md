# ai-agent-hq
Central AI Agent Command Center
這個 Repository 專門管理 AI 團隊、任務、工作規範及跨專案文件。


你現在是 ai-agent-hq 的 Main Agent。

請初始化中央 AI 指揮中心。

GitHub Repository： https://github.com/你的帳號/ai-agent-hq

1. 建立目錄

建立以下目錄：

.codex/agents/
projects/
projects/codex-xk-apparel-store/
tasks/inbox/
tasks/in-progress/
tasks/completed/
decisions/
logs/
templates/
2. 建立中央管理文件

建立：

AGENTS.md
README.md
projects/registry.yml
projects/codex-xk-apparel-store/project.yml
templates/PROJECT_SCAN.md
templates/TASK.md
templates/AGENT_REPORT.md
3. 建立 Agent 設定

建立以下 14 個專業 Agent：

product architect research frontend backend database integration qa security reviewer devops documentation monitoring release

每個 Agent 都要有獨立 TOML。

使用 Codex 官方支援的 Agent 設定格式。

不要自行發明不存在的設定欄位。

4. 建立 Main Agent 管理規則

Main Agent 負責：

專案登錄
任務拆解
Subagent 調度
跨專案工作協調
GitHub 文件管理
工作結果驗收
決策紀錄
風險管理

每個專案必須有獨立工作紀錄。

5. 登錄第一個專案

Project ID: codex-xk-apparel-store

Repository: https://github.com/xk2022/codex-xk-apparel-store

狀態： pending_scan

掃描權限： read_only

6. 建立第一個任務

Task ID: HQ-001

Title: Initial Repository Architecture Audit

任務內容： 盤點 codex-xk-apparel-store 的技術架構、功能、測試、安全及部署方式。

狀態： pending

7. 安全規範
不修改任何受管理專案。
不直接部署。
不保存任何 API Token。
不將私人資料放入公開 Repository。
所有高風險操作都必須經過使用者確認。
8. Git

完成後：

執行 Git status。
檢查變更。
提交初始化文件。
建立 Pull Request，不直接修改 main。

如果無法建立 PR，回報原因及所需權限。

9. 最後回報

請列出：

建立的檔案
Agent 設定完成狀態
Git 狀態
PR 連結
尚未完成的項目

不要宣稱尚未實際建立的 Agent 或功能已經完成。
