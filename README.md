# Assistant - Rin (Testing, In Progress...) ᓚᘏᗢ

<!-- Vietnamese -->
<details>
  <summary>🇻🇳 Tiếng Việt</summary>

## Giới thiệu

Assistant - Rin là một trợ lý ảo mạnh mẽ được xây dựng bằng Python, sử dụng mô hình ngôn ngữ lớn (LLM) Gemini của Google để thực hiện nhiều tác vụ khác nhau.  Rin có khả năng thực thi mã Python, thực thi lệnh hệ thống, xử lý file, và tương tác với người dùng qua giao diện dòng lệnh.  Điểm đặc biệt của Rin là khả năng tự đánh giá và cải thiện kết quả thực thi thông qua việc sử dụng một mô hình Gemini thứ hai để kiểm tra chéo.

## Tính năng

*   **Thực thi mã Python:**  Cho phép người dùng yêu cầu Rin thực thi các đoạn mã Python. Rin sẽ tạo mã, thực thi, và trả về kết quả, bao gồm cả đầu ra (stdout), lỗi (stderr), và thời gian thực thi.
*   **Thực thi lệnh hệ thống:**  Cho phép người dùng yêu cầu Rin thực thi các lệnh hệ thống (PowerShell trên Windows).  Rin sẽ sử dụng Gemini để tạo lệnh, thực thi, và trả về kết quả, bao gồm cả đầu ra, lỗi, mã trả về, và đánh giá của Gemini thứ hai.
*   **Xử lý file nâng cao:**  Cung cấp các chức năng xử lý file như đọc, ghi, chỉnh sửa (thay thế, xóa, thêm nội dung), tạo code Python, sửa lỗi code Python, và nâng cấp code Python.  Rin cũng hỗ trợ nhiều định dạng file khác nhau (text, JSON, CSV, DOCX, XLSX).
*   **Tương tác với Gemini:**  Giao tiếp trực tiếp với mô hình Gemini để trả lời các câu hỏi chung, không liên quan đến plugin.
*   **Ghi nhớ:**  Lưu trữ lịch sử các tương tác và kết quả thực thi vào các file memory, cho phép sử dụng lại thông tin trong các phiên làm việc sau.
*   **Giám sát file:** (Tính năng thử nghiệm) Có khả năng giám sát sự thay đổi của file và thông báo cho người dùng.
*   **Giao diện dòng lệnh:**  Tương tác với người dùng thông qua giao diện dòng lệnh, với màu sắc và hiệu ứng để tăng trải nghiệm.

## Cài đặt

1.  **Yêu cầu:**
    *   Python 3.7 trở lên.
    *   Các thư viện (xem file `requirements.txt` để biết chi tiết): `google-generativeai`, `python-magic`, `psutil`, `watchdog`, `pygments`, `docx`, `openpyxl`, `wmi`, `ctypes`, `rich`.

2.  **Các bước cài đặt:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git # Thay bằng link repo của bạn
    cd your-repository-name
    python -m venv moitruongao
    moitruongao\Scripts\activate  # Hoặc  source moitruongao/bin/activate  trên Linux/macOS
    pip install -r requirements.txt
    ```
    * Thay `your-username` và `your-repository-name` bằng liên kết repo github của bạn.
    * Chạy file `run.bat` để tạo và kích hoạt môi trường ảo `moitruongao`, cài đặt các thư viện cần thiết và chạy chương trình. Hoặc chạy các lệnh trên theo cách thủ công

3.  **Chạy ứng dụng:**
    *  Chạy file `run.bat`
    ```
    run.bat
    ```
    *  Hoặc chạy file `rin.py`
     ```
      python rin.py
      ```

4. **Cấu hình:**
   *   Cấu hình API key, tên model, và các tham số khác trong file `utils/cau_hinh.py`.
        *   Thay `API_KEY` bằng API key Gemini của bạn.

## Hướng dẫn sử dụng

*   **Tương tác cơ bản:** Nhập câu hỏi hoặc yêu cầu trực tiếp vào giao diện dòng lệnh.
*   **Thực thi mã Python:**  Bắt đầu câu hỏi bằng ký tự `$` (ví dụ: `$ print("Hello")`).  Rin sẽ hiểu đây là yêu cầu thực thi mã Python.
    *   **Ví dụ:** `$ tính tổng của 2 số 5 và 7`
*   **Thực thi lệnh hệ thống:** Bắt đầu câu hỏi bằng ký tự `@`. Rin sẽ hiểu đây là yêu cầu thực thi lệnh hệ thống.
    *   **Ví dụ:** `@ danh sách các tiến trình đang chạy`
*   **Xử lý file:** Bắt đầu câu hỏi bằng ký tự `#`, theo sau là đường dẫn file và yêu cầu (ví dụ: `# "C:\test.txt" đọc file`). Rin hỗ trợ các hành động sau:
    *   `đọc file`: Đọc nội dung file.  **Ví dụ:** `# "C:\my_folder\test.txt" đọc file`
    *   `chỉnh sửa file`: Chỉnh sửa nội dung file (thay thế, xóa, thêm).   **Ví dụ:** `# "C:\my_folder\test.txt" chỉnh sửa file, thay thế "xin chào" bằng "hello"`
    *   `ghi file`: Ghi nội dung vào file.  **Ví dụ:** `# "C:\my_folder\test.txt" ghi file với nội dung "Đây là nội dung mới"`
    *   `tạo code`: Tạo code Python theo yêu cầu.  **Ví dụ:** `# "C:\my_folder\my_script.py" viết cho tôi một mã python có chức năng tính giai thừa`
    *   `fix_code`: Sửa lỗi code Python.  **Ví dụ:** `# "C:\my_folder\error_script.py" fix code`
    *    `nâng cấp`: Nâng cấp code Python. **Ví dụ:** `#"C:\my_folder\old_script.py" nâng cấp code`
