# HQ-001-R — Research Agent 工作回報

## 任務與範圍

- Project：`codex-xk-apparel-store`；Task／子任務：`HQ-001`／`HQ-001-R`。
- 角色：Research Agent；已讀取並依 HQ `.codex/agents/research.toml` 的指令執行，並遵守 HQ 與目標專案的 `AGENTS.md`。
- 查核日期：2026-11-16（UTC）。來源文件日期多為 2026-11-13；歷史文件結果不視為本次重跑證據。
- 共同來源：`xk2022/codex-xk-apparel-store@1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422`，分支 `main`。
- 唯讀 checkout：`/workspace/scratch/HQ-001-1qnZaIVi/source`。
- 範圍：前端功能、流程、需求與文件落差、商業化缺口及候選優先序；不執行安裝、測試、瀏覽器、部署或正式服務請求。
- 唯一可寫路徑：本報告；未修改任何已追蹤檔案，未建立 Commit，未讀取正式憑證。
- 子任務結果：已交付，等待 Main Agent 驗收；本報告不自行變更 HQ-001 狀態。

## 證據索引

下列來源全部固定在共同 SHA；`path:line` 範圍可與本機 `nl -ba` 輸出逐項核對。

| ID | 來源與用途 |
| --- | --- |
| R1 | [docs/REQUIREMENTS.md:6-34](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/docs/REQUIREMENTS.md#L6-L34)：確認需求與原型邊界。 |
| R2 | [docs/REQUIREMENTS.md:44-82](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/docs/REQUIREMENTS.md#L44-L82)：示意政策、待定事項與過時部署描述。 |
| R3 | [src/app.ts:102-164](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/src/app.ts#L102-L164)：首頁、分類、搜尋、排序及出貨訊息。 |
| R4 | [src/app.ts:183-259](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/src/app.ts#L183-L259)：商品詳情、購物袋及訪客結帳。 |
| R5 | [src/app.ts:280-315](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/src/app.ts#L280-L315)：訂單確認、展示會員、示意後台與 hash 路由。 |
| R6 | [src/app.ts:390-475](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/src/app.ts#L390-L475)：取消、購物袋、會員切換與資料重設；[src/app.ts:500-590](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/src/app.ts#L500-L590)：配額更新、結帳送出與焦點控制。 |
| R7 | [src/catalog.ts:1-116](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/src/catalog.ts#L1-L116)：商品、SKU、單張示意圖、價格與有限配額。 |
| R8 | [src/model.ts:5-65](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/src/model.ts#L5-L65) 與 [src/model.ts:146-195](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/src/model.ts#L146-L195)：政策常數、資料型別、結帳驗證、模擬下單及取消。 |
| R9 | [src/app.ts:28-64](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/src/app.ts#L28-L64)：完整 DemoState 的 localStorage 載入與保存。 |
| R10 | [README.md:25-61](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/README.md#L25-L61) 與 [docs/HANDOFF.md:24-50](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/docs/HANDOFF.md#L24-L50)：維護與歷史交付紀錄、瀏覽器驗收限制。 |
| R11 | [docs/ACCEPTANCE.md:9-47](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/docs/ACCEPTANCE.md#L9-L47) 與 [docs/ACCEPTANCE.md:49-64](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/docs/ACCEPTANCE.md#L49-L64)：歷史測試、Pages 證據連結及未驗收項目。 |
| R12 | [docs/DATA_MODEL.md:3-17](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/docs/DATA_MODEL.md#L3-L17) 與 [docs/DATA_MODEL.md:38-99](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/docs/DATA_MODEL.md#L38-L99)：實際本機模型與尚未核准的正式資料模型候選。 |
| R13 | [docs/ASSET_SOURCES.md:3-29](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/docs/ASSET_SOURCES.md#L3-L29)：照片示意性、來源及正式商品素材替換需求。 |
| R14 | [index.html:14-25](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/index.html#L14-L25)：明示假商品／模擬交易、無 JS 提示；[.github/workflows/ci.yml:1-26](https://github.com/xk2022/codex-xk-apparel-store/blob/1d4f2acad5475f4d2b8c4c16a11377fe2ffe4422/.github/workflows/ci.yml#L1-L26)：建置測試及 artifact 工作流程。 |

## 已驗證的前端流程（靜態來源）

此處的「已驗證」表示確認程式與文件中的實作，不表示本子任務已進行真實瀏覽器驗收。

| 流程 | 實際實作與範圍 | 證據 |
| --- | --- | --- |
| 選品 | 首頁／商品列表、現貨／預購篩選、分類、名稱／分類包含式搜尋、價格升降排序。8 款商品寫在靜態 catalog。 | R3 `app.ts:133-164`；R7 `catalog.ts:26-116`。 |
| 規格 | 可選顏色、尺寸與數量；可購配額／預購備貨日數明示。首次開啟會預選首個有貨 SKU，售罄時使用第一個 SKU 並停用加入按鈕。 | R4 `app.ts:183-217`。 |
| 購物袋 | 顯示 SKU、增減／移除、運費、總額、混單等待資訊；數量異動後更新本機儲存與結帳摘要。 | R4 `app.ts:224-230`；R6 `app.ts:372-382`；R8 `model.ts:5-8`。 |
| 訪客結帳 | 不必登入；姓名、手機、Email、示意門市、card／COD；有填示意資料入口，不收卡號，表單與模型共同驗證。 | R4 `app.ts:232-259`；R6 `app.ts:439-447,519-554`；R8 `model.ts:146-179`。 |
| 下單／查單 | 模擬訂單保存商品與金額快照、更新本機配額、清空購物袋，hash 導向確認頁；只在當前瀏覽器訂單陣列內查找。 | R5 `app.ts:280-288`；R6 `app.ts:541-554`；R8 `model.ts:157-181`。 |
| 展示會員 | member 是布林值，可直接切換；無帳號、密碼或真正認證，展示目前瀏覽器所有訂單。 | R5 `app.ts:290-294`；R6 `app.ts:450-459`；R9 `app.ts:28-50`。 |
| 店主示意後台 | `#admin` 直接進入，顯示訂單／配額；取消 preparing 訂單回補一次、修改 0–99999 配額、重設本機假資料。不是正式權限保護。 | R5 `app.ts:296-315`；R6 `app.ts:390-400,467-475,503-517`；R8 `model.ts:184-195`。 |
| 可及性基礎 | 有 skip link、live status、dialog 標記與 Escape／Tab 焦點控制；具體瀏覽器、觸控、螢幕閱讀器表現未在本子任務量測。 | R14 `index.html:15-24`；R6 `app.ts:562-587`；R11 `ACCEPTANCE.md:12,22,41`。 |

## 已確認規則與示意假設

- **已確認規則**：台灣市場、自建網站、款式×顏色×尺寸 SKU、現貨／預購混單、等預購到齊整單寄出且一次運費、允許訪客；正式會員功能是保留方向，並非目前完成的認證功能。證據：R1 `REQUIREMENTS.md:10-18`，R8 `model.ts:8`，R4 `app.ts:251`。
- **待店家定案的示意假設**：NT$65 運費、NT$2,000 免運、品牌名稱、商品照片／材質／尺寸、SKU 配額及備貨日數。它們雖已硬編碼，不能升格為正式營運承諾。證據：R2 `REQUIREMENTS.md:44-57,68-74`，R7 `catalog.ts:28-113`，R8 `model.ts:5-7`，R13。
- **候選而非已建成架構**：DATA_MODEL 中的 DB、庫存保留、payments／shipments／invoices、outbox／idempotency 表格是待審草案；實際執行端仍只有前端與 localStorage。證據：R12 `DATA_MODEL.md:3-17,38-58,85-99`，R9。

## 需求與交接落差

| ID／程度 | 已驗證落差 | 影響與建議 | 證據 |
| --- | --- | --- | --- |
| R-GAP-01／中 | 原型需求列「多圖」，但每個 catalog `images` 均僅一張，商品詳情只呈現 `p.image`；未見利用 `images` 的 gallery／縮圖切換。 | 不能把「多圖詳情」列為完整實作。先由產品確認單圖是否接受；若保留多圖需求，再另授權實作與驗收。顏色不換圖已有明示，與此缺口分開看待。 | R1 `REQUIREMENTS.md:27`；R7 `catalog.ts:19,29,41,53,65,75,87,97,108`；R4 `app.ts:208-217`。 |
| R-GAP-02／低 | REQUIREMENTS 仍寫「公開同步進行中／預定網址尚待啟用」，README、ACCEPTANCE、HANDOFF 則記載已發布與歷史部署 run。 | 交接文件狀態不一致。後續核對實際遠端證據後，將需求文件更新為歷史計畫或當前狀態；本子任務不據文件自行宣稱 live Pages 現在正常。 | R2 `REQUIREMENTS.md:80-82`；R10 `README.md:27-35`、`HANDOFF.md:34-49`；R11 `ACCEPTANCE.md:59-64`。 |
| R-GAP-03／後續驗收 | 文件對原碼交付已完成、客戶風格與真實瀏覽器驗收未完成有清楚界線；不能將歷史 25/25 或 Pages HTTP 200 當成客戶驗收完成。 | 先以手機／桌面及真實瀏覽器驗證畫面、觸控、鍵盤／輔助工具和混單流程，再定客戶可接受性；本次測試結果由 Main／QA 另附實測證據。 | R10 `README.md:29,59`、`HANDOFF.md:42-49`；R11 `ACCEPTANCE.md:38-47,55-64`。 |

## 商業化缺口與候選優先順序

以下為依程式與需求推導的建議，**不是已授權開發，也不是原型邊界內的缺陷清單**。正式 DB、金流等原本就明確排除於原型交付（R1 `REQUIREMENTS.md:34`）。

| 優先序 | 建議工作／原因 | 相依與可驗收條件 | 依據 |
| --- | --- | --- | --- |
| P0：維持展示邊界 | 繼續阻止將本原型當營運商城；保留示意標籤、無真實個資／金流／帳號，避免店主誤用本機後台。 | 決策：是否只維持 demo 或另立正式版工作包；不得為商業化候選直接開工。 | R14；R5 `app.ts:292,301`；R9；R10 `README.md:49`。 |
| P1：先完成產品驗收 | 以真實瀏覽器與客戶確認手機／桌面風格、混單、訪客結帳、焦點與錯誤訊息；處理多圖需求及過時交接描述。 | 有明確情境、裝置、結果與接受／待修清單；保持已確認混單一次運費規則。 | R-GAP-01～03；R1；R11 `ACCEPTANCE.md:9-22`。 |
| P1：定案營運資料 | 品牌、實拍、SKU、價格、供貨上限、交期／延遲、取消退貨退款、運費、未取、員工權限、保存期限、責任與預算。 | 由店家確認政策及素材權利；不把假資料轉成正式承諾。 | R2 `REQUIREMENTS.md:68-74`；R13；R12 `DATA_MODEL.md:95-99`。 |
| P2：可信交易與權限基礎 | 正式後端、資料庫、商品管理、訪客安全查單／會員與管理員權限、伺服器重算價格、庫存保留與交易，避免裝置間資料分裂及可自行改價配額。 | 先核准架構與資料模型；跨使用者隔離、最後一件併發、冪等、備份還原及遷移測試通過。 | R9；R5 `app.ts:296-315`；R12 `DATA_MODEL.md:38-85,95-99`。 |
| P3：實際商家介接 | 金流、超商門市／物流與 COD、退款、發票、通知；需各自狀態、回調驗簽、冪等、查詢／對帳補償。 | 商家資格與服務帳戶核准；僅先在 sandbox 以測試憑證驗證，正式部署另經使用者確認。 | R1 `REQUIREMENTS.md:17-18,34`；R12 `DATA_MODEL.md:50-56,87-93`；R11 `ACCEPTANCE.md:45-47`。 |
| P4：營運就緒 | 監控、稽核、支援流程、依賴管理、成品與原碼追蹤、受控發布及回滾；不把靜態預覽部署成功當正式 SLA。 | 以正式需求定指標；CI、資料復原、安全及營運驗收完成才評估上線。 | R14 `ci.yml:1-26` 只見測試／artifact；R10 `README.md:31` 提醒 main 不會自行同步成品；R12 `DATA_MODEL.md:97-99`。 |

## 命令、變更與限制

| 實際動作 | 結果／Exit code | 範圍與限制 |
| --- | --- | --- |
| 以 `cat`／`nl -ba`／`sed` 讀取兩層 AGENTS、角色設定、模板、README、需求／驗收／交接／資料模型／素材文件與 app/catalog/model/index/package/CI。 | 批次讀取命令 exit 0；較長輸出截斷的區段已定向重讀。 | 靜態來源查核，無腳本執行、無憑證讀取。 |
| `rg -n` 搜尋 images/gallery、會員／後台、storage、遠端 API 與測試名稱。 | exit 0；結果作為上述指定檔案行號的輔助，不單憑搜尋無結果認定絕對安全。 | 沒有查外部私人資料，無需外部技術行為假設。 |
| `git diff --exit-code`、`git diff --cached --exit-code`、`git rev-parse HEAD`。 | 均 exit 0，HEAD 為本報告共同 SHA。 | 本子任務來源已追蹤內容無差異；整體測試前後的最終雜湊由 Main Agent 驗收。 |
| `npm ci`、`npm test`、覆蓋率與瀏覽器驗收。 | **本 Research 子任務未執行**。 | 執行與結果由 QA／Main Agent 提供，不引用歷史 25/25 作本次結果。 |

- 交付僅本報告，無受管理專案修改、Commit、部署或 Issue／PR 更新。
- 未自行關閉既有產品 Issue、未讀取其私人管理中心，未建立新的產品任務或日曆事件；本次是唯讀掃描與本地報告交接。
- 下一步：由 Main Agent 整合 QA、Architect、Security 的實際證據，確認 roadmap 依賴，回報 HQ 並等待新授權。
- Main Agent 驗收：待審核；本報告可供 `scan-report.md` 與 `roadmap.md` 引用。
