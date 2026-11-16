# HQ-001-Q：QA 掃描報告

## 任務與範圍

- Project：`codex-xk-apparel-store`；Repository：<https://github.com/xk2022/codex-xk-apparel-store>。
- Role：QA；派工者／最終驗收：Main Agent。
- 查核日期：2026-11-16 UTC。
- 固定 revision：`main`／`1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422`。
- 唯讀來源：`/workspace/scratch/HQ-001-1qnZaIVi/source`。
- 權限：`read_only`；僅本報告及 `evidence/qa-*` 為允許寫入的 HQ 路徑，不修改受管理專案或其他已追蹤檔案。
- 本報告的 `path:line` 均指上述固定 revision，原始來源基準為 <https://github.com/xk2022/codex-xk-apparel-store/tree/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422>。
- 本報告依 QA TOML 的職責與 HQ 回報模板執行；不代表原生 custom-agent loader 已經驗證。

## 靜態檢查結果

| 發現 | 狀態 | 證據 | 影響／限制 |
| --- | --- | --- | --- |
| 專案要求 Node.js >=24，test 先跑型別檢查及建置，再執行 Node test runner | 已驗證 | `package.json:6-9`、`tsconfig.json:2-11` | `npm test` 同時驗證 build，與真實瀏覽器或後端整合測試不同 |
| 直接開發依賴為 TypeScript、esbuild、happy-dom；lockfile v3 固定解析版本為 5.9.3／0.25.12／20.14.6 | 已驗證 | `package.json:11-14`、`package-lock.json:4`、`:514-519`、`:556-559`、`:575-578` | manifest 的 caret 範圍不等於每次使用最新版；`npm ci` 以 lockfile 為準 |
| root scripts 只有 build、test，未定義 root 安裝生命週期 hook；lockfile 中唯一 `hasInstallScript` 為 esbuild | 已驗證 | `package.json:7-10`、`package-lock.json:514-519`；逐項解析 lockfile 的 37 個非 root package entries | 37 包含跨平台 optional 套件，不能當成當前平台實際安裝數；esbuild hook 執行前仍須審查其封包內腳本 |
| 建置會刪除及重建 `dist/`，並產生 `review.html`，不改來源碼 | 已驗證 | `build.mjs:3-17,18-50`；`.gitignore:1-3` | 必須在隔離副本執行，且這些產物均未追蹤；不能把 build 當作純讀取命令 |
| UI tests 用 happy-dom 啟用記憶體內 JavaScript；停用 JS/CSS 檔案與圖片載入 | 已驗證 | `tests/ui.test.mjs:8-29` | 不驗證 CSS 排版、真實觸控、瀏覽器兼容性或螢幕閱讀器 |
| 離線產物測試檢查內嵌 classic scripts、9 張 JPEG byte 一致，並封鎖 file-URL 範例中的 fetch/XHR | 已驗證 | `tests/artifact.test.mjs:10-42,45-91` | 可以支持離線產物結構／DOM操作；來源字串掃描不等於動態安全稽核 |
| CI 對 push main／PR／手動觸發安裝與測試，最後保存 `review.html` 及 `dist/` 14 天 | 已驗證 | `.github/workflows/ci.yml:2-26` | 這是配置檢查，不能單靠此檔宣稱某次遠端 CI 或 Pages 部署成功 |

## 測試範圍與覆蓋缺口

### 既有 25 個測試的靜態盤點

| 測試組 | 案例數 | 主要情境 | 證據 |
| --- | ---: | --- | --- |
| 模型 | 15 | SKU 合併、數量整數與溢位、免運門檻、現貨／預購混單、庫存額度、訪客結帳、輸入不變、最後一件順序競購、訂單快照、ID重試、取消／回補一次、COD | `tests/model.test.mjs:10-139` |
| DOM 互動 | 6 | 混單及COD結帳／重載、庫存修改阻止結帳／移除、草稿保留、過量購物車降量、商品深連結、鍵盤焦點圈／Escape | `tests/ui.test.mjs:50-257` |
| 離線產物 | 4 | 無外部style/script、9圖內嵌、無遠端交易client字串、file URL點擊選規格／加入購物車 | `tests/artifact.test.mjs:10-92` |