*   **Load memory:**  Bắt đầu câu hỏi bằng ký tự `!` theo sau là tên file memory (ví dụ: `! memory_file.json`).  Thao tác này sẽ load thông tin từ file memory đã lưu trước đó.
    * **Ví dụ:** `!my_previous_session.json`
*  **Thoát:** Gõ `0`.
*  **Ngắt tiến trình:** Gõ `2`.

## Cấu trúc thư mục
```
Assistant/
├── .git/ (Không liệt kê)
├── .gitignore
├── bieutuong/ (Không liệt kê)
├── cac_plugin/
│   ├── thuc_thi_lenh_he_thong.py
│   ├── thuc_thi_python.py
│   ├── xu_ly_file_plugin.py
│   ├── __init__.py
│   ├── __pycache__/ (Không liệt kê)
├── chat.py
├── core/
│   ├── chat.py
│   ├── __init__.py
│   ├── __pycache__/ (Không liệt kê)
├── memory/ (Không liệt kê)
├── rin.py
├── run.bat
├── utils/
│   ├── animation/
│   │   ├── hieu_ung.py
│   │   ├── __init__.py
│   │   ├── __pycache__/ (Không liệt kê)
│   ├── cau_hinh.py
│   ├── nhat_ky.py
│   ├── __init__.py
│   ├── __pycache__/ (Không liệt kê)
├── __init__.py
├── __pycache__/ (Không liệt kê)
```

</details>

<!-- English -->
<details>
  <summary>🇬🇧 English</summary>

## Introduction

Assistant - Rin is a powerful virtual assistant built with Python, using Google's Gemini large language model (LLM) to perform various tasks. Rin is capable of executing Python code, executing system commands, processing files, and interacting with users via the command-line interface.  A special feature of Rin is its ability to self-evaluate and improve execution results by using a second Gemini model for cross-checking.

## Features

*   **Execute Python code:** Allows users to request Rin to execute Python code snippets. Rin will generate the code, execute it, and return the results, including output (stdout), errors (stderr), and execution time.
*   **Execute system commands:** Allows users to request Rin to execute system commands (PowerShell on Windows).  Rin will use Gemini to generate the command, execute it, and return the results, including output, errors, return code, and evaluation by the second Gemini model.
*   **Advanced file processing:** Provides file processing functions such as reading, writing, editing (replacing, deleting, adding content), creating Python code, fixing Python code errors, and upgrading Python code.  Rin also supports various file formats (text, JSON, CSV, DOCX, XLSX).
*   **Interact with Gemini:** Communicate directly with the Gemini model to answer general questions, not related to plugins.
*   **Memory:** Stores interaction history and execution results in memory files, allowing reuse of information in subsequent working sessions.
*   **File monitoring:** (Experimental feature) Capable of monitoring file changes and notifying the user.
*   **Command-line interface:** Interacts with the user through the command-line interface, with colors and effects to enhance the experience.

## Installation

1.  **Requirements:**
    *   Python 3.7 or higher.
    *   Libraries (see `requirements.txt` file for details):  `google-generativeai`, `python-magic`, `psutil`, `watchdog`, `pygments`, `docx`, `openpyxl`, `wmi`, `ctypes`, `rich`.

