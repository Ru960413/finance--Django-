# Bankist 虛擬網路銀行

- [Bankist 虛擬網路銀行](#bankist-虛擬網路銀行)
  - [我的網站](#我的網站)
    - [所使用的技術](#所使用的技術)
    - [專案介紹](#專案介紹)
    - [動機及 project 設計](#動機及project設計)
    - [專案重點](#專案重點)

## 我的網站

<https://finance-django-production.up.railway.app/>

![Welcome Page](pics/welcomePage.png "Welcome Page")

### 所使用的技術

    1. HTML
    2. CSS
    3. JavaScript
    4. Python
    5. Django
    6. ExchangeRate API
    7. Railway(Deployment)

### 專案介紹

這是一個由 Python、Django 以及 JavaScript 為邏輯所寫成虛擬銀行網站，不僅有提款、領錢、貸款的功能，也有外幣買賣、查詢歷史買賣、查詢現價的功能

### 動機及 project 設計

這個專案的起源是在上 Udemey 平台上的 Jonas Schmedtmann 所開設的 JavaScript 課程，當初在練習 JavaScript Array 以及 DOM manipulation 時，我便想把這個練習變得更加全面，因而就有了這個 project 的產生。

在 project 的設計上，主要有三個面向：一般的 banking 功能、外幣的買賣功能及使用者驗證的功能。banking 前端是老師在上課時為我們設計的，我則寫了能支援其功能的 Django 後端，而外幣兌換與使用者介面的前端及後端皆由我設計及編寫，外幣的資料來源來自 ExchangeRate API。

### 專案重點

1. 使用者頁面

   ![使用者登入](pics/user_login.png "使用者登入")

   ![使用者註冊](pics/user_register.png "使用者註冊")

   ![個人資料頁面](pics/profile_page.png "個人資料頁面")

2. 銀行頁面

   ![主頁](pics/banking_page.png "主頁")

   ![成功（以提款舉例）](pics/success.png "成功（以提款舉例）")

   ![失敗（以提款舉例）](pics/fail.png "失敗（以提款舉例）")

3. 外幣頁面

   ![外幣購買](pics/currency_page.png "外幣購買")

   ![成功（以買入舉例）](pics/success_buy.png "成功（以買入舉例）")

   ![Error handling舉例](pics/error_handling.png "Error handling")