以上案例數由實際 `test(...)` 宣告盤點；執行結果另列，不能把靜態盤點當成通過證據。

| 缺口／限制 | 狀態與證據 | 建議 |
| --- | --- | --- |
| Repository 沒有既有 coverage 指令、數值報告或最低門檻；本輪額外實測僅涵蓋兩個產物模組 | 已驗證：`package.json:7-10`、CI `:18-19`；本輪 `evidence/npm-coverage.log` | 不能將下方 catalog/model 產物覆蓋率當成全專案或前端app覆蓋率；後續建立來源對應與UI量測，再決定門檻 |
| 未包含真實瀏覽器、手機觸控、視覺、螢幕閱讀器驗收 | 已驗證：測試載入 happy-dom；`tests/ui.test.mjs:8`、`docs/ACCEPTANCE.md:40-42,57,64` | 優先補桌面／手機關鍵購物流程及鍵盤／無障礙驗收 |
| 單模型最後一件順序測試不代表跨分頁／多人併發安全 | 已驗證：`tests/model.test.mjs:79-83`；`docs/ACCEPTANCE.md:36` | 未有後端前保留此限制；正式版以交易／庫存保留及並發測試驗收 |
| 搜尋／排序／分類、重設流程、localStorage損毀／寫入失敗未有現有UI自動測試案例 | 已驗證：完整6個案例清單；對照 `src/app.ts:42-63,140-154,467-475` | 以read-only檢視列候選回歸測試，本次不新增專案測試 |
| UI-11 的「後台重設恢復初始資料」DOM通過聲明，無法單靠這6個UI測試支持 | 已驗證：`docs/ACCEPTANCE.md:21` 對照 `tests/ui.test.mjs:50-257`，沒有操作 `data-action=reset` 的案例 | 主張需補過往手動證據或新增測試；本次不把文件勾選當作重設實測通過 |
| 正式會員、管理者授權、DB交易、金物流／發票、回調驗簽、備份及監控未被原型測試驗收 | 已驗證：`docs/ACCEPTANCE.md:40,45-47`；測試本身僅本機資料模型和DOM | 正式版啟動前需新授權、測試環境與獨立驗收證據 |

## 命令、實測結果與覆蓋率

Main Agent 已提供本輪實測資料；QA 直接讀取並核對 JSON 命令紀錄與完整測試日誌。固定 revision 與本報告一致。執行副本為 `/workspace/scratch/HQ-001-1qnZaIVi/test-copy`，sandbox 內工作目錄為 `/workspace/work`。

| 時間（UTC） | 命令／階段 | Exit code | 實際結果與證據 |
| --- | --- | ---: | --- |
| 2026-11-16 09:35:07–12 | `npm ci --ignore-scripts` | 0 | 先下載並安裝套件、停用生命週期腳本；新增12個平台實際套件。`evidence/npm-prepare.json`、`evidence/npm-prepare.log` |
| 09:35:52–53 | `npm audit --json` | 1 | 一個直接開發依賴 happy-dom 的 high severity vulnerability entry，含兩則 advisory；不是測試失敗。`evidence/npm-audit.json`、`evidence/npm-audit.log` |
| 09:36:17–23 | `npm ci --offline --no-audit --no-fund` | 0 | 審查 esbuild install.js 後，在無網路的 bwrap 重新執行完整 install lifecycle，新增12個套件。`evidence/npm-install.json`、`evidence/npm-install.log`、`evidence/install-hook-review.json` |
| 09:36:37–42 | `npm test` | 0 | `tsc --noEmit`、esbuild建置成功；25個測試全部通過，0失敗／取消／跳過／todo。`evidence/npm-test.json`；`evidence/npm-test.log:2-42` |
| 09:36:57–09:37:00 | Node test runner 加 `--experimental-test-coverage --test-coverage-include=dist/assets/*.js`，執行既有三個測試檔 | 0 | 再次25／25通過，回報篩選後 catalog.js／model.js 覆蓋率。`evidence/npm-coverage.json`、`evidence/npm-coverage.log` |

