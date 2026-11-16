# HQ-001：候選開發路線

來源固定於 `xk2022/codex-xk-apparel-store@1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422`；查核2026-11-16 UTC。以下皆為候選，**未建立新Issue、未啟動開發、未排程、未授權部署**。估計方向依本次原始碼、實測與四角色報告，不虛構工時或店家決策。

## 1. 優先序的適用條件

- 若下一階段仍是假資料原型，先處理下列P1工具鏈、健壯性、測試與文件，再進行實際使用者回饋。
- 若要收真實訂單、個資或款項，P0商用前置條件必須先定案；不能用25／25原型測試通過取代它們。
- P0表示正式化的停止門檻，不表示既有demo必須在本輪偷偷補齊正式服務。原始排除範圍見`docs/REQUIREMENTS.md:34`、`README.md:49`。
- 目前執行結果：[npm-test.log](evidence/npm-test.log)；安全發現：[npm-audit.log](evidence/npm-audit.log)；架構：[architecture.md](architecture.md)。

## 2. 原型下一批候選工作

| 候選 | 優先／角色 | 實際依據 | 建議交付與驗收條件 | 依賴／授權 |
| --- | --- | --- | --- | --- |
| D1 測試依賴安全升版 | P1；security、qa、integration | lock的happy-dom20.14.6；audit為1 High package／2 advisories，見`package-lock.json:556-560`及audit JSON | 審查涵蓋兩項advisory的21.0.4或較新版本與相容性；更新manifest/lock後重跑25測試、build、audit；記錄剩餘發現，不用`fix --force`直接越版 | 使用者核准來源變更；21屬major，需檢查Node及API相容性。原型目前不要將不可信HTML／外部模組送入happy-dom |
| D2 本機資料schema與保存失敗語意 | P1；architect、frontend、qa | `src/app.ts:42-64,541-559`；型別只在編譯期、save失敗後仍導成功hash | 定義版本化runtime schema／欄位與範圍檢查、舊資料遷移／可復原重設、持續的未保存提示；補壞JSON、內部壞shape、quota／禁儲存測試，不清除使用者資料 | 核准程式修改及資料相容策略；不先承諾可保存真實訂單 |
| D3 需求與驗收證據對齊 | P1；documentation、qa、product | `REQUIREMENTS.md:27,80-82`與`app.ts:208-217`、`ACCEPTANCE.md:21`、Pages歷史API證據 | 修正Pages過時文字；決定多圖是補作或明確排除；對重設驗收補可重現測試／原手動證據，無證據不得標通過 | 核准文件變更；多圖範圍需產品確認。僅更新文件不代表部署 |
| D4 真實瀏覽器／手機與無障礙驗收 | P1；qa、frontend、product | `tests/ui.test.mjs:8-29`只有happy-dom；`docs/ACCEPTANCE.md:40-42,64`明示未驗 | 桌面／手機選品→SKU→混單→訪客結帳→取消；檢查排版溢出、觸控、鍵盤、焦點、讀屏與錯誤提示；以viewport／瀏覽器版本／截圖或錄影／失敗證據交付 | 測試假資料；需要使用者對風格與流程回饋。不使用正式憑證 |
| D5 補回歸範圍及可解釋coverage | P2；qa、frontend | 六個UI測試未覆蓋搜尋／排序／分類／重設與storage失敗；現有coverage僅model/catalog | 增加關鍵分支案例，讓app來源有可對應coverage；分開模型／UI／瀏覽器指標，再核准合理門檻 | 先D1、D2相關介面契約；不以本輪96.32%冒稱全專案覆蓋 |
| D6 CI供應鏈與成品可追溯性 | P2；devops、security、release | CI `:11-26`以v4 tag、無timeout；README `:31` main與gh-pages不自動同步 | 釘Actions SHA、加執行時間限制與依賴檢查；紀錄source SHA、artifact雜湊與deploy run對應；若提案自動發布，先建立審核門檻 | 核准workflow變更；任何真實部署仍需使用者具體確認，不由本掃描授權 |
| D7 多圖與素材／商品內容 | P2；product、frontend、documentation | `REQUIREMENTS.md:27`多圖需求；`catalog.ts:26-116`每款單張、`app.ts:209`只render主圖；`ASSET_SOURCES.md:3-29`為示意素材 | 範圍核准後加入gallery與可及文字；或同步需求明確維持單圖。正式化時替換店家核准商品資料與合法素材 | 先D3產品決策；不得複製他店品牌／圖片或宣稱示意材質交期是真實承諾 |

