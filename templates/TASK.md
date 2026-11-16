---
id: "<task_id>"
title: "<task_title>"
project_id: "<project_id>"
status: pending
scan_permission: read_only
assigned_agents: []
dependencies: []
created_at: "2026-11-16"
---

# 任務：`<task_id>` — `<task_title>`

> Frontmatter 為 HQ 自訂任務資料，不是 Codex Agent 設定，也不會自動強制執行權限。複製時須更新日期及佔位符。

## 目標與輸入

- 目標／背景：`<待填>`
- Repository／分支／完整 Commit SHA：`<待填>`
- 專案設定：`projects/<project_id>/project.yml`
- 專案工作紀錄：`projects/<project_id>/work-log.md`
- 輸入文件、前置任務與相依專案：`<待填>`
- 授權來源、範圍與限制：`<使用者指示或決策紀錄；不得填入私人對話全文>`

## 工作範圍

- 納入：`<待填>`
- 排除：`<待填>`
- 本次權限為 `read_only`：不修改受管理專案、不建立其 Commit、不推送、不部署。
- 允許寫入的 HQ 文件或報告路徑：`<明列路徑>`。
- 不保存 API Token，不接觸正式憑證，不將私人資料放入公開 Repository。
- 高風險操作必須先由 Main Agent 取得使用者明確確認；未獲授權時回報阻塞。
- 依賴安裝與測試須事前審查腳本及副作用；`npm ci`、`npm test` 僅在隔離 Cloud、無正式憑證且副作用受控時執行。

## 子任務派工

| 子任務 ID | Agent | 輸入／Revision | 工作範圍 | 唯一 owned paths | 輸出及驗收條件 | 相依任務 |
|---|---|---|---|---|---|---|
| `<待填>` | `<role>` | `<待填>` | `<待填>` | `<HQ 路徑；無寫入則填無>` | `<待填>` | `<待填>` |

- Main Agent 確認各子任務的寫入路徑不重疊；跨專案任務須逐一確認該專案的權限、相依條件及工作紀錄。
- 子 Agent 使用 `templates/AGENT_REPORT.md` 回報，區分已驗證、推論及未執行項目。
- 子 Agent 只回報工作結果；Main Agent 負責整合、解決衝突與最終驗收。

## 狀態與工作紀錄

- `pending`：尚未啟動，位於 `tasks/inbox/`。
- `in_progress`：已由 Main Agent 接手並派工，位於 `tasks/in-progress/`。
- `blocked`：已啟動任務的權限、輸入或相依條件不足；保留於 `tasks/in-progress/` 並記錄阻塞。
- `awaiting_review`：結果已交付，等待 Main Agent 驗收，位於 `tasks/in-progress/`。
- `completed`：Main Agent 已驗收，移至 `tasks/completed/`。
- 任務移動後同步更新 `project.yml` 的任務檔案路徑，以及引用此任務的登錄或紀錄。

| 時間（UTC） | 狀態 | 執行者 | 動作／證據 | 阻塞／下一步 |
|---|---|---|---|---|
| `<待填>` | `pending` | Main Agent | `<建立任務與授權依據>` | `<待填>` |

## 風險與授權

| 操作／風險 | 影響 | 風險等級 | 是否需使用者確認 | 授權依據／尚缺條件 |
|---|---|---|---|---|
| `<待填>` | `<待填>` | `<待填>` | `<待填>` | `<待填>` |

## 交付與驗收條件

- [ ] 所有要求均有對應交付物，路徑為 `<待填>`。
- [ ] 結論附 revision、檔案位置或實際命令結果，未驗證項目清楚標示。
- [ ] 測試紀錄含命令、exit code、範圍與限制；未量測覆蓋率時明確說明。
- [ ] 未超出授權範圍，受管理專案已追蹤檔案無變更。
- [ ] 風險、阻塞與需確認事項已整理，機密及私人資料已排除。
- [ ] Main Agent 已複核子 Agent 結果並更新該專案工作紀錄。

- Main Agent 驗收結果／時間：`<待審核>`
- 需補件項目：`<待填>`
- 最終交付／PR：`<待填；未建立則寫未建立>`
