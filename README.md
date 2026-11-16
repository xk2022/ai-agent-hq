# ai-agent-hq

Central AI Agent Command Center

中央 AI 指揮中心，用來管理 AI 團隊、專案登錄、任務拆解、跨專案協調、驗收、決策與工作紀錄。

## 目前狀態

- HQ Repository：[xk2022/ai-agent-hq](https://github.com/xk2022/ai-agent-hq)。
- 已建立 14 份專業 Agent TOML 設定；設定檔完成不等於 Agent 已啟動或工作已執行。
- 第一個專案：`codex-xk-apparel-store`，狀態 `pending_scan`，掃描權限 `read_only`。
- 第一個任務：[HQ-001 — Initial Repository Architecture Audit](tasks/inbox/HQ-001.md)，狀態 `pending`，尚未執行掃描或專案測試。
- 本儲存庫提供管理文件與 Agent 指令，不含常駐調度器、自動監控或部署服務。

## 目錄

```text
.codex/agents/                         14 份專業 Agent 設定
AGENTS.md                              Main Agent 與協作規範
projects/registry.yml                   專案索引
projects/codex-xk-apparel-store/
  project.yml                          專案狀態與權限
  work-log.md                          專案獨立工作紀錄
tasks/inbox/                           待啟動任務
tasks/in-progress/                     執行中、受阻、待驗收任務
tasks/completed/                       Main Agent 已驗收任務
decisions/                             決策與授權依據
logs/                                  全域工作與協調紀錄
templates/                             掃描、任務及 Agent 回報模板
```

掃描產出在任務執行後建立於 `projects/<project-id>/reports/<task-id>/`；目前沒有預先填寫掃描結果。空任務目錄以 `.gitkeep` 納入 Git。

## Main Agent 管理方式

1. 依 [AGENTS.md](AGENTS.md) 核對專案登錄與權限。
2. 使用 [TASK 模板](templates/TASK.md) 拆解任務，定義範圍、輸入 revision、依賴、產出與驗收條件。
3. 分派專業 Agent，明列可讀與可寫路徑，避免重疊寫入。
4. 收集 [Agent 報告](templates/AGENT_REPORT.md)，核對證據、差異與驗證結果後整合。
5. 維護各專案 `work-log.md`；重大決策寫入 `decisions/`，全域協調寫入 `logs/`。
6. HQ 文件由獨立分支與 PR 交付，不直接提交或推送 `main`，不自行合併。

任務從 `pending` 開始；Main Agent 啟動後移到 `tasks/in-progress/` 並改為 `in_progress`，可標 `blocked` 或 `awaiting_review`。驗收後才移至 `tasks/completed/` 並標為 `completed`，同步專案中的任務路徑。這些 YAML 與 frontmatter 是 HQ 自訂管理資料，不是 Codex 設定或自動權限控制。

## 14 個專業 Agent

| Agent | 主要工作 |
| --- | --- |
| product | 需求、使用者流程、產品缺口與優先順序 |
| architect | 系統架構、模組邊界、資料流與依賴 |
| research | 官方文件、技術選項與來源核對 |
| frontend | 前端畫面、狀態、互動與可及性分析 |
| backend | 後端流程、API 契約與錯誤處理分析 |
| database | 資料模型、持久化、一致性與遷移風險 |
| integration | 跨模組、跨專案及外部服務契約 |
| qa | 測試、覆蓋缺口、驗收與重現步驟 |
| security | 信任邊界、授權、敏感資料與風險 |
| reviewer | 交付結果、正確性、差異及回歸風險複核 |
| devops | CI、建置、部署設定與環境風險盤點 |
| documentation | 證據化文件、操作說明與紀錄一致性 |
| monitoring | 可觀測性、告警與監控缺口分析 |
| release | 發版條件、相容性、回滾與發布建議 |

每個 Agent 位於 `.codex/agents/<name>.toml`，只使用官方必要欄位 `name`、`description`、`developer_instructions`。省略模型設定以繼承父 Agent；不需要額外 `[agents.<name>]` 註冊。

使用時在支援自訂 Agent 的 Codex 中開啟本儲存庫，要求 Main Agent 按角色派工。Agent 的實際啟動與回報仍需執行驗證；本次初始化未逐一啟動這 14 個自訂角色。

依 [Codex 官方 Subagents 文件](https://developers.openai.com/codex/subagents)（2026-11-16 查核），專案層級獨立 TOML 放在 `.codex/agents/`。Subagent 繼承父層權限；指令中的唯讀規則不會建立獨立 sandbox，Main Agent 必須落實任務與工具限制。

## 第一個專案與任務

- [專案登錄](projects/registry.yml)
- [專案設定](projects/codex-xk-apparel-store/project.yml)
- [專案工作紀錄](projects/codex-xk-apparel-store/work-log.md)
- 目標 Repository：[xk2022/codex-xk-apparel-store](https://github.com/xk2022/codex-xk-apparel-store)
- `HQ-001` 盤點技術架構、功能、測試、安全及部署方式；規劃由 architect、research、qa、security 分工，再由 Main Agent 驗收。
- 原本根目錄 `HQ-001` 已移至任務收件匣，原始掃描要求保留於任務內文。
- [PROJECT_SCAN 模板](templates/PROJECT_SCAN.md) 規範掃描範圍、證據及輸出格式。

## 安全規範

- 不修改受管理專案，不直接部署或發版。
- 不保存 API Token、密碼、私鑰或正式憑證。
- 不將私人資料放入公開 Repository；寫入 PR 或報告前先核對可見性並清理敏感資訊。
- 高風險操作必須經使用者對具體操作明確確認，並記錄範圍。
- 測試僅在隔離 Cloud 執行，先審查腳本與副作用，不改動已追蹤檔案、不使用正式憑證。
- 專案狀態、命令結果與覆蓋率以實測為準；未知或未執行必須明示。

完整規則見 [AGENTS.md](AGENTS.md)，初始化決策見 [ADR-0001](decisions/0001-central-hq-initialization.md)。