## 3. 正式商用前必須核准的工作包

| 門檻／候選 | 優先／角色 | 目前證據與缺口 | 建議驗收 | 前置條件 |
| --- | --- | --- | --- | --- |
| P0-A 店家與產品政策 | P0；product、research | `REQUIREMENTS.md:68-74`的品牌、SKU、交期、取消退款、COD、預算與供應商未定案；`:44-57`是假設 | 店家批准正式商品／運費／預購延遲／取消退款／未取／客服政策；素材權利及商業責任確認 | 使用者及商家決策；不可將NT$65、2,000免運及示意庫存當承諾 |
| P0-B 權威API、DB與認證 | P0；architect、backend、database、security | `app.ts:28-64,290-315,500-559`全在client；DATA_MODEL `:3-5,42-58`只是草案 | 後端決定價格、庫存、訂單與身分；管理者RBAC與資源授權；DB schema／migration／備份還原；禁止客戶任意改價格或取消他人單 | 先P0-A及架構／資安審查、隔離測試環境；預算／資源另核准 |
| P0-C 庫存與訂單交易 | P0；database、backend、qa | `model.ts:157-195`只有本機clone與ID重試；`ACCEPTANCE.md:36,47`排除多人交易驗收 | 原子扣量／庫存保留及過期、唯一訂單／請求雜湊冪等；最後一件多人併發、重試、取消回補、重送等測試 | P0-B；確認線上付款／COD不同保留及取消規則，避免僅移植localStorage模型 |
| P0-D 個資及帳號治理 | P0，任何真實資料前；security、backend、product | `model.ts:32,48-65`收件聯絡欄位；`app.ts:55-63`整份localStorage，無TTL | 定義目的及最小欄位、權限隔離、傳輸／保存、到期刪除、備份與稽核；帳號及真實資料不沿用展示boolean/localStorage | 使用者確認政策與保存責任；掃描不用真資料驗證 |
| P0-E 金流、物流、發票及通知 | P0，相關功能上線前；integration、backend、qa、security | `model.ts:47,174,193-195`均模擬付款退款；`REQUIREMENTS.md:34`排除真服務 | 選定供應商與sandbox；驗簽、重送冪等、付款逾時／晚到、退款對帳、物流狀態、未取、發票作廢／折讓、通知；全部有測試證據 | P0-A/B/C/D、商家審核及各服務授權；正式憑證只進核准安全儲存，不寫repo |
| P0-F 營運與發布驗收 | P0，正式發布前；devops、monitoring、release、qa | `ACCEPTANCE.md:47,64`明示備份還原、監控及客戶驗收未完成；現有CI只測原型 | 監控／告警、事故處理、備份還原演練、回滾、權限及部署審核、店主操作與使用者驗收 | 前述正式能力完成；上線與付費資源需使用者明確確認 |

建議依賴：`政策 → 架構／API／DB／個資 → 庫存交易 → 供應商sandbox整合 → 真實瀏覽器及營運驗收 → 使用者核准發布`。監控、安全與測試設計須隨各階段同步，而非等到最後才補。此為基於上述缺口的規劃推論，不是已核准設計或時程。

## 4. 現有工作項目與下一次派工

- 本次只讀API回傳產品Issue #1與PR #2/#3/#4均closed；[github-work-items.json](evidence/github-work-items.json)保留查核時間及來源。這只支持既有原型交付已關閉的狀態，不代表本路線候選都已完成。
- 不新增或複製產品Issue，不更新現有Issue、日曆或正式工作流；各候選需先由使用者選定並授權，再由Main拆解成有唯一owner／revision／可寫路徑／驗收條件的工作包。
- 建議下一個可獨立審核工作包是D1：測試依賴安全升版與回歸；D2／D3可於後續授權後平行。若使用者的下一步是商用，先開P0-A/B/D設計審查而非直接串付款。
- 本輪只有三份主報告及其子報告／證據新檔；既有tracked任務、registry、project.yml與work-log未更動，沒有Commit、推送或部署。等待下一個任務。
