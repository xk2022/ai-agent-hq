# ADR-0002：Manager Mode管理閱讀層

- 日期：2026-11-17
- 狀態：accepted
- 決策範圍：HQ-002實作及Git交付；不包含商城開發或網站部署。

## 採用方案

管理者審閱規劃後批准實作、push與PR merge。HQ以GitHub README作管理首頁，專案摘要連至原始報告及證據；原有派工流程與14份Agent設定不變。

原規劃採private目的地；後續管理者確認選擇維持public儲存庫。採此更新後的受眾選擇，新內容須經可公開資料審查。public代表全部檔案及Git歷史可讀；首頁簡化不構成隱私隔離。沒有因此核准網站部署或公開私人資料。

## 資料與管理規則

- 任務狀態、健康度、商業就緒度、批准狀態分開。
- 每項主張保留來源revision、日期、證據狀態與連結；只整理摘要不代表重新驗證來源。
- 健康度有明確理由及範圍；不能單依測試全過判為Healthy。
- HQ-001原始報告及證據保留；只對齊過時管理索引。
- DEC-001／DEC-002是商城後續候選決策，仍pending；不能沿用HQ-002批准而執行。
- 六問10秒的人類驗收未取得結果前，HQ-002保持待驗收；可以交付已審查文件，但不能把merge當成完整驗收證據。

## 參考

- [HQ-002任務](../tasks/in-progress/HQ-002.md)
- [架構與實作計畫](../projects/codex-xk-apparel-store/reports/HQ-002/architecture-plan.md)
- [健康規格](../docs/PROJECT_HEALTH_AND_RISK.md)
