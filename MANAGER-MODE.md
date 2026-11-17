# Manager Mode 使用與維護

Manager Mode 是 ai-agent-hq 的管理閱讀層。管理者先看[首頁](README.md)的專案、健康、風險、最近成果、建議與待決策事項，再按需要進入專案摘要及原始報告。

本版使用 GitHub Repository 原生 Markdown，沒有新增網站、登入服務、資料庫、常駐排程或自動部署。儲存庫目前為 **public**；所有新增內容必須適合公開分享。

## 管理者先看什麼

| 管理問題 | 閱讀入口 | 需要注意 |
| --- | --- | --- |
| 現在有哪些專案？ | [首頁專案總覽](README.md)、[專案登錄](projects/registry.yml) | 專案流程狀態與健康判斷不同 |
| 哪些專案有問題？ | 首頁健康與高優先風險、各專案摘要 | 看理由、適用範圍與證據日期，不能只看測試通過率 |
| Agent 最近完成什麼？ | 首頁最近成果、已驗收任務與報告 | 任務完成只代表該交付範圍，不代表產品全部完成 |
| 下一步應該做什麼？ | Main Agent 建議 | 建議仍是候選，未自行取得執行授權 |
| 哪些事情需要批准？ | 管理者待決策事項 | 看具體操作、影響、選項與目前授權狀態 |
| 想核對原始內容？ | [第一個專案摘要](projects/codex-xk-apparel-store/executive-summary.md) | 從摘要進入原始報告與命令證據，首頁不展開完整技術日誌 |

首頁的「10 秒回答六個問題」是人類閱讀驗收目標，須實際計時並記錄結果。文件檢查或 Agent 自評不能代替管理者的這項驗收。

## 四個獨立維度

| 維度 | 意義與規則 |
| --- | --- |
| 任務／流程狀態 | 沿用既有 `pending`、`in_progress`、`blocked`、`awaiting_review`、`completed` 流程；專案 `scan_completed` 只表示掃描已完成 |
| 專案健康 | 使用 `Healthy`、`Needs Attention`、`At Risk`、`Blocked`、`Unknown`，依風險、證據、阻塞及目標判斷；必須附理由 |
| 商業就緒度 | 明示目前適用範圍、尚缺能力及未驗證條件；原型測試成功不能取代正式交易或個資治理驗收 |
| 授權／決策狀態 | 將 Main 建議、待管理者批准、已批准範圍與未獲授權操作分開；批准有具體範圍，不自動延伸至部署或新功能 |

健康與風險分類定義見[專案健康及風險規格](docs/PROJECT_HEALTH_AND_RISK.md)。它們是 HQ 自訂管理資料，並非 Codex 設定，也不會變更 Agent 的 sandbox、工具權限或派工角色。

每項管理結論另外標示證據狀態：**已驗證、推論、未執行、未知**。例如，25／25 測試是固定版本的已驗證結果；健康等級是附理由的管理判斷；真實瀏覽器未測須標未執行；缺少足夠資料則標未知。

行動批准狀態獨立使用：**不需批准、待批准、已批准、拒絕**。依賴修補等候選建議目前保持待批准；待批准不代表已執行，已批准也只允許具體範圍，仍須另有執行證據。

## 摘要與證據如何更新

1. 專業 Agent 依原本任務與 [Agent 回報模板](templates/AGENT_REPORT.md) 交付，保留來源 revision、實際結果與限制。
2. Main Agent 核對原始來源、命令證據及矛盾，接受交付後才更新有效任務狀態與專案工作紀錄。
3. 依[統一摘要模板](templates/EXECUTIVE_SUMMARY.md)維護各專案 `executive-summary.md`，為重要數字、風險與結論附原始報告或證據連結。
4. 摘要分別保留更新日期及證據日期／來源 revision。摘要今日更新，不表示測試今日重跑；歷史部署成功，不表示網站即時健康。
5. Main Agent 將摘要的專案名稱、健康、主要風險、成果、建議與決策事項同步至首頁。兩處內容不一致、缺少證據或資料過期時，明示差異，不能維持沒有依據的綠燈。
6. QA 檢查數值、狀態、相對連結、來源範圍及未執行項目；Security 檢查公開內容、存取界線與外部資源；Main 整合後交付審查。

