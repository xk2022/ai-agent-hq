# 專案健康度與風險分類規格

Manager Mode 用健康度回答「目前核准目標是否能安全前進」，不把測試通過率、任務完成率或產品商用能力混成單一分數。本規格是 HQ 自訂管理資料規則，不是 Codex 設定，也不改變 Agent 的派工或執行權限。

## 狀態分開記錄

| 軸 | 允許值／呈現方式 | 判斷內容 |
| --- | --- | --- |
| 專案健康度 `health` | `Healthy`、`Needs Attention`、`At Risk`、`Blocked`、`Unknown` | 相對於 `health_scope` 中的目前核准目標作管理評估 |
| 掃描流程狀態 | 專案管理 `status`，例如 `pending_scan`、`scan_completed`；摘要可記為 `scan_status` | 是否完成掃描，不代表健康或商業就緒 |
| 證據狀態 | `verified` 已驗證、`inferred` 推論、`not_executed` 未執行、`unknown` 未知 | 每一主張是否有實際來源；健康度通常是 `inferred` |
| 任務狀態 `task_status` | 沿用 `pending`、`in_progress`、`blocked`、`awaiting_review`、`completed` | 實際派工及 Main Agent 驗收狀態，不由摘要自行創造新狀態 |
| 批准狀態 | `not_required`、`pending`、`approved`、`rejected` | 具體行動是否取得使用者批准；與證據狀態獨立 |
| 商業就緒度 `business_readiness` | `Ready`、`Not Ready`、`Unknown`，附適用條件與缺口 | 是否滿足指定營運目標；原型測試成功不能直接判為 `Ready` |

例如「發現一個 High 套件」可為已驗證；「建議升版」是管理建議；「是否批准升版」仍可為待批准。批准不會把未執行工作變成已完成，任務完成也不代表所有建議都已獲准。

## 五類健康度

每次評估先明列核准目標、來源 revision、證據日期及未驗證範圍，再使用以下條件：

| 健康度 | 判斷條件 | 必須交付的管理資訊 |
| --- | --- | --- |
| Healthy | 當前目標所需證據足夠且適用，無阻塞、無威脅該目標的未處理重大風險 | 判斷依據、證據日期及仍不包含的範圍；測試全過不能單獨成立 |
| Needs Attention | 有具體待處理發現或部分驗證缺口，仍可在已核准範圍與現有控制下前進 | 問題、owner、建議下一步與是否需批准 |
| At Risk | 重大且未充分緩解的安全、資料、品質或交付風險已威脅當前核准目標，但尚未完全停止工作 | 影響、已知暴露面、降低風險措施及處理優先級 |
| Blocked | 已核准工作實際無法繼續，必須補權限、資源、依賴或具體決策 | 阻塞原因、受影響工作及可驗證的解鎖條件 |
| Unknown | 缺少、失效或互相矛盾的必要證據，無法對當前目標作可靠判斷 | 未知項目、缺少的證據及下一次查核方式 |

使用順序：先辨識實際阻塞及威脅當前目標的重大風險，再判斷證據是否足夠；沒有前述情況時，依待處理事項區分 Needs Attention 與 Healthy。已知 High 風險不得因整體狀態 Unknown 而從首頁消失。

健康度必須限定範圍。假資料原型可為 Needs Attention，但同一成果仍可能不具正式商用能力。若下一階段尚未批准，不能只因候選方案等待批准就將目前專案標為 Blocked。發布目的地或內容若不符合使用者核准的受眾範圍，則阻塞該發布工作，與產品原型健康度是不同範圍。使用者選擇公開不等於同意公開憑證、個資或私密執行資料；新增內容仍須發布前審查，不自行部署。

## 風險與優先級

每個風險至少包含：ID、管理者可理解的一句話、適用範圍、影響、證據狀態、來源連結、來源嚴重度、管理優先級、處理狀態、owner、下一步及批准狀態。

