# HQ-001-S：Security Agent 工作回報

## 任務與範圍

- 專案：`codex-xk-apparel-store`。
- Repository：<https://github.com/xk2022/codex-xk-apparel-store>。
- 來源：`main@1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422`，2026-11-16 UTC 查核。
- 唯讀工作目錄：`/workspace/scratch/HQ-001-1qnZaIVi/source`。
- 角色：Security Agent；已讀取並套用 HQ 的 `.codex/agents/security.toml`、`AGENTS.md`、`templates/AGENT_REPORT.md` 及目標專案 `AGENTS.md`。
- 授權：使用者 HQ-001 唯讀掃描；Main Agent 指派靜態安全、依賴與 CI／部署風險盤點。
- 子任務結果：已交付靜態分析，等待 Main Agent 複核；不自行更新主任務狀態。
- 唯一寫入：本未追蹤報告。未修改受管理專案、未建立 Commit、未部署、未接觸正式憑證或正式服務。

本文的 `path:line` 均指上述完整 SHA；可在[固定 revision](https://github.com/xk2022/codex-xk-apparel-store/tree/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422) 查核。風險優先序區分「目前示意原型」與「正式營運前阻擋項目」，不把已揭露的示意功能誤報為現有正式系統漏洞。

## 結論

**已驗證：這是純前端、假商品與模擬交易原型，沒有正式身分驗證或後端交易權威，不能用於真實會員、付款、訂單或營運庫存。** UI 明確揭露此限制（`index.html:16-18`、`src/app.ts:251`、`src/app.ts:292`、`src/app.ts:301`）；程式的訂單標記為 `simulated: true`（`src/model.ts:172-180`）。正式上線前需另立核准任務，不能把本次掃描或自動測試通過當成上線批准。

## 結果與證據

| ID | 結論 | 狀態 | 證據 | 原型／正式營運影響 |
| --- | --- | --- | --- | --- |
| S-01 | 管理頁 `#admin` 直接路由，展示會員只是本機 boolean，取消與庫存修改未經伺服器授權。 | 已驗證 | `src/app.ts:290-315`、`src/app.ts:390-400`、`src/app.ts:450-452`、`src/app.ts:500-517` | 對已標示的單機假資料原型屬預期設計；正式版為 P0 阻擋，需身分驗證、管理者角色、資源授權與稽核。 |
| S-02 | 商品、價格、配額、購物車與完整訂單均由使用者端 state／localStorage 管理；模型僅提供單次呼叫快照與同一 state 的順序驗證。 | 已驗證 | `src/app.ts:28-63`、`src/app.ts:543-554`；`src/model.ts:157-181` | 原型不代表跨分頁、跨裝置或多人庫存交易已成立。正式版 P0：以伺服器價格與 DB 交易為權威，處理保留、併發、唯一訂單與冪等。 |
| S-03 | 訂單保留姓名、手機、Email、門市等欄位，透過整份 state 寫入 localStorage；有示意資料提示及手動重設，但未見 TTL 或自動刪除。 | 已驗證／影響為推論 | `src/model.ts:32`、`src/model.ts:48-65`、`src/model.ts:175`；`src/app.ts:55-63`、`src/app.ts:251`、`src/app.ts:467-475` | 目前應只輸入假資料；真實資料若誤填將留在該瀏覽器，具共用裝置與同 origin 腳本可見風險。正式版 P0：最小化、保存期限、存取隔離及刪除機制。未讀取任何使用者瀏覽器資料。 |
| S-04 | 常見文字／屬性輸出使用 `esc()`，訊息與驗證錯誤使用 `textContent`，是現有正向控制。 | 已驗證 | `src/app.ts:69-78`、`src/app.ts:82-87`、`src/app.ts:161`、`src/app.ts:209-217`、`src/app.ts:276`、`src/app.ts:288`、`src/app.ts:528-534`、`src/app.ts:555-557` | 尚不能據此宣稱整個應用無 XSS；未進行瀏覽器攻擊或動態漏洞測試。 |
| S-05 | persisted state 只檢查三個欄位為陣列，沒有完整 runtime schema；多個預期為數字的值直接進入 HTML template，`asset()` 只作 HTML escaping 而非 URL allowlist。 | 已驗證；外部可利用性未證實 | `src/app.ts:42-50`、`src/app.ts:77-78`、`src/app.ts:131`、`src/app.ts:161`、`src/app.ts:217`、`src/app.ts:301` | P1 健壯性／未來資料接入風險：損壞或自行變造 localStorage 可能使畫面例外或破壞輸出假設。現在沒有已確認遠端資料注入來源，不列為已證實的遠端 XSS。接正式 API／匯入功能前應加 schema、範圍與 URL／色碼 allowlist、遷移／復原機制。 |
| S-06 | 所有付款狀態為 `simulated_paid`／`cod_pending` 等本機狀態；沒有卡號輸入及支付客戶端。 | 已驗證 | `src/model.ts:31-32`、`src/model.ts:47`、`src/model.ts:174`；`src/app.ts:251`；`tests/artifact.test.mjs:35-43` | 原型降低真金流風險；正式版 P0：可信伺服器金流、回調驗簽、冪等與退款／對帳，不可相信 client 宣稱付款成功。 |
| S-07 | 根套件只有 build/test；lockfile 會固定下載版本與 integrity，但 esbuild 有 install script。 | 已驗證 | `package.json:7-15`；`package-lock.json:514-525`、`package-lock.json:556-560` | 安裝依賴即有執行第三方程式的供應鏈風險。Main 應使用無正式憑證、受控網路與檔案系統的隔離環境。此子任務未執行 npm 安裝或測試，不推論依賴無已知漏洞。 |
| S-08 | CI 僅給 `contents: read`，在 main push／PR／手動觸發時安裝、測試及上傳產物；不含部署步驟。 | 已驗證 | `.github/workflows/ci.yml:1-26` | 權限限制為正向控制；PR 仍執行來源程式，需維持無正式憑證。此 workflow 不是 Pages 發布 pipeline。 |
| S-09 | Actions 使用 `@v4` tag，runner 為 `ubuntu-latest`，未釘完整 SHA；無 timeout 或自動依賴更新設定出現在此 workflow。 | 已驗證（限本檔） | `.github/workflows/ci.yml:11-20` | P2 供應鏈與重現性改善：釘 Actions SHA、設定執行時間上限、建立更新與安全檢查流程。未查核 org 級政策，不宣稱整個帳號無額外控制。 |
| S-10 | 建置只在 `dist/`、`review.html` 產生交付，包含 source maps；這些路徑被忽略。 | 已驗證 | `build.mjs:3-17`、`build.mjs:39-50`；`.gitignore:1-3` | 應在隔離副本產生，無需修改已追蹤檔。source maps 讓已發布程式易讀，但此原碼本來公開；不將其單獨視為秘密外洩。未檢查部署端的 CSP／HTTP headers。 |
| S-11 | 鎖定的 happy-dom `20.14.6` 命中兩項 High advisories；audit 計為 1 個 high vulnerable package。 | 已驗證版本與 audit；可利用性未實測 | `package.json:11-14` 為 `^20.0.10` 範圍；實際 lock 版本見 `package-lock.json:556-560`；`evidence/npm-audit.log`、`evidence/npm-audit.json` | P1 dev／test 供應鏈風險。升級需另核准並驗證相容性；不能宣稱靜態商城執行時可被這兩項漏洞直接遠端利用。詳見下節。 |

## 依賴漏洞實測與本次限制

Main Agent 在隔離副本 `/workspace/work` 執行 `npm audit --json`，2026-11-16 09:35:52–09:35:53 UTC，exit code **1**。已讀取實際 JSON 與執行 metadata：audit 回報 **1 個 High vulnerable package（happy-dom）、2 項 advisory**，不是兩個 vulnerable packages，也不是測試失敗。來源 lock 鎖定 **20.14.6**；`package.json` 的 `^20.0.10` 是版本範圍，不能寫成實際安裝 20.0.10。

| Advisory | 官方受影響／修補版本 | 本案判斷 |
| --- | --- | --- |
| [GHSA-834v-8h66-3h79](https://github.com/advisories/GHSA-834v-8h66-3h79) | High；受影響 `>=17.0.0 <=21.0.3`，修補 `21.0.4` | JavaScript 評估開啟且處理攻擊者控制 HTML／模組時，有 Node host 程式執行風險。現有測試開啟 JS evaluation（`tests/ui.test.mjs:14-29`、`tests/artifact.test.mjs:45-64`），但讀取的是本地已審查 HTML／bundle；本次未提供攻擊輸入或重現漏洞。 |
| [GHSA-c8p4-j97h-3vg8](https://github.com/advisories/GHSA-c8p4-j97h-3vg8) | High；受影響 `<=20.14.6`，修補 `21.0.0` | 處理不可信 HTML 時，iframe／stylesheet 載入可形成 SSRF。測試已設定 `disableCSSFileLoading: true`，但未顯式設定 `disableIframePageLoading`；此為硬化缺口，不表示現有受控 HTML 已造成 SSRF。 |

兩份 GitHub Reviewed advisory 於 2026-11-16 以官方 GitHub Advisory Database 頁面交叉核對，採頁面受影響／修補版本欄位與 audit 回應。`npm audit` 的共同修補建議為 happy-dom **21.0.4**，`isSemVerMajor: true`。只升到 21.0.0 不足以涵蓋本次兩項通報；不能使用未審核的 `npm audit fix --force` 直接改動 lockfile。

這是 Node 測試工具鏈風險：happy-dom 位於 `devDependencies`，只有測試檔匯入，正式靜態產物的 entry points 為 `src/app.ts`／`model.ts`／`catalog.ts`（`package.json:11-15`、`tests/ui.test.mjs:6`、`tests/artifact.test.mjs:6`、`build.mjs:5-13`）。本次未確認外部攻擊者可將不可信 HTML 輸入測試，也未確認預覽站 runtime 使用 happy-dom。現有程式、既有 CI 工作流能執行專案測試，不代表依賴安全檢查通過。

已讀取 Main 的 `evidence/install-hook-review.json`、`npm-install.json`、`npm-test.json`、`npm-test.log`、`npm-coverage.json`、`npm-coverage.log`：先審查 esbuild install hook 後，在無網路、無認證環境且 tracked 檔案逐檔唯讀掛載的 bwrap sandbox 執行 `npm ci --offline --no-audit --no-fund`（完整 hooks，exit 0）與 `npm test`（exit 0，25／25 通過）。這些措施降低本次審核暴露面，**不移除 advisory，也不表示依賴安全檢查通過**。補充 coverage 只量到 `model.js`／`catalog.js`（合計行 96.32%、分支 84.69%、函式 86.36%），不含經 happy-dom eval 的 app 邏輯，不能稱整體應用覆蓋率。Security Agent 未攻擊、未升級依賴，沒有讀取正式憑證。

## GitHub Pages 與部署證據邊界

- **已驗證的原碼設定**：這份 SHA 只有 `.github/workflows/ci.yml`，內容為測試與 artifact 上傳；沒有 Pages deploy step。`README.md:27-35` 描述建置後將 `dist/` 內容放在 `gh-pages` 根目錄，再由 GitHub Pages 從該分支部署；`README.md:31` 明確說明 main 變更不會自行同步。
- **本次已核對歷史 run metadata**：已讀取 Main Agent 於 2026-11-16 09:32:30 UTC 取得的 [Actions API](https://api.github.com/repos/xk2022/codex-xk-apparel-store/actions/runs?per_page=10) 最小化證據 `evidence/github-actions.json`。固定 main SHA 的 [run 43373108942](https://github.com/xk2022/codex-xk-apparel-store/actions/runs/43373108942) 為 `Prototype checks`、`completed/success`，更新時間 2026-11-13 05:36:39Z。另有 [Pages run 43359061053](https://github.com/xk2022/codex-xk-apparel-store/actions/runs/43359061053)，`gh-pages@302f9580fa6b74f153964d8834274510f5f638cc`，事件 `dynamic`，`completed/success`，更新時間 2026-11-13 03:27:40Z。這證明有成功的歷史 Pages 部署，不能因 main CI 無部署 step 就宣稱「尚未部署」。
- **目前成品分支與歷史 job**：已讀取 `evidence/github-pages.json`（2026-11-16 09:37:00 UTC），[gh-pages branch API](https://api.github.com/repos/xk2022/codex-xk-apparel-store/branches/gh-pages) 的 ref 仍為 `302f9580fa6b74f153964d8834274510f5f638cc`；[歷史 Pages jobs API](https://api.github.com/repos/xk2022/codex-xk-apparel-store/actions/runs/43359061053/jobs) 的 `build`、`report-build-status`、`deploy` 及各已回傳步驟均 `completed/success`。它們證明分支與歷史執行紀錄，沒有證明目前 live 站資源與最新 main 產物逐檔一致。
- **文件聲明的其餘邊界**：`docs/ACCEPTANCE.md:53-64`、`docs/HANDOFF.md:35-43` 的 17 個 HTTP 200／內容一致結果屬 2026-11-13 紀錄，本次未重新執行；不能當成 2026-11-16 即時站況。
- **本次未執行／無法查核**：未開正式預覽站、未做 HTTP／資源內容比對、未讀 Pages 管理設定、未觸發 workflow、未推送 `gh-pages`。Main 回報 deployments endpoint 為 connector `INVALID_ARGUMENT`，屬工具能力限制，不是沒有部署資源的證據。其他 branch／job API 結果以整合報告為準。
- **風險推論**：main 與成品分支分離，需要保留來源 SHA、產物 SHA、測試與部署 run 的對應，避免測過的原碼與發布內容漂移。改善建議需另行核准，不在本次掃描修改 pipeline。

## 命令、檢查與限制

工作目錄均為唯讀來源副本；下列檢查沒有執行專案程式。

| 實際檢查 | 結果／exit code | 限制 |
| --- | --- | --- |
| `git rev-parse HEAD` | `1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422`，0 | 固定本次來源。 |
| `nl -ba`／定向閱讀 app、model、catalog、build、HTML、package、lockfile、CI 與交接／驗收文件 | 完成，0 | 靜態資料流與設定分析；不證明執行時不存在缺陷。 |
| `rg` 搜尋網路客戶端、`eval`、HTML sinks、storage 與事件處理位置 | 完成，0 | `eval` 出現在 happy-dom 本機測試，用於執行受控 bundle；本次未執行這些測試，不代表能安全處理不可信 HTML。 |
| Python 以常見 GitHub／OpenAI token、AWS access key ID、私鑰標頭樣式掃描 21 個 tracked 文字檔 | 0 命中，0 | 只回報類別、路徑與行號，未輸出秘密值；不是完整 secret detector、歷史掃描或機密資料保證。未讀 `.git` 歷史內文或認證檔。 |
| `git status --porcelain` | 空輸出，0 | 本子任務讀取時來源副本無變更；最終前後 hash 由 Main 整體核對。 |
| 讀取 Main 取得的 `evidence/github-actions.json` | JSON 可讀，0 | 僅核對歷史 run metadata；不是本次觸發測試／部署，亦非即時網站健康檢查。 |
| 讀取 Main 的 `evidence/npm-audit.log`／`npm-audit.json` | audit exit 1；1 個 High package、2 advisories | 本子任務未執行 npm；核對實際 audit 證據與來源 lock。Main 的 audit 執行環境採 allowlist、停用 user/global npm config、tracked 唯讀掛載，audit 階段允許網路。 |
| 讀取 Main 的 `install-hook-review.json`、`npm-install.json`、`npm-test.json` 與 `npm-test.log` | 完整 hooks 的離線 `npm ci --offline --no-audit --no-fund` exit 0；`npm test` exit 0，25／25 通過 | 本子任務未執行 npm；只核對 Main 生成的實際證據。測試通過不會消除 audit 的 High advisories。 |
| 讀取 Main 的 `npm-coverage.json`／`npm-coverage.log` | 補充 coverage exit 0 | 量測 model／catalog 合計 96.32% 行、84.69% 分支、86.36% 函式，不涵蓋 eval app，不視為全專案覆蓋率。 |
| 讀取 Main 的 `github-pages.json` | JSON 可讀，0 | 目前 gh-pages ref 與歷史 build／report／deploy job steps 成功，不是 live 站檢查。 |

沒有測試正式支付、管理帳號、真實資料庫、訂單、物流、憑證、正式站流量、headers 或主動攻擊。Security Agent 沒有自行量測覆蓋率；Main 的部分模組量測已如上限定範圍。

## 建議優先序與停止條件

1. **P0，任何正式商用前**：核准產品與商家政策後，另立後端／DB／身分與管理授權設計；價格、庫存、下單與付款以伺服器為權威，加入交易、唯一約束、冪等與稽核。依據 S-01、S-02、S-06。
2. **P0，任何真實個資前**：先完成收集目的、最小化、保存／刪除、隔離與安全設計，不沿用整份 localStorage state 保存真實會員與訂單。依據 S-03；現階段只保留示意資料。
3. **P1，下一個開發／CI 安全工作包**：審查 happy-dom 21.0.4（或涵蓋兩項通報的較新版本）相容性與變更，再核准升級並跑完整測試／audit；現階段禁止此工具鏈處理不可信 HTML／外部模組，維持無網路、無憑證隔離執行。依據 S-11。這項建議尚未授權實作。
4. **P1，擴大 demo 資料來源前**：加入 persisted state schema 與版本遷移，防禦異常型別及缺失欄位；各 sink 採文字輸出或符合上下文的 allowlist，並補損壞資料與匯入邊界測試。依據 S-04、S-05。
5. **P2，工程維護**：釘 Actions SHA、review install hook／依賴 advisories、設定 CI timeout、保留原碼與成品對應。依據 S-07 至 S-10。升版與 pipeline 修改均屬候選工作，本次未實作。
6. **停止條件**：操作若要求正式憑證、正式資料、寫入受管理專案、部署、權限變更或付費資源，先回報 Main Agent，取得使用者對具體操作的明確確認。

## Main Agent 驗收

- 交付物：`projects/codex-xk-apparel-store/reports/HQ-001/security-report.md`。
- 需整合：最終 tracked-file hash 與未變更證明。Main 的 npm／隔離執行、有限 coverage、Actions、gh-pages 與歷史 Pages jobs 證據已核讀並納入上述安全報告。
- Main Agent 複核結果：待複核。本子任務不修改專案登錄、任務狀態或既有 work-log。
