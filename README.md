# 🎁 Bale Gift Auto-Opener

Automatically detects gift messages on Bale and attempts to open them.

## ✨ Features

- Automatic gift detection and opening attempts
- Windows executable available through GitHub Releases
- Python source support for Windows and Linux
- Persistent login session
- Suitable for continuous operation on a VPS

## 🪟 Windows

### Option 1: Windows Executable

1. Visit the [Releases](https://github.com/m4ni-z/gift-opener/releases) page.
2. Download the latest Windows ZIP file.
3. Extract the downloaded archive.
4. Right-click the executable and select **Run as administrator**.
5. Enter your Bale phone number directly in the application.
6. Enter the verification code when prompted.

After login, the application automatically starts scanning messages. On subsequent launches, the saved session can be reused if it remains valid.

### Option 2: Run from Source

Install [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads/).

Open Command Prompt or PowerShell **as administrator**, then run:

```powershell
git clone https://github.com/m4ni-z/gift-opener.git
cd gift-opener
python -m pip install aiobale-py
python main.py
```

## 🐧 Linux (Ubuntu)

### 1. Install Dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip git
```

### 2. Clone the Repository

```bash
git clone https://github.com/m4ni-z/gift-opener.git
cd gift-opener
```

### 3. Install and Run

```bash
python3 -m pip install aiobale-py
python3 main.py
```

## 🔐 Login and Session

On the first launch, enter your Bale phone number directly in the application, then enter the verification code when prompted.

The application saves a login session for future launches. Keep the session file in its expected location and do not share it.

## ⏱️ 24/7 Operation

The application must remain running and connected to the internet to continue scanning messages.

To run it continuously on a personal computer, keep the computer powered on and prevent it from sleeping. For more reliable 24/7 availability, consider running the application on a VPS.

## 📄 License

See the repository for license information.

---

# 🎁 بازکنندهٔ خودکار هدیه‌های بله

پیام‌های حاوی هدیه در بله را به‌صورت خودکار شناسایی می‌کند و تلاش می‌کند آن‌ها را باز کند.

## ✨ ویژگی‌ها

- شناسایی خودکار هدیه‌ها و تلاش برای باز کردن آن‌ها
- ارائهٔ فایل اجرایی ویندوز در بخش انتشارهای گیت‌هاب (GitHub Releases)
- پشتیبانی از اجرای کد پایتون در ویندوز و لینوکس
- ذخیرهٔ نشست ورود برای اجراهای بعدی
- مناسب برای اجرای مداوم روی سرور مجازی (VPS)

## 🪟 ویندوز

### روش اول: فایل اجرایی ویندوز

1. به صفحهٔ [انتشارها (Releases)](https://github.com/m4ni-z/gift-opener/releases) بروید.
2. آخرین فایل ZIP مخصوص ویندوز را دانلود کنید.
3. فایل دانلودشده را از حالت فشرده خارج کنید.
4. روی فایل اجرایی راست‌کلیک کنید و گزینهٔ **Run as administrator** را انتخاب کنید.
5. شماره تلفن بلهٔ خود را مستقیماً در برنامه وارد کنید.
6. وقتی برنامه درخواست کرد، کد تأیید را وارد کنید.

پس از ورود، برنامه به‌صورت خودکار اسکن پیام‌ها را آغاز می‌کند. در اجراهای بعدی، اگر نشست ذخیره‌شده همچنان معتبر باشد، برنامه می‌تواند از آن استفاده کند.

### روش دوم: اجرا از کد منبع پایتون

ابتدا [پایتون](https://www.python.org/downloads/) و [گیت](https://git-scm.com/downloads/) را نصب کنید.

خط فرمان (Command Prompt) یا پاورشل (PowerShell) را **با دسترسی مدیر سیستم (Administrator)** باز کنید و دستورهای زیر را اجرا کنید:

```powershell
git clone https://github.com/m4ni-z/gift-opener.git
cd gift-opener
python -m pip install aiobale-py
python main.py
```

## 🐧 لینوکس (اوبونتو)

### ۱. نصب پیش‌نیازها

```bash
sudo apt update
sudo apt install python3 python3-pip git
```

### ۲. کلون کردن مخزن

```bash
git clone https://github.com/m4ni-z/gift-opener.git
cd gift-opener
```

### ۳. نصب و اجرا

```bash
python3 -m pip install aiobale-py
python3 main.py
```

## 🔐 ورود و نشست کاربری

در اولین اجرا، شماره تلفن بلهٔ خود را مستقیماً در برنامه وارد کنید؛ سپس، هنگامی که برنامه درخواست کرد، کد تأیید را وارد کنید.

برنامه نشست ورود را برای اجراهای بعدی ذخیره می‌کند. فایل نشست را در محل مورد انتظار برنامه نگه دارید و آن را با دیگران به اشتراک نگذارید.

## ⏱️ اجرای ۲۴ ساعته

برای ادامهٔ اسکن پیام‌ها، برنامه باید در حال اجرا باشد و به اینترنت متصل بماند.

برای اجرای مداوم روی رایانهٔ شخصی، رایانه را روشن نگه دارید و از رفتن آن به حالت خواب جلوگیری کنید. برای دسترس‌پذیری مطمئن‌تر در تمام ساعات شبانه‌روز، استفاده از یک سرور مجازی (VPS) را در نظر بگیرید.

