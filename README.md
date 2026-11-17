# AI 專案決策中控台

**1 個受管理專案 · 1 個 High 依賴風險 · 2 項待決策**

| 專案 | 健康判斷〔推論〕 | 正式商用 |
| --- | --- | --- |
| [服飾商城](projects/codex-xk-apparel-store/executive-summary.md) | Needs Attention | 未就緒 |

- **Agent 最近完成**：HQ-001 掃描已驗收，四角色成果已整合；25／25 測試通過。[成果與證據](projects/codex-xk-apparel-store/reports/HQ-001/execution-record.json)
- **最重要的風險**：happy-dom 20.14.6 有 **1 個 High 依賴套件、2 項公告**，尚未修補。[安全依據](projects/codex-xk-apparel-store/reports/HQ-001/evidence/npm-audit.log)
- **Main Agent 建議〔未授權執行〕**：優先安排測試依賴安全升版與回歸。[建議與理由](projects/codex-xk-apparel-store/executive-summary.md#main-agent-下一步建議)
- **需要你決策**：[DEC-001：是否核准依賴升版工作包](projects/codex-xk-apparel-store/executive-summary.md#dec-001)；[DEC-002：維持原型或啟動正式化設計](projects/codex-xk-apparel-store/executive-summary.md#dec-002)。兩項均待批准。

資料為 **2026-11-16** 掃描、產品 revision `1d4f2ac`；摘要整理於 2026-11-17，產品目前 revision 未重新查核。這是管理快照，沒有即時監控或新的測試結果。

## 專案總覽

受管理專案 ID：`codex-xk-apparel-store`。目前目標是**假商品／模擬交易原型**；健康 Needs Attention 是依此範圍的管理推論，不是正式安全認證。

| 維度 | 已知狀態 | 查核入口 |
| --- | --- | --- |
| 掃描流程 | `scan_completed`；HQ-001 已完成並驗收 | [完成任務](tasks/completed/HQ-001.md) |
| 工程品質 | 該版本型別檢查、建置及25／25測試通過 | [實測日誌](projects/codex-xk-apparel-store/reports/HQ-001/evidence/npm-test.log) |
| 安全 | High 測試依賴風險未修補；不宣稱已證實商城執行時漏洞 | [Security 報告](projects/codex-xk-apparel-store/reports/HQ-001/security-report.md) |
| 商業就緒度 | 僅原型；後端授權、權威DB／庫存交易、真實金流及個資治理尚缺 | [正式化門檻](projects/codex-xk-apparel-store/reports/HQ-001/roadmap.md) |
| 尚未驗證 | 真實瀏覽器／手機／讀屏、即時Pages健康、正式服務與多人併發 | [未驗證清單](projects/codex-xk-apparel-store/reports/HQ-001/execution-record.json) |
| Coverage | 96.32%僅catalog/model產物行覆蓋率；app與完整TS專案未量測 | [量測範圍](projects/codex-xk-apparel-store/reports/HQ-001/evidence/npm-coverage.log) |

## 最近成果與下一步

- **HQ-001 已完成**：Architect、Research、QA、Security 已交付，由Main整合。[專案管理摘要](projects/codex-xk-apparel-store/executive-summary.md)
- **HQ-002 Manager Mode**：管理首頁與規格已實作，QA／Security結果見下方；管理者六問10秒人類驗收待確認。[任務](tasks/in-progress/HQ-002.md)
- **候選工作未開工**：依賴修補與正式化設計仍待DEC-001／DEC-002批准。批准本次HQ介面工作不會授權修改商城或部署。

## 從管理結論查到證據

[專案摘要](projects/codex-xk-apparel-store/executive-summary.md) → [完整掃描](projects/codex-xk-apparel-store/reports/HQ-001/scan-report.md) → [原始證據目錄](projects/codex-xk-apparel-store/reports/HQ-001/evidence/)。

- [架構報告](projects/codex-xk-apparel-store/reports/HQ-001/architecture.md)／[候選路線](projects/codex-xk-apparel-store/reports/HQ-001/roadmap.md)
- [HQ-002 QA驗收](projects/codex-xk-apparel-store/reports/HQ-002/qa-report.md)／[Security審查](projects/codex-xk-apparel-store/reports/HQ-002/security-review.md)／[Main整合](projects/codex-xk-apparel-store/reports/HQ-002/main-report.md)
- [Manager Mode使用與技術導航](MANAGER-MODE.md)／[健康與風險規格](docs/PROJECT_HEALTH_AND_RISK.md)／[摘要模板](templates/EXECUTIVE_SUMMARY.md)
- [專案索引](projects/registry.yml)／[專案設定](projects/codex-xk-apparel-store/project.yml)／[獨立工作紀錄](projects/codex-xk-apparel-store/work-log.md)／[Main與派工規範](AGENTS.md)

本HQ依管理者目前選擇維持**公開儲存庫**；所有檔案與Git歷史皆可公開讀取，折疊或連結不提供存取隔離。新內容只使用經審查可公開的管理資訊；不得加入憑證、私人資料或私密Agent紀錄。本次沒有網站部署。