- **來源嚴重度**：沿用工具或審查來源的 `Critical`／`High`／`Moderate`／`Low`；來源未給時標「未分級」，不可編造 CVSS 或公告數。
- **管理優先級**：P0＝指定活動開始前必須解除的門檻；P1＝下一批優先處理；P2＝後續改善。優先級是管理評估，不能改寫來源嚴重度。
- **處理狀態**：`open`、`mitigated`、`resolved`、`unknown`。`mitigated` 必須寫控制範圍；不能當成已修補。`resolved` 必須有修補後驗證證據，不能只依建議、PR 建立或歷史測試通過。
- 風險數量須說明計數單位。例如「1 個 High vulnerable package、2 項 advisories」不能縮成「2 個 High 套件」，也不能只顯示測試通過而隱藏 audit 失敗。
- High 套件不自動證明產品 runtime 可被遠端利用；應分開已知版本命中、受影響執行環境、實際暴露面與尚未重現的影響。

## 摘要格式與可追溯性

每個專案使用 `projects/<project-id>/executive-summary.md`，依 [摘要模板](../templates/EXECUTIVE_SUMMARY.md) 保留八個區塊：一句話狀態、任務進度、重要發現、風險與優先級、商業就緒度、Main 建議、管理者待決策事項、原始報告與證據。

Frontmatter 最少包含：`schema_version`、`project_id`、`summary_updated`、`evidence_as_of`、`source_revision`、`health`、`health_evidence_status`、`health_scope`、`business_readiness`、`task_id`、`task_status`；`scan_status` 記錄對應的專案掃描流程。日期用字串，revision 使用完整 SHA；這些是 HQ 自訂 metadata。摘要及首頁不得以 health 覆寫任務執行狀態、掃描權限或 Agent 設定。

每一重要主張都必須能從摘要進入原始報告，再進入實際 log／JSON 或固定 revision 的檔案。首頁只提取短摘要與導航；完整技術日誌保留在原路徑，不預設展開。缺少證據以未知或未執行呈現，不補零值或假造通過。

任務進度只可使用已核准且定義清楚的分母，例如「HQ-001 三份主報告已交付 3／3」。沒有核准的全產品工作分解與驗收基準時，不產生「產品完成百分比」。Agent 角色、結果與最近完成資訊採實際執行／驗收紀錄，不因 TOML 存在就稱角色已執行。

## 建議與決策的邊界

Main 建議與管理者待決策事項分開呈現。每個決策有固定 ID、問題、選項、Main 建議、批准狀態及批准範圍。只有取得對具體操作的明確批准，才記錄 `approved`、批准者、時間與適用工作包；不得將推測意圖、沉默或另一工作包的批准視為同意。

Manager Mode 的核准不會自動授權受管理專案的原始碼變更、正式憑證、部署或付費資源。決策欄位是管理紀錄，不是可觸發執行的按鈕，也不能繞過現有 Main Agent 派工及驗收流程。

## 證據新鮮度與衝突處理

- 分開顯示摘要整理日、原始證據日、產品 revision，以及是否重查目前來源；重新排版摘要不等於重跑測試或安全審計。
- 來源未重查時保留「截至某日的評估」，並標目前來源未重新驗證，不宣稱即時健康。
- revision 改變、關鍵證據衝突或未滿足經管理者批准的複查政策時，標示需重新評估；不得僅更新日期恢復 Healthy。不自行設定未批准的過期天數。
- 保留歷史已知風險；未重跑 audit 不代表漏洞已消失。對目前狀態無可靠依據時可為 Unknown，但歷史 finding 仍須可見。
- 任務索引與已接受的 execution record 衝突時，指出來源與原因，由 Main 核對後同步管理資料；不改寫歷史報告以製造一致。

## 首個專案的分類基準

`codex-xk-apparel-store` 的 [HQ-001 execution record](../projects/codex-xk-apparel-store/reports/HQ-001/execution-record.json) 記錄 2026-11-16 掃描完成、25／25 測試、1 個 High 套件及 2 項 advisories。管理摘要採 **Needs Attention〔推論、prototype 範圍〕**，因仍有未修補的測試工具鏈風險與驗證缺口；商業就緒度採 **Not Ready〔管理評估〕**，不是以測試成功掩蓋正式化門檻。

96.32% 僅為 catalog／model 兩個建置 JS 檔的行覆蓋率，app 未量測；真實瀏覽器、目前 Pages 健康與正式服務未驗證。詳見 [首份管理摘要](../projects/codex-xk-apparel-store/executive-summary.md) 及所附原始證據。
