# HQ-001：Initial Repository Architecture Audit

- 專案：`codex-xk-apparel-store`；來源：<https://github.com/xk2022/codex-xk-apparel-store>。
- 查核日期：2026-11-16，UTC；本輪執行紀錄見 [execution-record.json](execution-record.json)。
- 固定 revision：`main@1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422`。
- 執行總管：Main Agent；Architect、Research、QA、Security 四個 Subagent 已依各自 TOML 指令執行、交付並由 Main 複核整合。這是明確派工及讀取角色指令，不宣稱已驗證原生 custom-agent loader。
- 授權：READ ONLY；不修改任何已追蹤檔案、不建立 Commit、不推送、不部署、不接觸正式憑證。

本文的 `path:line` 均指上述 SHA，原始碼可由[固定版本目錄](https://github.com/xk2022/codex-xk-apparel-store/tree/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422)查核。「已驗證」限實際閱讀或命令結果；「推論」表示依資料流推導，未動態重現；「未執行」不視為通過。原型文件中 2026-11-13 的驗收紀錄與本次重跑結果分開記錄。

## 1. 驗收結論

**掃描交付完成，型別檢查、建置及 25／25 項測試通過；依賴安全審計有發現，不能判定為可正式營運。**

| 項目 | 本次結果 | 實際證據 |
| --- | --- | --- |
| 安裝 | 完整 lifecycle `npm ci --offline --no-audit --no-fund`，exit 0；未略過安裝 hook | [npm-install.json](evidence/npm-install.json)、[原始日誌](evidence/npm-install.log) |
| 型別檢查／建置 | `npm test` 內的 `tsc --noEmit && node build.mjs` 成功，產生隔離副本的 `dist/` 與 `review.html` | `package.json:8-9`；[npm-test.log](evidence/npm-test.log) |
| 測試 | 25 項：15 模型、6 happy-dom DOM、4 離線產物；25 pass、0 fail／skip | `tests/model.test.mjs:10-139`、`tests/ui.test.mjs:50-257`、`tests/artifact.test.mjs:10-92`；[npm-test.json](evidence/npm-test.json) |
| 有限範圍 coverage | `catalog.js` 與 `model.js` 合計行 96.32%、分支 84.69%、函式 86.36% | [npm-coverage.log](evidence/npm-coverage.log)、[執行 metadata](evidence/npm-coverage.json)；不是全專案數值 |
| 依賴 audit | exit 1：happy-dom 20.14.6 為 1 個 High vulnerable package，對應 2 項 advisory | `package-lock.json:556-560`；[audit JSON](evidence/npm-audit.log)、[命令 metadata](evidence/npm-audit.json) |
| 已追蹤檔案保護 | HQ 28 檔、來源 30 檔、測試副本對應 30 檔的 SHA-256 均與基準一致；HEAD 未變 | [readonly-integrity.json](evidence/readonly-integrity.json) |

安全 finding 與測試通過並存；未執行依賴修補或任何新功能。正式會員、伺服器 DB、金物流與多人庫存原先即排除於原型範圍，並非以本輪掃描要求偷偷擴充的驗收標準（`docs/REQUIREMENTS.md:34`、`README.md:49`）。

## 2. 專案目錄、技術棧與設定

| 面向 | 已驗證內容 | 證據 |
| --- | --- | --- |
| 架構 | 無前端框架的 TypeScript 靜態 SPA，HTML shell、DOM renderer、hash 路由；沒有後端或 DB 執行元件 | `index.html:19-25`、`src/app.ts:1-21,303-315,589-590`；來源 tracked tree 30 檔 |
| 模組 | `src/catalog.ts` 商品與 SKU；`src/model.ts` 純函式規則；`src/app.ts` UI、狀態與儲存 | `src/catalog.ts:1-26`、`src/model.ts:1-67`、`src/app.ts:1-64` |
| 其他目錄 | `assets/` 有 hero 與 8 商品 JPEG；`tests/` 三個測試檔；`docs/` 五份需求／資料／驗收／交接／素材文件；一個 CI YAML | 來源 tracked tree；`build.mjs:14-17,26-37`；[architecture.md](architecture.md) 目錄表 |
| Node／npm | manifest 要求 Node `>=24`；實際 Node v24.22.1、npm 11.9.0；CI Node 24 | `package.json:6`、`.github/workflows/ci.yml:14-19`；[runtime.json](evidence/runtime.json) |
| 開發依賴 | lock v3；實裝 TypeScript 5.9.3、esbuild 0.25.12、happy-dom 20.14.6；不是把 manifest caret 下限當實裝版本 | `package-lock.json:4,514-519,556-559,575-578`；[runtime.json](evidence/runtime.json) |
| TypeScript | ES2022、ESNext、Bundler resolution、strict、noEmit、skipLibCheck；include `src/**/*.ts` | `tsconfig.json:2-12` |
| 建置 | 型別檢查後 esbuild 產多檔 ESM、source maps；另產 IIFE／CSS／9圖內嵌單檔離線版 | `package.json:8`、`build.mjs:3-50`；[npm-test.log](evidence/npm-test.log) |

## 3. 商品、訂單與儲存

| 結構／行為 | 已驗證事實 | 證據 |
| --- | --- | --- |
| Product／Variant | 8 款假商品；Product 單一整數價格、圖、描述、材質、版型、variants；SKU 有顏色、尺寸、有限配額、預購及備貨日 | `src/catalog.ts:1-116` |
| Cart | `{variantId, quantity}`；合併同 SKU，檢查正安全整數、溢位、價格與可購量，摘要重新計算 | `src/model.ts:11-30,76-144`；模型測試及 npm-test 日誌 |
| Order | 訂單與付款狀態、顧客示意欄位、SKU／單價／品名快照、一次運費、混單、最長備貨日、回補旗標、`simulated: true` | `src/model.ts:31-67,157-181` |
| 下單／取消 | 全單驗證後 clone 扣量，不改輸入；同 ID 重試回傳舊訂單；取消僅在備貨中回補一次；card／COD 都是模擬 | `src/model.ts:157-195`；`tests/model.test.mjs:65-131` |
| 營運規則 | 訪客可購買；現貨預購可混單、到齊整單寄、一次運費。NT$65／滿2,000免運、配額與交期是示意假設 | `src/model.ts:5-9,115-124`、`docs/REQUIREMENTS.md:44-66` |
| 持久化 | `xk-apparel-demo-v1` 單一 localStorage key 保存 products／cart／orders／member；僅檢查三者是 Array，失敗退回本次記憶體 | `src/app.ts:28-64` |
| 正式資料模型 | `docs/DATA_MODEL.md` 是候選草案，尚非 ORM、Migration 或已建立 DB | `docs/DATA_MODEL.md:3-5,42-58,69-99`；tracked tree |

單次模型的 clone 保護不等於資料庫交易；本機順序最後一件測試也不證明跨分頁或多人併發安全。深度結構驗證不足、整包覆寫與保存失敗後仍走成功頁的影響是靜態推論，未在本輪注入壞資料重現（`src/app.ts:42-64,541-559`；`docs/ACCEPTANCE.md:36`）。

## 4. 前端功能與使用者流程

已閱讀實作：首頁與商品列表 → 分類／現貨預購篩選／搜尋／價格排序 → 商品詳情選色、尺寸、數量 → 購物袋 → 訪客結帳與示意門市／付款 → 訂單確認。另有展示會員、本機查單、示意後台取消及配額修改／重設（`src/app.ts:102-164,183-315,390-475,500-559`）。

本次 happy-dom 實測包含混單 COD 下單與重載、會員展示、本機取消回補、配額更新阻擋結帳、購物車草稿保留、降量、連續商品深連結與鍵盤焦點；離線版亦執行內嵌腳本選規格加車（[npm-test.log](evidence/npm-test.log)）。搜尋／排序／分類／重設不在現有六項 UI 案例中；不把功能存在寫成全數已操作驗收。

三項可追蹤落差：

1. 需求要求商品「多圖」，目前每商品只有一張且 detail renderer 只使用 `p.image`，沒有 gallery。證據：`docs/REQUIREMENTS.md:27`、`src/catalog.ts:26-116`、`src/app.ts:208-217`。需後續決定補作或調整範圍。
2. `UI-11` 宣稱重設 DOM 通過，現有測試只有重載恢復的支持，六個案例無 reset 操作。證據：`docs/ACCEPTANCE.md:21`、`tests/ui.test.mjs:50-257`；不是斷言重設程式壞掉。
3. 需求文件仍寫 Pages 尚待啟用，與 README、驗收文件及本次歷史 run 證據不一致。證據：`docs/REQUIREMENTS.md:80-82`、`README.md:27-35`、[github-pages.json](evidence/github-pages.json)。

## 5. 安裝、測試及覆蓋率的實際執行

- Cloud source：`/workspace/scratch/HQ-001-1qnZaIVi/source`；可丟棄測試副本：`/workspace/scratch/HQ-001-1qnZaIVi/test-copy`，sandbox 內為 `/workspace/work`。
- 先以禁用 lifecycle 的 install 取得 lockfile 套件，實讀 esbuild `install.js:1-289`。完整安裝才允許已審查 hook；hook 可寫套件內檔、執行 native binary version check，fallback 下載在完整安裝階段由無網路控制阻擋。證據：[install-hook-review.json](evidence/install-hook-review.json)。
- bwrap 將來源對應的每個 tracked 檔案 ro-bind；只在新副本、cache 與私有 tmp 產生輸出。環境使用 allowlist、停用使用者及全域 npm 設定，遮蔽 home／原 workspace，不傳 auth variables。完整安裝、測試及 coverage 均 `--unshare-net`。證據：[run-checks.py](evidence/run-checks.py)、各命令 metadata。

| 時間（UTC，2026-11-16） | 命令 | Exit | 結果／證據 |
| --- | --- | ---: | --- |
| 09:35:07–12 | `npm ci --ignore-scripts` | 0 | 下載 12 個當前平台套件、未執行 hook；audit 摘要顯示 high；[prepare log](evidence/npm-prepare.log) |
| 09:35:52–53 | `npm audit --json` | 1 | 1 High package／2 advisories；沒有執行 fix；[audit log](evidence/npm-audit.log) |
| 09:36:17–23 | `npm ci --offline --no-audit --no-fund` | 0 | 完整 lifecycle，使用預填 cache；單獨保留上列 audit finding，沒有因 no-audit 隱藏它；[install log](evidence/npm-install.log) |
| 09:36:37–42 | `npm test` | 0 | build 與 25／25 通過；[test log](evidence/npm-test.log) |
| 09:36:57–09:37:00 | `node --test --test-isolation=none --experimental-test-coverage --test-coverage-include=dist/assets/*.js tests/artifact.test.mjs tests/model.test.mjs tests/ui.test.mjs` | 0 | 再跑 25／25，產生下列有限 coverage；[coverage log](evidence/npm-coverage.log) |

37 個 lockfile 非 root entries 含跨平台 optional，不等於此平台實際安裝 37 個（見 lockfile、prepare log）。安裝與完整測試前曾有掛載目的路徑唯讀、npm user/global 同指 `/dev/null` 的設定錯誤；已分別修正 writable private workspace、使用不同空設定路徑。前者未啟動 npm，後者未執行測試；記錄保留於 [sandbox setup](evidence/sandbox-setup-attempt.log) 與 [npm config attempt](evidence/npm-config-attempt.log)，不可解讀為被省略的測試失敗。

| 實際列入 coverage 的檔案 | 行 | 分支 | 函式 |
| --- | ---: | ---: | ---: |
| `dist/assets/catalog.js` | 98.11% | 100.00% | 83.33% |
| `dist/assets/model.js` | 94.61% | 83.15% | 87.50% |
| 以上兩檔合計 | 96.32% | 84.69% | 86.36% |

這是 Node V8 對建置後 JS 的量測；app 在 happy-dom 中由 bundle eval，未列入此表。未量測完整 TypeScript 專案／前端來源覆蓋率。未執行真實瀏覽器、手機視覺／觸控、螢幕閱讀器、正式後端或跨使用者併發驗收。coverage 不代表商用安全或功能完整。

## 6. GitHub Actions 與 Pages

| 面向 | 本次證據與結論 |
| --- | --- |
| 品質 CI | `.github/workflows/ci.yml:1-26` 在 main push／PR／手動時以 Node 24 安裝、測試、上傳產物，保存14天；只授 `contents: read`，無 deploy step。固定 SHA 的 [run 43373108942](https://github.com/xk2022/codex-xk-apparel-store/actions/runs/43373108942) 已於2026-11-13 05:36:39Z完成成功；metadata 本次重查，非本輪觸發。 |
| Pages 方式 | README `:27-35` 記錄將 `dist/` 放至 `gh-pages` root，以分支發布；main 修改不自動同步產物。本次讀取當前 gh-pages ref 為 `302f9580fa6b74f153964d8834274510f5f638cc`。 |
| 歷史部署 | [Pages run 43359061053](https://github.com/xk2022/codex-xk-apparel-store/actions/runs/43359061053) 在上述 gh-pages SHA 於2026-11-13完成成功；build／report-build-status／deploy jobs及部署step皆 success。 |
| 本次未驗證 | 沒有重新開網站、做HTTP／資源比對、操作Pages設定或驗證線上產物對應目前main；不能將歷史success等同現在網站健康。本輪沒有部署。deployments endpoint 不受 connector 支援，錯誤不是「無部署」證據。 |

最小化 API 證據：[github-actions.json](evidence/github-actions.json)、[github-pages.json](evidence/github-pages.json)。`docs/ACCEPTANCE.md:59-64` 的17檔HTTP200是歷史文件聲明，未當成本次重測。源碼／產物分支需另保留 provenance 以降低漂移風險，這是改善建議。

## 7. 安全風險與商業化缺口

| 優先級／適用範圍 | 發現與影響 | 證據／界線 |
| --- | --- | --- |
| P1，現在的開發測試工具鏈 | happy-dom **20.14.6** 命中 host code execution 與 SSRF 兩項 high advisories；需另審相容性後升到涵蓋兩者的21.0.4或較新版本 | [audit](evidence/npm-audit.log)；[GHSA-834v-8h66-3h79](https://github.com/advisories/GHSA-834v-8h66-3h79)、[GHSA-c8p4-j97h-3vg8](https://github.com/advisories/GHSA-c8p4-j97h-3vg8)。屬dev/test，不宣稱商城靜態runtime已可遠端利用；本輪僅使用已審查本地HTML，無網路隔離執行，未攻擊或修補 |
| P1，原型健壯性 | persisted JSON 缺深度schema、保存失敗仍走成功頁、無跨分頁同步；有損壞／失去更新的推論風險 | `src/app.ts:42-64,541-559`；目前已有一次toast fallback提醒，不是完全沒有處理；未動態重現 |
| P0，任何正式商用前 | 管理後台與會員僅本機展示；價格、庫存、下單、取消由client決定，沒有伺服器認證授權、DB交易、權威付款 | `src/app.ts:290-315,390-400,450-452,500-559`；`src/model.ts:157-195`；`README.md:49`。已揭露的原型限制，不是本輪要求實作正式服務 |
| P0，任何真實個資前 | 顧客聯絡資料隨訂單進localStorage，未見TTL；不能把展示資料儲存當真實會員／訂單治理 | `src/model.ts:32,48-65`、`src/app.ts:55-63,251,467-475`；僅分析欄位，未接觸真實資料 |
| P2，工程維護 | Actions 以v4 tag而非完整SHA、缺timeout；source／Pages產物分支分離；測試／驗收文件缺口 | `.github/workflows/ci.yml:11-26`、`README.md:31`、上述三項落差；不代表帳號沒有額外組織層控制 |

正向控制包括 HTML `esc()`、訊息及錯誤 `textContent`、清楚假商品／模擬付款提示、無卡號欄位、CI唯讀權限、有限安全整數及一次回補保護（`src/app.ts:69-87,251,528-557`、`src/model.ts:76-195`、CI `:7-8`）。這些不構成全面安全保證。詳細範圍與每項引用見 [security-report.md](security-report.md)。

正式化還需確認商品與素材、品牌／店家政策、金物流及發票供應商、預算、庫存保留／過期／退款／未取等規則；候選資料模型與流程已有草案，尚未授權開發（`docs/REQUIREMENTS.md:68-76`、`docs/DATA_MODEL.md:38-99`、`docs/ASSET_SOURCES.md:3-29`）。候選優先順序與驗收條件見 [roadmap.md](roadmap.md)。

## 8. HQ 交接與限制

- 三份主交付：[scan-report.md](scan-report.md)、[architecture.md](architecture.md)、[roadmap.md](roadmap.md)。四份子報告為 [Architect](architect-report.md)、[Research](research-report.md)、[QA](qa-report.md)、[Security](security-report.md)；Main已核對關鍵原始碼、實測日誌與跨報告差異。
- 已重查公開產品工作項目：API回傳 Issue #1及PR #2/#3/#4皆closed，未見open紀錄；closed PR不直接解讀為全部商用驗收完成。新候選工作未建Issue、未排程、未同步日曆。證據：[github-work-items.json](evidence/github-work-items.json)；`docs/ACCEPTANCE.md:63-64`。
- 本輪使用者「不得修改已追蹤檔案」優先於既有HQ狀態移動／work-log更新流程，因此未移動或改寫 tracked task、registry、project.yml、work-log.md。它們保留初始化狀態；本次專案獨立執行／驗收紀錄在此新增報告目錄與 [execution-record.json](execution-record.json)，不聲稱已同步遠端狀態。
- 報告只在HQ本機新檔交付，未提交、推送或開PR。不得將本輪掃描完成解讀為產品正式上線驗收、所有待辦完成或下一階段已獲授權。
- Main Agent驗收：本次要求的盤點、命令及證據已交付；上述風險與未驗證範圍一併保留。等待下一個任務，不啟動候選開發或背景監看。