安裝腳本審查涵蓋 esbuild@0.25.12 `install.js:1-289`；其作用是定位平台optional native binary、檢查版本與寫入套件內檔案，缺少binary時才嘗試下載。完整lifecycle階段已使用離線cache與停用網路，來源已追蹤檔唯讀mount，環境只保留allowlist且無auth variables，停用原本user/global npm設定。此為 Main Agent 的執行紀錄與審查，不是 QA 自行啟動模型、安裝或呼叫正式服務。

前兩次啟動有已解決的測試環境錯誤：第一次 bwrap 無法在唯讀根目錄建立 `/work`；第二次 npm 因 user/global同指 `/dev/null` 拒絕重複載入。相關 exit code 皆為1，實際 npm install/test 尚未開始；修正隔離工作目錄與分離空config後重試通過。證據：`evidence/sandbox-setup-attempt.json/.log`、`evidence/npm-config-attempt.json/.log`。不可將這兩次設定失敗隱藏，也不應解讀為產品測試案例失敗。

**本輪測試結果：25／25通過（15模型、6 DOM、4離線產物）。** `npm test` 本身不產生coverage；下表來自 Main Agent 額外啟用 Node 24 內建實驗性coverage的實際執行，非由案例數推估。

| 本輪coverage實際列出的產物檔 | Line % | Branch % | Function % |
| --- | ---: | ---: | ---: |
| `dist/assets/catalog.js` | 98.11 | 100.00 | 83.33 |
| `dist/assets/model.js` | 94.61 | 83.15 | 87.50 |
| 篩選後上述兩檔合計 | 96.32 | 84.69 | 86.36 |

證據：`evidence/npm-coverage.log` 的 coverage report，完整命令與隔離條件見 `evidence/npm-coverage.json`。`app.ts` 在DOM測試中由esbuild產生bundle並經happy-dom `eval` 執行（`tests/ui.test.mjs:12,28`），未列入此表；**不能稱全專案96.32%覆蓋、前端app已完整覆蓋，或將產物百分比直接套用TypeScript來源。** app數值覆蓋率仍未量測。真實瀏覽器、觸控、螢幕閱讀器、跨分頁併發、正式後端／金流／部署均未在本輪驗證。

### 依賴稽核限制

`happy-dom@20.14.6` 為測試用直接devDependency，audit回傳的1個high套件項目包含 GHSA-834v-8h66-3h79（不可信import alias host code execution）與 GHSA-c8p4-j97h-3vg8（解析不可信HTML的SSRF）。資料來源為本輪 `evidence/npm-audit.log`，完整安全分析由 Security Agent 與Main整合。當前 tests 只載入本repo程式與HTML，完整測試在無網路／無正式憑證環境執行；這不能證明漏洞不存在或一般使用皆安全。audit建議21.0.4且標為major update，本輪未執行 `npm audit fix`、未更新依賴或lockfile。後續修補需另外授權並重跑測試。

## 安全、交付與驗收

- QA 僅以唯讀命令讀取來源、解析 lockfile 與測試宣告，未自行執行 npm／專案 script、未安裝依賴。
- 未存取正式服務、正式憑證或客戶資料；不建立 Commit、不推送、不部署。
- 實際建立的 HQ 檔案只有本報告；原始碼與已追蹤檔案是否維持不變，待 Main Agent 整體baseline比對提供最終證據。
- 子任務狀態：已交付，靜態審查與本輪實測證據整合完成；最終主任務狀態與驗收由Main Agent決定。測試通過與依賴稽核high發現同時成立，不互相抵銷。
- 專案工作紀錄：由 Main Agent 在不修改已追蹤檔案的本次限制下，將本輪紀錄保存在新增的 HQ-001 報告中，不改原 `work-log.md`。