2.  **Installation steps:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git # Replace with your repo link
    cd your-repository-name
    python -m venv virtual_environment_name
    virtual_environment_name\Scripts\activate  # Or  source virtual_environment_name/bin/activate  on Linux/macOS
    pip install -r requirements.txt
    ```
     * Replace `your-username` and `your-repository-name` with your github repo link.
    *  Run the `run.bat` file to create and activate the `moitruongao` virtual environment, install the necessary libraries and run the program. Or run the above commands manually.

3.  **Run the application:**
    *  Run `run.bat` file
    ```
    run.bat
    ```
    *  Or run `rin.py` file.
    ```
    python rin.py
    ```
4.  **Configuration:**
   *   Configure the API key, model name, and other parameters in the `utils/cau_hinh.py` file.
       *   Replace `API_KEY` with your Gemini API key.

## Usage

*   **Basic interaction:** Enter questions or requests directly into the command-line interface.
*   **Execute Python code:** Start the question with the `$` character (e.g., `$ print("Hello")`). Rin will understand this as a request to execute Python code.
    *   **Example:** `$ calculate the sum of 5 and 7`
*   **Execute system commands:** Start the question with the `@` character (e.g., `@ Get-Process`). Rin will understand this as a request to execute a PowerShell command.
    *   **Example:** `@ list running processes`
*   **File processing:** Start the question with the `#` character, followed by the file path and request (e.g., `# "C:\test.txt" read file`).  Rin supports the following actions:
    *   `read file`: Read the file content.  **Example:** `# "C:\my_folder\test.txt" read file`
    *   `edit file`: Edit the file content (replace, delete, add). Example: `# "C:\my_folder\test.txt" edit file, replace "hello" with "hi"`.
    *   `write file`: Write content to the file.  Example: `# "C:\my_folder\test.txt" write file with content "This is the new content"`.
    *   `create code`: Create Python code as requested.  Example: `# "C:\my_folder\my_script.py" write me a python code to calculate the factorial of a number`.
    *   `fix_code`: Fix Python code. Example: `# "C:\my_folder\error_script.py" fix code`.
    *  `upgrade`: Upgrade Python Code. Example: `# "C:\my_folder\old_script.py" upgrade`
*   **Load memory:** Start the question with the `!` character followed by the memory file name (e.g., `! memory_file.json`). This will load information from a previously saved memory file.
    *  **Example:** `!my_previous_session.json`
*   **Exit:** Type `0`.
*   **Interrupt process:** Type `2`.

## Folder Structure
```
Assistant/
├── .git/ (Not listed)
├── .gitignore
├── bieutuong/ (Not listed)
├── cac_plugin/
│   ├── thuc_thi_lenh_he_thong.py
│   ├── thuc_thi_python.py
│   ├── xu_ly_file_plugin.py
│   ├── __init__.py
│   ├── __pycache__/ (Not listed)
├── chat.py
├── core/
│   ├── chat.py
│   ├── __init__.py
│   ├── __pycache__/ (Not listed)
├── memory/ (Not listed)
├── rin.py
├── run.bat
├── utils/
│   ├── animation/
│   │   ├── hieu_ung.py
│   │   ├── __init__.py
│   │   ├── __pycache__/ (Not listed)
│   ├── cau_hinh.py
│   ├── nhat_ky.py
│   ├── __init__.py
│   ├── __pycache__/ (Not listed)
├── __init__.py
├── __pycache__/ (Not listed)
```
</details>

<!-- Japanese -->
<details>
  <summary>🇯🇵 日本語</summary>

## 概要

Assistant - Rinは、Pythonで構築された強力な仮想アシスタントであり、GoogleのGemini大規模言語モデル（LLM）を使用してさまざまなタスクを実行します。Rinは、Pythonコードの実行、システムコマンドの実行、ファイル処理、コマンドラインインターフェースを介したユーザーとの対話が可能です。Rinの特別な機能は、クロスチェックのために2番目のGeminiモデルを使用して実行結果を自己評価および改善する機能です。

## 機能

*   **Pythonコードの実行:** ユーザーがPythonコードスニペットの実行をRinに要求できるようにします。Rinはコードを生成、実行し、出力（stdout）、エラー（stderr）、実行時間などの結果を返します。
*   **システムコマンドの実行:** ユーザーがシステムコマンド（WindowsではPowerShell）の実行をRinに要求できるようにします。RinはGeminiを使用してコマンドを生成、実行し、出力、エラー、リターンコード、2番目のGeminiモデルによる評価などの結果を返します。
*   **高度なファイル処理:** 読み取り、書き込み、編集（コンテンツの置換、削除、追加）、Pythonコードの作成、Pythonコードエラーの修正、Pythonコードのアップグレードなどのファイル処理機能を提供します。Rinは、さまざまなファイル形式（テキスト、JSON、CSV、DOCX、XLSX）もサポートしています。
*   **Geminiとの対話:** プラグインに関連しない一般的な質問に答えるために、Geminiモデルと直接通信します。
*   **メモリ:** インタラクション履歴と実行結果をメモリファイルに保存し、後続の作業セッションで情報を再利用できるようにします。
*   **ファイル監視:**（実験的機能）ファイルの変更を監視し、ユーザーに通知する機能。
*   **コマンドラインインターフェース:** コマンドラインインターフェースを介してユーザーと対話し、色と効果を使用してエクスペリエンスを向上させます。

