# ADR-0001：建立中央 AI 指揮中心

- 日期：2026-11-16
- 狀態：accepted
- 決策者：Main Agent
- 授權依據：使用者本次初始化指示，包含 HQ 文件提交與建立 PR。

## 背景與選項

HQ 原先只有 README 與根目錄的 `HQ-001` 掃描要求。可維持單一說明文件，或建立專案登錄、任務狀態與獨立工作紀錄。本次採用後者，以便調度與驗收時查核。

## 決策

1. 使用 `xk2022/ai-agent-hq` 作為中央管理儲存庫；它與現有 checkout 的 origin 一致，取代使用者指示中的帳號佔位符。
2. 專案使用 `projects/registry.yml` 與各自的 `project.yml`、`work-log.md`；這些是 HQ 管理資料，不是 Codex 權限設定。
3. 將既有根目錄 `HQ-001` 遷移到 `tasks/inbox/HQ-001.md`，保留原始掃描要求，維持 `pending`。初始化不代表掃描已啟動。
4. 建立 14 份 `.codex/agents/*.toml`，只使用官方支援的 `name`、`description`、`developer_instructions`。省略模型選擇以繼承父 Agent；不建立額外註冊表或自創設定欄位。
5. 受管理專案保持唯讀；高風險操作需使用者確認。以 HQ 分支與 PR 交付，不直接修改 `main`。

## 影響與限制

- 檔案與政策可供後續 session 讀取，不提供常駐排程、即時監控或自動部署。
- Agent 設定建立與 TOML 解析可驗證；實際載入及啟動需由支援此格式的 Codex session 執行，不能單靠文件宣稱已啟用。
- 父 session 與平台控制實際權限；Agent 指令及 YAML 不構成獨立 sandbox。
- 後續 `HQ-001` 掃描須遵守任務範圍、隔離測試及證據要求，不可預先填入尚未執行的結果。

## 官方格式來源

- [Codex Subagents](https://developers.openai.com/codex/subagents)，2026-11-16 查核，當日導向 [ChatGPT Learn Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)。