來源優先序是「可重現的命令／原始證據 → Main 已驗收執行紀錄 → 管理摘要 → 首頁索引」。舊登錄與已驗收紀錄衝突時，先揭露差異並查證，再以有來源的工作紀錄對齊；不改寫歷史報告以掩蓋當時限制。

第一份摘要沿用 HQ-001 的 2026-11-16 掃描，目標原始碼為 `codex-xk-apparel-store@1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422`。本輪管理介面工作沒有重新執行該專案測試、修補其依賴或部署產品。詳見 [HQ-001 掃描](projects/codex-xk-apparel-store/reports/HQ-001/scan-report.md)及[執行紀錄](projects/codex-xk-apparel-store/reports/HQ-001/execution-record.json)。

## 公開內容與存取界線

- public Repository 的首頁、摘要、所有檔案及 Git 歷史均可公開讀取。折疊區塊、較深目錄、未在首頁列出的檔案或不容易猜的連結，都不是存取控制。
- 只新增可公開的專案識別、管理結論、必要證據及已去敏報告。不新增私人公司資料、客戶原始資料、秘密、正式憑證、內部環境路徑或原始對話。
- 發布前檢視完整差異及原有歷史的公開風險；敏感資訊若已進入歷史，單純刪除目前檔案不代表外洩已解除。先停止相關發布並交由管理者處理。
- 不以外部 badge、追蹤碼、分析服務或遠端腳本呈現私人管理資料。現版僅使用 Repository 內的 Markdown 與來源連結。
- 管理者選擇 public，不等於批准網站部署。GitHub Pages、其他 hosting、權限變更、正式服務與付費資源都需要各自明確授權。

## 保留的 Agent 派工與工程入口

本版沒有更動 `.codex/agents/` 的14份設定、角色名稱、Main 的派工方式、owned paths 或驗收權責。設定存在不等於角色已啟動；角色回報也不等於主任務已驗收。工作規範仍以 [AGENTS.md](AGENTS.md) 及當次使用者授權為準。

| Agent | 工程職責與設定 |
| --- | --- |
| product | [需求、使用者流程與產品優先序](.codex/agents/product.toml) |
| architect | [系統架構、模組邊界與資料流](.codex/agents/architect.toml) |
| research | [官方來源、版本行為與方案研究](.codex/agents/research.toml) |
| frontend | [前端畫面、互動、狀態與可及性](.codex/agents/frontend.toml) |
| backend | [API、業務流程、驗證與錯誤處理](.codex/agents/backend.toml) |
| database | [資料模型、交易、遷移與復原](.codex/agents/database.toml) |
| integration | [跨模組與外部服務契約](.codex/agents/integration.toml) |
| qa | [測試、覆蓋缺口與驗收證據](.codex/agents/qa.toml) |
| security | [信任邊界、授權與資料風險](.codex/agents/security.toml) |
| reviewer | [交付正確性、差異與回歸風險複核](.codex/agents/reviewer.toml) |
| devops | [建置、CI 與環境設定盤點](.codex/agents/devops.toml) |
| documentation | [文件、操作說明與交接一致性](.codex/agents/documentation.toml) |
| monitoring | [可觀測性、告警與監控缺口](.codex/agents/monitoring.toml) |
| release | [發版條件、相容性與回滾準備](.codex/agents/release.toml) |

其他入口：[專案設定](projects/codex-xk-apparel-store/project.yml)、[專案工作紀錄](projects/codex-xk-apparel-store/work-log.md)、[任務模板](templates/TASK.md)、[掃描模板](templates/PROJECT_SCAN.md)、[決策目錄](decisions/)、[全域工作紀錄](logs/)。完整技術報告保留於各專案 `reports/`，不預設展開在管理首頁。

HQ-002 的[架構及實作範圍](projects/codex-xk-apparel-store/reports/HQ-002/architecture-plan.md)、[QA 驗收](projects/codex-xk-apparel-store/reports/HQ-002/qa-report.md)、[Security 審查](projects/codex-xk-apparel-store/reports/HQ-002/security-review.md)與[Main 整合報告](projects/codex-xk-apparel-store/reports/HQ-002/main-report.md)記錄本輪結果及尚待人類驗收項目。