## インストール

1.  **必要条件:**
    *   Python 3.7 以上
    *   ライブラリ (詳細は`requirements.txt`ファイルを参照): `google-generativeai`, `python-magic`, `psutil`, `watchdog`, `pygments`, `docx`, `openpyxl`, `wmi`, `ctypes`, `rich`.

2.  **インストール手順:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git # あなたのリポジトリのリンクに置き換えてください
    cd your-repository-name
    python -m venv virtual_environment_name
    virtual_environment_name\Scripts\activate  # または Linux/macOS では source virtual_environment_name/bin/activate
    pip install -r requirements.txt
    ```
    *  `your-username` と `your-repository-name` をあなたのGithubリポジトリのリンクに置き換えて下さい。
    * `run.bat` ファイルを実行して、`moitruongao` 仮想環境を作成およびアクティブ化し、必要なライブラリをインストールしてプログラムを実行します。 または、上記の手順を手動で実行してください。

3.  **アプリケーションの実行:**
     * `run.bat`ファイルを実行します
    ```
    run.bat
    ```
    * または、`rin.py`ファイルを実行します
    ```
    python rin.py
    ```

4. **設定:**
   * `utils/cau_hinh.py` ファイルで API キー、モデル名、およびその他のパラメータを設定します。
      * `API_KEY` を自分の Gemini API キーに置き換えてください。

## 使用方法

*   **基本的な操作:** コマンドラインインターフェースに質問またはリクエストを直接入力します。
*   **Pythonコードの実行:**  `$` 文字で質問を開始します (例: `$ print("Hello")`)。Rin は、これを Python コードの実行要求として理解します。
    *   **例:** `$ 5 と 7 の合計を計算する`
*   **システムコマンドの実行:** `@` 文字で質問を開始します (例: `@ Get-Process`)。Rin は、これを PowerShell コマンドの実行要求として理解します。
    *   **例:** `@ 実行中のプロセスを一覧表示する`
*   **ファイル処理:** `#` 文字で質問を開始し、その後にファイルパスとリクエストを続けます (例: `# "C:\test.txt" read file`)。Rin は以下のアクションをサポートしています:
    *   `read file`: ファイルの内容を読み込みます。  **例:** `# "C:\my_folder\test.txt" read file`
    *   `edit file`: ファイルの内容を編集します (置換、削除、追加)。例: `# "C:\my_folder\test.txt" edit file, replace "hello" with "hi"`.
    *   `write file`: ファイルに内容を書き込みます。例: `# "C:\my_folder\test.txt" write file with content "This is the new content"`.
    *   `create code`: 要求に応じて Python コードを作成します。例: `# "C:\my_folder\my_script.py" write me a python code to calculate the factorial of a number`.
    *   `fix_code`: Python コードを修正します。例: `# "C:\my_folder\error_script.py" fix code`.
    *   `upgrade`: Python コードをアップグレードします。例: `# "C:\my_folder\old_script.py" upgrade code`
*   **メモリのロード:** `!` 文字で質問を開始し、その後にメモリファイル名を続けます (例: `! memory_file.json`)。これにより、以前に保存されたメモリファイルから情報がロードされます。
     *  **例:** `!my_previous_session.json`
* **終了:** `0` と入力します。
*　**処理を中断:** `2`　を入力します。

## フォルダ構造
```
Assistant/
├── .git/ (リストされていません)
├── .gitignore
├── bieutuong/ (リストされていません)
├── cac_plugin/
│   ├── thuc_thi_lenh_he_thong.py
│   ├── thuc_thi_python.py
│   ├── xu_ly_file_plugin.py
│   ├── __init__.py
│   ├── __pycache__/ (リストされていません)
├── chat.py
├── core/
│   ├── chat.py
│   ├── __init__.py
│   ├── __pycache__/ (リストされていません)
├── memory/ (リストされていません)
├── rin.py
├── run.bat
├── utils/
│   ├── animation/
│   │   ├── hieu_ung.py
│   │   ├── __init__.py
│   │   ├── __pycache__/ (リストされていません)
│   ├── cau_hinh.py
│   ├── nhat_ky.py
│   ├── __init__.py
│   ├── __pycache__/ (リストされていません)
├── __init__.py
├── __pycache__/ (リストされていません)
```

</details>
