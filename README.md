# Assistant - Rin (Testing, In Progress...) ᓚᘏᗢ

# I want open the control panel but forgot how to open it or how to do that, what should i do?
![Image](https://github.com/user-attachments/assets/bce1e88b-4710-41a4-87c0-88eced9e1635)


# Assistant - Trợ lý Ảo Cá Nhân (Rin) Dựa trên Gemini

<details>
<summary>🇻🇳 Tiếng Việt</summary>

## 1. Giới thiệu

**Assistant** (tên mã là **Rin**) là một trợ lý ảo cá nhân mã nguồn mở, được xây dựng dựa trên sức mạnh của mô hình ngôn ngữ lớn Gemini (Google). Rin được thiết kế để giúp người dùng tự động hóa các tác vụ hàng ngày, tương tác với hệ thống, xử lý file, và nhiều hơn nữa, thông qua giao diện dòng lệnh (CLI) thân thiện và trực quan.

**Mục tiêu chính của dự án Assistant (Rin):**

- **Tự động hóa tác vụ:** Giúp người dùng thực hiện các công việc phức tạp như thực thi lệnh hệ thống, chạy script Python, chỉnh sửa file một cách dễ dàng và nhanh chóng thông qua lệnh bằng ngôn ngữ tự nhiên.
- **Mở rộng khả năng:** Kiến trúc plugin linh hoạt cho phép dễ dàng mở rộng thêm các tính năng mới, phù hợp với nhu cầu sử dụng đa dạng của người dùng.
- **Tích hợp AI mạnh mẽ:** Sử dụng Gemini để hiểu và phản hồi câu hỏi, yêu cầu của người dùng một cách thông minh và tự nhiên.
- **Mã nguồn mở và Tùy biến:** Mã nguồn dự án được cung cấp mở, khuyến khích cộng đồng đóng góp và tùy chỉnh để phát triển trợ lý ảo theo ý muốn.

**Assistant (Rin) hướng đến:**

- **Người dùng cá nhân:** Muốn có một trợ lý ảo đa năng để hỗ trợ công việc và giải trí hàng ngày.
- **Nhà phát triển:**  Muốn tìm hiểu cách tích hợp AI vào ứng dụng, hoặc muốn đóng góp vào một dự án trợ lý ảo mã nguồn mở.
- **Người yêu thích công nghệ:** Muốn khám phá và tùy chỉnh một trợ lý ảo linh hoạt và mạnh mẽ.

## 2. Tính năng

**Assistant (Rin)** cung cấp một loạt các tính năng mạnh mẽ, bao gồm:

- **Thực thi lệnh hệ thống (@):** Cho phép người dùng chạy trực tiếp các lệnh PowerShell (trên Windows) thông qua câu lệnh tự nhiên, ví dụ: `@mở trình quản lý thiết bị`, `@ipconfig /all`.
- **Thực thi mã Python ($):** Có khả năng tạo và thực thi các đoạn mã Python ngắn trực tiếp trong môi trường dòng lệnh, ví dụ: `$viết code python in ra thông tin ổ đĩa`, `$tính tổng các số từ 1 đến 100 bằng python`.
- **Xử lý file nâng cao (#):** Hỗ trợ đọc, ghi, chỉnh sửa, fix lỗi, và nâng cấp code trong các file khác nhau. Các lệnh xử lý file bắt đầu bằng `#` và có thể áp dụng cho nhiều loại file, ví dụ: `#đọc file "path/to/file.txt"`, `#sửa lỗi code file "script.py"`.
- **Tích hợp Gemini (Google AI):** Sử dụng sức mạnh của Gemini để hiểu ngôn ngữ tự nhiên, tạo ra lệnh hệ thống, sinh code Python, phân tích kết quả thực thi, và đưa ra đánh giá thông minh.
- **Hỗ trợ Memory (lưu trữ phiên làm việc):** Rin có khả năng lưu trữ thông tin từ các tương tác trước đó (memory) trong phiên làm việc hiện tại, giúp đưa ra phản hồi phù hợp hơn trong các câu lệnh tiếp theo.
- **Plugin kiến trúc:** Thiết kế theo dạng plugin, dễ dàng thêm mới các chức năng và mở rộng khả năng của trợ lý ảo thông qua việc phát triển các plugin mới.
- **Thông báo và Phân tích kết quả:**  Sau khi thực hiện lệnh, Rin cung cấp thông báo trạng thái (thành công/lỗi), kết quả đầu ra (output), phân tích lỗi (nếu có), và đánh giá kết quả bằng Gemini 2.
- **Hiệu ứng động và Giao diện thân thiện:** Sử dụng hiệu ứng động "đang suy nghĩ" để tạo trải nghiệm tương tác thú vị. Giao diện dòng lệnh (CLI) được tối ưu hóa về màu sắc và bố cục để dễ đọc và sử dụng.
- **Hoạt động trên Windows (tối ưu hóa cho PowerShell):** Rin được phát triển chủ yếu để chạy trên hệ điều hành Windows và tận dụng sức mạnh của PowerShell cho các lệnh hệ thống.

## 3. Cấu trúc Dự án

```
Assistant/
├── .git/             (Thư mục Git - không liệt kê khi tạo tài liệu)
├── .gitignore        (File chỉ định các tệp/thư mục Git bỏ qua)
├── Assistant/
├── bieutuong/         (Thư mục chứa các biểu tượng và hình ảnh - không liệt kê khi tạo tài liệu)
├── cac_plugin/       (Thư mục chứa các plugin chức năng mở rộng)
│   ├── thuc_thi_lenh_he_thong.py (Plugin thực thi lệnh hệ thống PowerShell)
│   ├── thuc_thi_python.py     (Plugin thực thi mã Python)
│   ├── xu_ly_file_plugin.py   (Plugin xử lý file nâng cao)
│   ├── __init__.py
│   └── __pycache__/         (Thư mục cache Python - không liệt kê)
├── core/              (Thư mục chứa mã nguồn core của trợ lý ảo)
│   ├── chat.py         (Module quản lý giao tiếp với Gemini)
│   ├── __init__.py
│   └── __pycache__/         (Thư mục cache Python - không liệt kê)
├── memory/            (Thư mục lưu trữ memory và session - không liệt kê)
├── README.md
├── rin.py             (File mã nguồn chính, khởi chạy trợ lý ảo)
├── run.bat            (File batch script để chạy ứng dụng trên Windows)
├── utils/             (Thư mục chứa các module tiện ích)
│   ├── animation/      (Thư mục chứa hiệu ứng động)
│   │   ├── hieu_ung.py  (Module hiệu ứng động)
│   │   └── __init__.py
│   │   └── __pycache__/     (Thư mục cache Python - không liệt kê)
│   ├── cau_hinh.py     (File cấu hình các hằng số và cài đặt)
│   ├── nhat_ky.py      (Module nhật ký hoạt động)
│   ├── rin.bat        (File batch script phụ trợ)
│   ├── __init__.py
│   └── __pycache__/     (Thư mục cache Python - không liệt kê)
├── __init__.py
```

- **`.git/`, `.gitignore`**: Các file và thư mục liên quan đến Git, quản lý mã nguồn.
- **`Assistant/`**: Thư mục có thể dùng để chứa các tài liệu hoặc nguồn lực khác cho dự án (hiện tại có vẻ trống).
- **`bieutuong/`**: Thư mục chứa các file biểu tượng, hình ảnh, ASCII art sử dụng cho giao diện (có thể được tùy chỉnh).
- **`cac_plugin/`**: Thư mục cốt lõi chứa các plugin chức năng:
    - **`thuc_thi_lenh_he_thong.py`**: Plugin cho phép thực thi lệnh hệ thống (PowerShell).
    - **`thuc_thi_python.py`**: Plugin cho phép thực thi mã Python trực tiếp.
    - **`xu_ly_file_plugin.py`**: Plugin cung cấp các chức năng xử lý file (đọc, ghi, sửa...).
    - **`__init__.py`**: File khởi tạo package, báo cho Python biết đây là một package.
- **`core/`**: Chứa các module core của hệ thống:
    - **`chat.py`**: Module xử lý giao tiếp với Gemini API, khởi tạo và duy trì phiên chat.
    - **`__init__.py`**: File khởi tạo package.
- **`memory/`**: Thư mục (không được commit lên Git) lưu trữ memory của phiên làm việc và lịch sử hội thoại.
- **`README.md`**: File README này, cung cấp thông tin tổng quan về dự án.
- **`rin.py`**: File Python chính, chứa vòng lặp chính của chương trình, xử lý input người dùng, gọi plugin, và giao tiếp với Gemini.
- **`run.bat`**: File batch để chạy ứng dụng một cách dễ dàng trên Windows (kích hoạt môi trường ảo và chạy `rin.py`).
- **`utils/`**: Chứa các module tiện ích dùng chung:
    - **`animation/`**: Chứa module `hieu_ung.py` để tạo hiệu ứng động (ví dụ: "đang suy nghĩ").
    - **`cau_hinh.py`**: File cấu hình các hằng số, cài đặt, API key, màu sắc, v.v.
    - **`nhat_ky.py`**: Module quản lý nhật ký (logging) hoạt động của chương trình.
    - **`rin.bat`**: File batch script phụ trợ (ví dụ, có thể dùng cho mục đích debug hoặc test).
    - **`__init__.py`**: File khởi tạo package.
- **`__init__.py` (gốc thư mục `Assistant/`)**: File khởi tạo package cho thư mục gốc.

## 4. Cài đặt

### Điều kiện tiên quyết

Trước khi cài đặt và chạy **Assistant (Rin)**, bạn cần đảm bảo đã cài đặt các phần mềm sau:

1.  **Python:** Phiên bản Python 3.8 trở lên. Tải từ [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **pip:** (Đi kèm Python) Pip là trình quản lý gói của Python, dùng để cài đặt các thư viện phụ thuộc.

3.  **API Key của Gemini API:** Bạn cần có API key hợp lệ để sử dụng Gemini API.  Tham khảo hướng dẫn từ Google Generative AI để lấy API key. Sau khi có key, hãy đặt nó vào biến `API_KEY` trong file `utils/cau_hinh.py`. **Cẩn trọng bảo mật API Key của bạn**.

### Các bước cài đặt

1. **Tải Dự án:** Clone hoặc tải mã nguồn dự án **Assistant** từ GitHubGitHub.

   ```bash
   git clone https://github.com/Rin1809/System_Assistant
   cd Assistant
   ```

2. **Tạo Môi trường Ảo (khuyến khích):** Tạo môi trường ảo để quản lý thư viện riêng cho dự án này. Trong thư mục dự án **Assistant**, chạy lệnh:

   ```bash
   python -m venv moitruongao
   ```

3. **Kích hoạt Môi trường Ảo:**

   - **Windows:** Chạy file `run.bat`. File này sẽ kích hoạt môi trường ảo và chạy ứng dụng.

     Hoặc kích hoạt thủ công bằng lệnh trong Command Prompt/PowerShell:
     ```bash
     moitruongao\Scripts\activate.bat
     ```

   - **macOS/Linux:** Chạy lệnh trong Terminal:
     ```bash
     source moitruongao/bin/activate
     ```

4. **Cài đặt Thư viện:** Cài đặt các thư viện Python cần thiết từ file `requirements.txt` (nếu có trong dự án). Nếu không, cài đặt thủ công (trong môi trường ảo đã kích hoạt):

   ```bash
   pip install -r requirements.txt  # Nếu có file requirements.txt

   # Hoặc cài thủ công nếu không có file requirements.txt:
   pip install google-generativeai pygments python-magic python-docx openpyxl rich psutil watchdog wmi
   ```

5. **Cấu hình API Key:** Mở file `utils/cau_hinh.py` và thay thế giá trị placeholder trong biến `API_KEY = "YOUR_API_KEY_HERE"` bằng API key Gemini của bạn.

6. **Chạy Ứng dụng:**

   - **Windows (khuyến khích):** Chạy file `run.bat`.

   - **Mọi hệ điều hành (sau khi kích hoạt môi trường ảo):** Chạy lệnh:

     ```bash
     python rin.py
     ```

     Trợ lý ảo Rin sẽ khởi động trong dòng lệnh.

## 5. Cách Sử dụng

**Giao diện dòng lệnh (CLI) của Assistant (Rin):**

Khi chạy `rin.py` hoặc `run.bat`, bạn sẽ thấy giao diện dòng lệnh của Rin. Bạn có thể tương tác với Rin thông qua các lệnh bằng ngôn ngữ tự nhiên, với các tiền tố đặc biệt để gọi các chức năng plugin:

- **Câu hỏi thông thường (không tiền tố):**  Đối với các câu hỏi thông thường, bạn có thể nhập trực tiếp câu hỏi. Rin sẽ sử dụng Gemini để trả lời. Ví dụ: `thời tiết hôm nay thế nào?`, `tóm tắt về lịch sử Việt Nam`.
- **Thực thi lệnh hệ thống (tiền tố `@`):** Để thực thi lệnh hệ thống (PowerShell trên Windows), bắt đầu câu lệnh với ký tự `@`. Ví dụ: `@mở notepad`, `@ipconfig`.
- **Thực thi mã Python (tiền tố `$`)**: Để chạy mã Python, bắt đầu câu lệnh với `$`. Ví dụ: `$viết code python tính giai thừa của 10`, `$in ra ngày giờ hiện tại bằng python`.
- **Xử lý file (tiền tố `#`)**: Để thực hiện các thao tác trên file (đọc, sửa, ghi...), dùng tiền tố `#`.  Theo sau `#` là lệnh và đường dẫn file trong dấu nháy kép. Ví dụ: `#đọc file "path/to/my_file.txt"`, `#sửa file "script.py", thay thế 'old_text' bằng 'new_text'`.

**Các lệnh thường dùng:**

- **`rin`**: Gọi tên trợ lý để "đánh thức" hoặc bắt đầu cuộc trò chuyện (có thể không cần thiết trong mỗi câu lệnh).
- **`0`**: Nhập số `0` và Enter để thoát khỏi chương trình.
- **`2`**: Nhập số `2` và Enter để ngắt tiến trình hiện tại (nếu có).
- **`!` + `[tên_file_memory.json]`**:  Load memory từ một file JSON đã lưu trước đó trong thư mục `memory/`. Ví dụ: `!Memory_2024-12-28_10-30-45.json`.

**Lưu ý:**

- Đường dẫn file trong lệnh `#` nên được đặt trong dấu nháy kép (`"`).
- Rin hiện tại tối ưu hóa cho hệ điều hành Windows và PowerShell.
- Để sử dụng plugin xử lý file (`#`), bạn cần cung cấp đường dẫn file hợp lệ và đảm bảo Rin có quyền truy cập file.

## 6. Ví dụ Sử dụng

Dưới đây là một số ví dụ minh họa cách sử dụng **Assistant (Rin)** cho các tác vụ khác nhau:

**Ví dụ 1: Hỏi thông tin thời tiết:**

```
[Thời gian hiện tại] Rin: Tôi:  thời tiết Hà Nội hôm nay thế nào?

[Thời gian] Rin: Rin:  ☀️ Hà Nội hôm nay trời nắng đẹp đó cậu! Nhiệt độ dao động từ 20-28 độ C. Nhớ mang kính râm khi ra đường nha!
```

**Ví dụ 2: Mở ứng dụng bằng lệnh hệ thống:**

```
[Thời gian hiện tại] Rin: Tôi:  @mở notepad

[Thời gian] Rin: Rin:  [PLUGIN: Thực thi lệnh hệ thống] Rin:

[Thực thi lệnh hệ thống] ✨ Hoàn tất (0.25s) ✨
────────────────────────────────────────────────────────────────────────
✅ Thực thi thành công
🔍  Phân tích:
    -  - Result:

        -   "The command was successfully executed, and Notepad should be open now." (One line like this should not exceed 15 words)
- ➡️ Output:

    -

Error:
────────────────────────────────────────────────────────────────────────
```
*(Notepad sẽ được mở trên máy tính của bạn)*

**Ví dụ 3: Lấy thông tin ổ đĩa bằng Python:**

```
[Thời gian hiện tại] Rin: Tôi:  $viết code python in ra thông tin ổ đĩa

[Thời gian] Rin: Rin:  [PLUGIN: Thực thi Python] Rin:

[Thực thi Python] ✨ Hoàn tất (1.55s) ✨
────────────────────────────────────────────────────────────────────────
✅ Đã thực thi mã Python.
🔍  Phân tích:
    -  - Result:

        -   "The code executed successfully without errors." (One line like this should not exceed 15 words)
        -   "The disk information is extracted and printed as expected."
💽 Thông tin ổ đĩa:
    - ➡️ Ổ đĩa
      ➡️ Mô tả     Local Fixed Disk
      ➡️ Kích thước   931.51 GB
      ➡️ Còn trống    349.84 GB
      ➡️ Hệ thống File   NTFS
    - ➡️ Ổ đĩa   D:
      ➡️ Mô tả     Local Fixed Disk
      ➡️ Kích thước   1023.96 GB
      ➡️ Còn trống    754.85 GB
      ➡️ Hệ thống File   NTFS
    - ➡️ Ổ đĩa   E:
      ➡️ Mô tả     CD-ROM Disc
      ➡️ Kích thước   0.0 GB
      ➡️ Còn trống    0.0 GB
      ➡️ Hệ thống File   CDFS
    - ➡️ Ổ đĩa   F:
      ➡️ Mô tả     Local Fixed Disk
      ➡️ Kích thước   465.76 GB
      ➡️ Còn trống    444.04 GB
      ➡️ Hệ thống File   NTFS
    - ➡️ Ổ đĩa   G:
      ➡️ Mô tả     Local Fixed Disk
      ➡️ Kích thước   465.76 GB
      ➡️ Còn trống    439.14 GB
      ➡️ Hệ thống File   NTFS
    - ➡️ Ổ đĩa   C:
      ➡️ Mô tả     Local Fixed Disk
      ➡️ Kích thước   476.39 GB
      ➡️ Còn trống    44.47 GB
      ➡️ Hệ thống File   NTFS
────────────────────────────────────────────────────────────────────────
```

**Ví dụ 4: Đọc nội dung file code Python:**

```
[Thời gian hiện tại] Rin: Tôi:  #đọc file "utils/cau_hinh.py"

[Thời gian] Rin: Rin:  [PLUGIN: XuLyFile] Rin:
[Xử lý file] ✨ Hoàn tất (0.00s) ✨
────────────────────────────────────────────────────────────────────────
✅ Đã đọc file
    Nội dung:
    ----------------------------------------
    # utils/cau_hinh.py
    import threading
    import sys
    import codecs
    import os
    import re
    from rich.console import Console
    from rich.table import Table

    # Khóa Rin
    PRINT_LOCK = threading.Lock()

    # Màu sắc
    PINK1 = "\033[38;2;255;192;203m"
    PLUM2 = "\033[38;2;221;160;221m"
    RICH_PINK = "\033[38;2;255;105;180m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[38;5;226m"  # Nền vàng nhạt
    BLUE = "\033[94m"
    ORANGE = "\033[38;2;255;105;180m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNBOLD = "\033[0m"
    GREEN = "\033[38;5;154m"
    RIN = "\033[38;5;159m"
    TIME = "\033[38;5;231m"
    THISTLE1 = "\033[38;2;255;225;255m"
    DARK_ORANGE = "\033[38;2;255;140;0m"
    MODEL_NAME = "gemini-2.0-flash-exp" # Thay doi model neu can
    MODEL_NAME2 = "gemini-exp-1206"
    TEMP = 0.7
    TOP_P = 0.95
    TOP_K = 40
    MAX_OUTPUT_TOKENS = 8192 #giam xuon == nhanh hon
    API_KEY = "YOUR_API_KEY_HERE"

    SUCCESS = f"{GREEN}✔{RESET}"
    FAIL = f"{RED}❌{RESET}"
    ERROR = f"{RED}⚠{RESET}"

    # path luu memory
    MEMORY_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "memory")

    MEMORY_FILE_FORMAT = "Memory_%Y-%m-%d_%H-%M-%S.json"
    SESSION_FILE_FORMAT = "Session_%Y-%m-%d_%H-%M-%S.json"

    def remove_ansi_escape_codes(text):
        """Loại bỏ mã màu ANSI khỏi chuỗi."""
        return re.sub(r'\x1b\[[0-9;]*[mG]', '', text)

    def format_output(plugin_name, message=None, execution_time=None, content=None, error=None, analysis=None, output=None, code=None, disk_info=None, detailed=True):
        """
        Formats the output for better readability.
        """
        console = Console()

        if not detailed:
            if execution_time is not None:
                console.print(f"[{plugin_name}] ✨ Hoàn tất ({execution_time:.2f}s) ✨")
            if message:
                console.print(f"✅ {message}")
            if error:
                console.print(f"❌ {error}")
            return

        table = Table(title=f"[{plugin_name}]")

        table.add_column("Trường", style="dim", width=20)
        table.add_column("Giá trị")

        if message:
            table.add_row("✅ Thông báo", message)
        if execution_time is not None:
            table.add_row("✨ Thời gian", f"{execution_time:.2f}s")
        if analysis:
            table.add_row("🔍 Phân tích", analysis)
        if output:
            table.add_row("➡️ Output", output)
        if content:
            table.add_row("📄 Nội dung", content)
        if code:
            table.add_row("💻 Code", code)
        if disk_info:
            table.add_row("💽 Thông tin ổ đĩa", "")
            for disk in disk_info:
                table.add_row("    - ➡️ Ổ đĩa", disk['caption'])
                table.add_row("      ➡️ Mô tả", disk['description'])
                table.add_row("      ➡️ Kích thước", f"{disk['size']} GB")
                table.add_row("      ➡️ Còn trống", f"{disk['free_space']} GB")
                table.add_row("      ➡️ Hệ thống File", disk['file_system'])
        if error:
            table.add_row("❌ Lỗi", error)

        console.print(table)
    ----------------------------------------
────────────────────────────────────────────────────────────────────────
```

**Ví dụ 5: Chỉnh sửa file text (thay thế từ):**

```
[Thời gian hiện tại] Rin: Tôi:  #sửa file "example.txt" thay thế "từ cũ" bằng "từ mới"

[Thời gian] Rin: Rin:  [PLUGIN: XuLyFile] Rin:
[Xử lý file] ✨ Hoàn tất (0.01s) ✨
────────────────────────────────────────────────────────────────────────
✅ Đã chỉnh sửa file
    Code:
    ----------------------------------------
    Không có thay đổi
    ----------------------------------------
────────────────────────────────────────────────────────────────────────
```
*(File `example.txt` sẽ được chỉnh sửa, nếu có "từ cũ" sẽ bị thay thế bằng "từ mới")*

**Khám phá thêm:**

Hãy thử nghiệm với các lệnh khác nhau, kết hợp các tính năng, và tùy chỉnh các plugin để khám phá toàn bộ tiềm năng của **Assistant (Rin)**.

## 7. Cấu hình Nâng cao

- **File cấu hình `utils/cau_hinh.py`:** File này chứa các cấu hình quan trọng:
    - `API_KEY`:  **Bắt buộc** phải thay thế bằng API key Gemini của bạn.
    - `MODEL_NAME`, `MODEL_NAME2`: Tên các model Gemini được sử dụng. Có thể thay đổi để thử nghiệm các model khác.
    - `TEMP`, `TOP_P`, `TOP_K`, `MAX_OUTPUT_TOKENS`: Các tham số cấu hình cho model Gemini.  Bạn có thể tùy chỉnh để điều chỉnh độ sáng tạo, độ chính xác, và tốc độ phản hồi của Gemini.
    - Các biến màu sắc: `PINK1`, `RED`, `GREEN`, `YELLOW`, v.v.:  Mã màu ANSI để tùy chỉnh giao diện dòng lệnh.
    - `MEMORY_DIR`, `MEMORY_FILE_FORMAT`, `SESSION_FILE_FORMAT`: Đường dẫn và định dạng file cho việc lưu trữ memory và session.

- **Plugin kiến trúc:** Nếu bạn muốn mở rộng thêm tính năng cho **Assistant (Rin)**, bạn có thể phát triển các plugin mới trong thư mục `cac_plugin/`. Xem các plugin mẫu (`thuc_thi_lenh_he_thong.py`, `thuc_thi_python.py`, `xu_ly_file_plugin.py`) để hiểu cách xây dựng một plugin.

- **Chạy bằng quyền Admin (Windows):** Để một số plugin (ví dụ: `thuc_thi_lenh_he_thong.py`) hoạt động hiệu quả nhất (đặc biệt các lệnh yêu cầu quyền admin), bạn nên chạy `rin.py` hoặc `run.bat` với quyền Administrator. Khi khởi động, Rin sẽ kiểm tra quyền admin và tự động yêu cầu chạy lại với quyền admin nếu cần thiết.

</details>

<details>
<summary>🇬🇧 English</summary>

## 1. Introduction

**Assistant** (codename **Rin**) is an open-source personal virtual assistant, built on the powerful Gemini large language model (Google). Rin is designed to help users automate daily tasks, interact with the system, process files, and much more, through a user-friendly and intuitive command-line interface (CLI).

**The main goals of the Assistant (Rin) project:**

- **Task Automation:** Help users perform complex tasks like executing system commands, running Python scripts, and editing files easily and quickly through natural language commands.
- **Extensibility:** Flexible plugin architecture allows for easy addition of new features, suitable for diverse user needs.
- **Powerful AI Integration:** Leverage Gemini to understand and respond to user questions and requests intelligently and naturally.
- **Open Source and Customizable:** Project source code is open, encouraging community contributions and customization to develop virtual assistants as desired.

**Assistant (Rin) is aimed at:**

- **Personal Users:** Who want a versatile virtual assistant to support daily work and entertainment.
- **Developers:**  Who want to learn how to integrate AI into applications, or want to contribute to an open-source virtual assistant project.
- **Tech Enthusiasts:** Who want to explore and customize a flexible and powerful virtual assistant.

## 2. Features

**Assistant (Rin)** offers a range of powerful features, including:

- **System Command Execution (@):** Allows users to directly run PowerShell commands (on Windows) through natural language commands, for example: `@open device manager`, `@ipconfig /all`.
- **Python Code Execution ($):** Capable of creating and executing short Python code snippets directly in the command-line environment, for example: `$write python code to print disk information`, `$calculate the sum of numbers from 1 to 100 using python`.
- **Advanced File Processing (#):** Supports reading, writing, editing, fixing code, and upgrading code in different files. File processing commands start with `#` and can be applied to various file types, for example: `#read file "path/to/file.txt"`, `#fix code file "script.py"`.
- **Gemini Integration (Google AI):** Harnesses the power of Gemini to understand natural language, generate system commands, generate Python code, analyze execution results, and provide intelligent evaluations.
- **Memory Support (Session History):** Rin has the ability to store information from previous interactions (memory) in the current session, helping to provide more relevant responses in subsequent commands.
- **Plugin Architecture:** Designed with a plugin-based architecture, making it easy to add new functions and expand the virtual assistant's capabilities by developing new plugins.
- **Notification and Result Analysis:**  After executing commands, Rin provides status notifications (success/error), output results, error analysis (if any), and result evaluation using Gemini 2.
- **Dynamic Effects and Friendly Interface:** Uses dynamic "thinking" effects to create an engaging interaction experience. The command-line interface (CLI) is optimized for color and layout for readability and ease of use.
- **Runs on Windows (Optimized for PowerShell):** Rin is primarily developed to run on the Windows operating system and leverage the power of PowerShell for system commands.

## 3. Project Structure

```
Assistant/
├── .git/             (Git Directory - not listed in documentation)
├── .gitignore        (File specifying files/directories Git should ignore)
├── Assistant/
├── bieutuong/         (Directory containing icons and images - not listed in documentation)
├── cac_plugin/       (Directory containing extended function plugins)
│   ├── thuc_thi_lenh_he_thong.py (PowerShell system command execution plugin)
│   ├── thuc_thi_python.py     (Python code execution plugin)
│   ├── xu_ly_file_plugin.py   (Advanced file processing plugin)
│   ├── __init__.py
│   └── __pycache__/         (Python cache directory - not listed)
├── core/              (Directory containing the core source code of the virtual assistant)
│   ├── chat.py         (Module for managing Gemini communication)
│   ├── __init__.py
│   └── __pycache__/         (Python cache directory - not listed)
├── memory/            (Directory for storing session memory and history - not listed)
├── README.md
├── rin.py             (Main source code file, starts the virtual assistant)
├── run.bat            (Batch script to easily run the application on Windows)
├── utils/             (Directory containing utility modules)
│   ├── animation/      (Directory containing dynamic effects)
│   │   ├── hieu_ung.py  (Dynamic effects module)
│   │   └── __init__.py
│   │   └── __pycache__/     (Python cache directory - not listed)
│   ├── cau_hinh.py     (Configuration file for constants and settings)
│   ├── nhat_ky.py      (Activity logging module)
│   ├── rin.bat        (Auxiliary batch script file)
│   ├── __init__.py
│   └── __pycache__/     (Python cache directory - not listed)
├── __init__.py
```

- **`.git/`, `.gitignore`**: Git-related files and directories for source code management.
- **`Assistant/`**: Directory potentially for documents or other project resources (currently seems empty).
- **`bieutuong/`**: Directory containing icon files, images, ASCII art used for the interface (can be customized).
- **`cac_plugin/`**: Core directory containing function plugins:
    - **`thuc_thi_lenh_he_thong.py`**: Plugin for executing system commands (PowerShell).
    - **`thuc_thi_python.py`**: Plugin for direct Python code execution.
    - **`xu_ly_file_plugin.py`**: Plugin providing file processing functionalities (read, write, edit...).
    - **`__init__.py`**: Package initialization file, tells Python this is a package.
- **`core/`**: Contains core system modules:
    - **`chat.py`**: Module handling Gemini API communication, initializes and maintains chat sessions.
    - **`__init__.py`**: Package initialization file.
- **`memory/`**: Directory (not committed to Git) storing session memory and conversation history.
- **`README.md`**: This README file, provides project overview information.
- **`rin.py`**: Main Python file, contains program's main loop, processes user input, calls plugins, and interacts with Gemini.
- **`run.bat`**: Batch file to easily run the application on Windows (activates virtual environment and runs `rin.py`).
- **`utils/`**: Contains common utility modules:
    - **`animation/`**: Contains `hieu_ung.py` module to create dynamic effects (e.g., "thinking" animation).
    - **`cau_hinh.py`**: Configuration file for constants, settings, API key, colors, etc.
    - **`nhat_ky.py`**: Module for managing program activity logs (logging).
    - **`rin.bat`**: Auxiliary batch script file (e.g., can be used for debugging or testing purposes).
    - **`__init__.py`**: Package initialization file.
- **`__init__.py`** (root `Assistant/` directory): Package initialization file for the root directory.

## 4. Installation

### Prerequisites

Before installing and running **Assistant (Rin)**, ensure you have the following software installed:

1.  **Python:** Python version 3.8 or later. Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **pip:** (Included with Python) Pip is Python's package manager, used to install dependent libraries.

3.  **Gemini API Key:** You need a valid Gemini API key to use the Gemini API. Refer to Google Generative AI documentation to get an API key. Once you have the key, put it in the `API_KEY` variable in the `utils/cau_hinh.py` file. **Keep your API Key secure**.

### Installation Steps

1. **Download Project:** Clone or download the **Assistant** project source code from GitHub.

   ```bash
   git clone https://github.com/Rin1809/System_Assistant
   cd Assistant
   ```

2. **Create Virtual Environment (Recommended):** Create a virtual environment to manage libraries separately for this project. In the **Assistant** project directory, run the command:

   ```bash
   python -m venv moitruongao
   ```

3. **Activate Virtual Environment:**

   - **Windows:** Run the `run.bat` file. This file will activate the virtual environment and run the application.

     Or manually activate using the command in Command Prompt/PowerShell:
     ```bash
     moitruongao\Scripts\activate.bat
     ```

   - **macOS/Linux:** Run the command in the Terminal:
     ```bash
     source moitruongao/bin/activate
     ```

4. **Install Libraries:** Install the necessary Python libraries from the `requirements.txt` file (if present in the project). Otherwise, install them manually (in the activated virtual environment):

   ```bash
   pip install -r requirements.txt  # If requirements.txt file exists

   # Or install manually if requirements.txt is not present:
   pip install google-generativeai pygments python-magic python-docx openpyxl rich psutil watchdog wmi
   ```

5. **Configure API Key:** Open the `utils/cau_hinh.py` file and replace the placeholder value in the `API_KEY = "YOUR_API_KEY_HERE"` variable with your Gemini API key.

6. **Run Application:**

   - **Windows (Recommended):** Run the `run.bat` file.

   - **Any OS (after activating virtual environment):** Run the command:

     ```bash
     python rin.py
     ```

     The Rin virtual assistant will start in the command line.

## 5. Usage

**Command-Line Interface (CLI) of Assistant (Rin):**

When you run `rin.py` or `run.bat`, you will see Rin's command-line interface. You can interact with Rin through natural language commands, with special prefixes to invoke plugin functions:

- **Normal Questions (no prefix):** For general questions, you can directly enter the question. Rin will use Gemini to answer. For example: `how's the weather today in Hanoi?`, `summarize Vietnamese history`.
- **System Command Execution (prefix `@`):** To execute system commands (PowerShell on Windows), start the command with the `@` character. For example: `@open notepad`, `@ipconfig`.
- **Python Code Execution (prefix `$`)**: To run Python code, start the command with `$`. For example: `$write python code to calculate factorial of 10`, `$print current date and time using python`.
- **File Processing (prefix `#`)**: To perform file operations (read, edit, write...), use the prefix `#`. Following `#` is the command and the file path in double quotes. For example: `#read file "path/to/my_file.txt"`, `#edit file "script.py", replace 'old_text' with 'new_text'`.

**Common Commands:**

- **`rin`**: Calling the assistant's name to "wake up" or start a conversation (may not be necessary in every command).
- **`0`**: Enter number `0` and Enter to exit the program.
- **`2`**: Enter number `2` and Enter to interrupt the current process (if any).
- **`!` + `[memory_file_name.json]`**:  Load memory from a previously saved JSON file in the `memory/` directory. For example: `!Memory_2024-12-28_10-30-45.json`.

**Note:**

- File paths in `#` commands should be enclosed in double quotes (`"`).
- Rin is currently optimized for Windows OS and PowerShell.
- To use the file processing plugin (`#`), you need to provide valid file paths and ensure Rin has file access permissions.

## 6. Usage Examples

Below are some examples illustrating how to use **Assistant (Rin)** for different tasks:

**Example 1: Asking about weather information:**

```
[Current Time] Rin: Me:  how's the weather in Hanoi today?

[Time] Rin: Rin:  ☀️ Hanoi's weather today is sunny and beautiful! The temperature ranges from 20-28 degrees Celsius. Remember to wear sunglasses when going out!
```

**Example 2: Opening an application using system command:**

```
[Current Time] Rin: Me:  @open notepad

[Time] Rin: Rin:  [PLUGIN: System Command Execution] Rin:

[System Command Execution] ✨ Completed (0.25s) ✨
────────────────────────────────────────────────────────────────────────
✅ Execution successful
🔍  Analysis:
    -  - Result:

        -   "The command was successfully executed, and Notepad should be open now." (One line like this should not exceed 15 words)
- ➡️ Output:

    -

Error:
────────────────────────────────────────────────────────────────────────
```
*(Notepad will be opened on your computer)*

**Example 3: Getting disk information using Python:**

```
[Current Time] Rin: $write python code to print disk information

[Time] Rin: Rin:  [PLUGIN: Python Execution] Rin:

[Python Execution] ✨ Completed (1.55s) ✨
────────────────────────────────────────────────────────────────────────
✅ Python code executed successfully.
🔍  Analysis:
    -  - Result:

        -   "The code executed successfully without errors." (One line like this should not exceed 15 words)
        -   "The disk information is extracted and printed as expected."
💽 Disk Information:
    - ➡️ Disk
      ➡️ Description     Local Fixed Disk
      ➡️ Size          931.51 GB
      ➡️ Free Space    349.84 GB
      ➡️ File System   NTFS
    - ➡️ Disk   D:
      ➡️ Description     Local Fixed Disk
      ➡️ Size          1023.96 GB
      ➡️ Free Space    754.85 GB
      ➡️ File System   NTFS
    - ➡️ Disk   E:
      ➡️ Description     CD-ROM Disc
      ➡️ Size          0.0 GB
      ➡️ Free Space    0.0 GB
      ➡️ File System   CDFS
    - ➡️ Disk   F:
      ➡️ Description     Local Fixed Disk
      ➡️ Size          465.76 GB
      ➡️ Free Space    444.04 GB
      ➡️ File System   NTFS
    - ➡️ Disk   G:
      ➡️ Description     Local Fixed Disk
      ➡️ Size          465.76 GB
      ➡️ Free Space    439.14 GB
      ➡️ File System   NTFS
    - ➡️ Disk   C:
      ➡️ Description     Local Fixed Disk
      ➡️ Size          476.39 GB
      ➡️ Free Space    44.47 GB
      ➡️ File System   NTFS
────────────────────────────────────────────────────────────────────────
```

**Example 4: Reading content of a Python code file:**

```
[Current Time] Rin: Me:  #read file "utils/cau_hinh.py"

[Time] Rin: Rin:  [PLUGIN: File Processing] Rin:
[File processing] ✨ Completed (0.00s) ✨
────────────────────────────────────────────────────────────────────────
✅ File read successfully
    Content:
    ----------------------------------------
    # utils/cau_hinh.py
    import threading
    import sys
    import codecs
    import os
    import re
    from rich.console import Console
    from rich.table import Table

    # Rin Lock
    PRINT_LOCK = threading.Lock()

    # Colors
    PINK1 = "\033[38;2;255;192;203m"
    PLUM2 = "\033[38;2;221;160;221m"
    RICH_PINK = "\033[38;2;255;105;180m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[38;5;226m"  # Light Yellow background
    BLUE = "\033[94m"
    ORANGE = "\033[38;2;255;105;180m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNBOLD = "\033[0m"
    GREEN = "\033[38;5;154m"
    RIN = "\033[38;5;159m"
    TIME = "\033[38;5;231m"
    THISTLE1 = "\033[38;2;255;225;255m"
    DARK_ORANGE = "\033[38;2;255;140;0m"
    MODEL_NAME = "gemini-2.0-flash-exp" # Change model if needed
    MODEL_NAME2 = "gemini-exp-1206"
    TEMP = 0.7
    TOP_P = 0.95
    TOP_K = 40
    MAX_OUTPUT_TOKENS = 8192 # Reduce == faster
    API_KEY = "YOUR_API_KEY_HERE"

    SUCCESS = f"{GREEN}✔{RESET}"
    FAIL = f"{RED}❌{RESET}"
    ERROR = f"{RED}⚠{RESET}"

    # memory save path
    MEMORY_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "memory")

    MEMORY_FILE_FORMAT = "Memory_%Y-%m-%d_%H-%M-%S.json"
    SESSION_FILE_FORMAT = "Session_%Y-%m-%d_%H-%M-%S.json"

    def remove_ansi_escape_codes(text):
        """Removes ANSI color codes from a string."""
        return re.sub(r'\x1b\[[0-9;]*[mG]', '', text)

    def format_output(plugin_name, message=None, execution_time=None, content=None, error=None, analysis=None, output=None, code=None, disk_info=None, detailed=True):
        """
        Formats the output for better readability.
        """
        console = Console()

        if not detailed:
            if execution_time is not None:
                console.print(f"[{plugin_name}] ✨ Completed ({execution_time:.2f}s) ✨")
            if message:
                console.print(f"✅ {message}")
            if error:
                console.print(f"❌ {error}")
            return

        table = Table(title=f"[{plugin_name}]")

        table.add_column("Field", style="dim", width=20)
        table.add_column("Value")

        if message:
            table.add_row("✅ Message", message)
        if execution_time is not None:
            table.add_row("✨ Time", f"{execution_time:.2f}s")
        if analysis:
            table.add_row("🔍 Analysis", analysis)
        if output:
            table.add_row("➡️ Output", output)
        if content:
            table.add_row("📄 Content", content)
        if code:
            table.add_row("💻 Code", code)
        if disk_info:
            table.add_row("💽 Disk Information", "")
            for disk in disk_info:
                table.add_row("    - ➡️ Drive", disk['caption'])
                table.add_row("      ➡️ Description", disk['description'])
                table.add_row("      ➡️ Size", f"{disk['size']} GB")
                table.add_row("      ➡️ Free Space", f"{disk['free_space']} GB")
                table.add_row("      ➡️ File System", disk['file_system'])
        if error:
            table.add_row("❌ Error", error)

        console.print(table)
    ----------------------------------------
────────────────────────────────────────────────────────────────────────
```

**Example 5: Editing a text file (replacing text):**

```
[Current Time] Rin: Me:  #edit file "example.txt" replace "old text" with "new text"

[Time] Rin: Rin:  [PLUGIN: File Processing] Rin:
[File processing] ✨ Completed (0.01s) ✨
────────────────────────────────────────────────────────────────────────
✅ File edited successfully
    Code:
    ----------------------------------------
    No changes made
    ----------------------------------------
────────────────────────────────────────────────────────────────────────
```
*(File `example.txt` will be edited, if "old text" exists, it will be replaced with "new text")*

**Explore Further:**

Experiment with different commands, combine features, and customize plugins to explore the full potential of **Assistant (Rin)**.

## 7. Advanced Configuration

- **Configuration File `utils/cau_hinh.py`:** This file contains important configurations:
    - `API_KEY`:  **Required**, must be replaced with your Gemini API key.
    - `MODEL_NAME`, `MODEL_NAME2`: Names of Gemini models used. Can be changed to experiment with other models.
    - `TEMP`, `TOP_P`, `TOP_K`, `MAX_OUTPUT_TOKENS`: Configuration parameters for the Gemini model. You can customize these to adjust the creativity, accuracy, and response speed of Gemini.
    - Color variables: `PINK1`, `RED`, `GREEN`, `YELLOW`, etc.: ANSI color codes to customize the command-line interface.
    - `MEMORY_DIR`, `MEMORY_FILE_FORMAT`, `SESSION_FILE_FORMAT`: Paths and file formats for storing memory and session data.

- **Plugin Architecture:** If you want to add more features to **Assistant (Rin)**, you can develop new plugins in the `cac_plugin/` directory. See the sample plugins (`thuc_thi_lenh_he_thong.py`, `thuc_thi_python.py`, `xu_ly_file_plugin.py`) to understand how to build a plugin.

- **Run as Administrator (Windows):** For some plugins (e.g., `thuc_thi_lenh_he_thong.py`) to function most effectively (especially commands requiring admin rights), you should run `rin.py` or `run.bat` with Administrator privileges. Upon startup, Rin will check for administrator rights and automatically request to re-run with admin rights if needed.

</details>

<details>
<summary>🇯🇵 日本語</summary>

## 1. はじめに

**Assistant**（コード名 **Rin**）は、強力な Gemini 大規模言語モデル (Google) を基盤として構築されたオープンソースの個人用仮想アシスタントです。Rin は、ユーザーが日々のタスクを自動化したり、システムと対話したり、ファイルを処理したり、その他多くのことを、ユーザーフレンドリーで直感的なコマンドラインインターフェース（CLI）を通じて行うのを支援するように設計されています。

**Assistant (Rin) プロジェクトの主な目的:**

- **タスクの自動化:** システムコマンドの実行、Python スクリプトの実行、ファイルの編集などの複雑なタスクを、自然言語コマンドを通じて簡単かつ迅速に実行できるようにユーザーを支援します。
- **拡張性:** 柔軟なプラグインアーキテクチャにより、新しい機能の追加が容易になり、多様なユーザーニーズに対応できます。
- **強力な AI の統合:** Gemini を活用して、ユーザーの質問やリクエストをインテリジェントかつ自然に理解し、応答します。
- **オープンソースとカスタマイズ:** プロジェクトのソースコードは公開されており、コミュニティの貢献と、望むように仮想アシスタントを開発するためのカスタマイズを奨励しています。

**Assistant (Rin) は以下を対象としています:**

- **個人ユーザー:** 日常の仕事やエンターテイメントをサポートするための汎用性の高い仮想アシスタントを必要としているユーザー。
- **開発者:** アプリケーションへの AI の統合方法を学びたい、またはオープンソースの仮想アシスタントプロジェクトに貢献したいユーザー。
- **テクノロジー愛好家:** 柔軟で強力な仮想アシスタントを探求し、カスタマイズしたいユーザー。

## 2. 機能

**Assistant (Rin)** は、以下を含む一連の強力な機能を提供します。

- **システムコマンドの実行 (@):** 自然言語コマンドを通じて PowerShell コマンド (Windows 上) を直接実行できます。例: `@デバイスマネージャーを開く`、`@ipconfig /all`。
- **Python コードの実行 ($):** コマンドライン環境で短い Python コードスニペットを作成および実行できます。例: `$ディスク情報を印刷する python コードを記述`、`$Python を使用して 1 から 100 までの数値の合計を計算`。
- **高度なファイル処理 (#):** さまざまなファイルの読み取り、書き込み、編集、コードの修正、およびコードのアップグレードをサポートします。ファイル処理コマンドは `#` で始まり、さまざまなファイルタイプに適用できます。例: `#ファイル "path/to/file.txt" を読み取り`、`#コードファイル "script.py" を修正`。
- **Gemini 統合 (Google AI):** Gemini の力を活用して、自然言語を理解し、システムコマンドを生成し、Python コードを生成し、実行結果を分析し、インテリジェントな評価を提供します。
- **メモリサポート (セッション履歴):** Rin は、現在のセッションで以前のインタラクション (メモリ) から情報を保存する機能を備えており、後続のコマンドでより適切な応答を提供するのに役立ちます。
- **プラグインアーキテクチャ:** プラグインベースのアーキテクチャで設計されており、新しいプラグインを開発することで、新しい機能を追加し、仮想アシスタントの機能を簡単に拡張できます。
- **通知と結果分析:** コマンド実行後、Rin はステータス通知 (成功/エラー)、出力結果、エラー分析 (もしあれば)、および Gemini 2 を使用した結果評価を提供します。
- **動的エフェクトとフレンドリーなインターフェース:** 動的な「思考中」エフェクトを使用して、魅力的なインタラクションエクスペリエンスを作成します。コマンドラインインターフェース（CLI）は、読みやすさと使いやすさを考慮して、色とレイアウトが最適化されています。
- **Windows で実行 (PowerShell 用に最適化):** Rin は主に Windows オペレーティングシステムで実行され、システムコマンドに PowerShell の力を活用するように開発されています。

## 3. プロジェクト構造

```
Assistant/
├── .git/             (Git ディレクトリ - ドキュメントにリストされていません)
├── .gitignore        (Git が無視するファイル/ディレクトリを指定するファイル)
├── Assistant/
├── bieutuong/         (アイコンと画像を含むディレクトリ - ドキュメントにリストされていません)
├── cac_plugin/       (拡張機能プラグインを含むディレクトリ)
│   ├── thuc_thi_lenh_he_thong.py (PowerShell システムコマンド実行プラグイン)
│   ├── thuc_thi_python.py     (Python コード実行プラグイン)
│   ├── xu_ly_file_plugin.py   (高度なファイル処理プラグイン)
│   ├── __init__.py
│   └── __pycache__/         (Python キャッシュディレクトリ - リストされていません)
├── core/              (仮想アシスタントのコアソースコードを含むディレクトリ)
│   ├── chat.py         (Gemini 通信を管理するためのモジュール)
│   ├── __init__.py
│   └── __pycache__/         (Python キャッシュディレクトリ - リストされていません)
├── memory/            (セッションメモリと履歴を保存するためのディレクトリ - リストされていません)
├── README.md
├── rin.py             (メインソースコードファイル、仮想アシスタントを起動)
├── run.bat            (Windows でアプリケーションを簡単に実行するためのバッチスクリプト)
├── utils/             (ユーティリティモジュールを含むディレクトリ)
│   ├── animation/      (動的エフェクトを含むディレクトリ)
│   │   ├── hieu_ung.py  (動的エフェクトモジュール)
│   │   └── __init__.py
│   │   └── __pycache__/     (Python キャッシュディレクトリ - リストされていません)
│   ├── cau_hinh.py     (定数と設定の構成ファイル)
│   ├── nhat_ky.py      (アクティビティログモジュール)
│   ├── rin.bat        (補助バッチスクリプトファイル)
│   ├── __init__.py
│   └── __pycache__/     (Python キャッシュディレクトリ - リストされていません)
├── __init__.py
```

- **`.git/`、`.gitignore`**: ソースコード管理用の Git 関連ファイルおよびディレクトリ。
- **`Assistant/`**: ドキュメントまたはその他のプロジェクトリソースの可能性のあるディレクトリ（現在は空のようです）。
- **`bieutuong/`**: インターフェースに使用されるアイコンファイル、画像、ASCIIアートを含むディレクトリ (カスタマイズ可能)。
- **`cac_plugin/`**: 機能プラグインを含むコアディレクトリ:
    - **`thuc_thi_lenh_he_thong.py`**: システムコマンド（PowerShell）を実行するためのプラグイン。
    - **`thuc_thi_python.py`**: Python コードを直接実行するためのプラグイン。
    - **`xu_ly_file_plugin.py`**: ファイル処理機能（読み取り、書き込み、編集など）を提供するプラグイン。
    - **`__init__.py`**: パッケージの初期化ファイル。これはパッケージであることを Python に伝えます。
- **`core/`**: コアシステムモジュールが含まれています:
    - **`chat.py`**: Gemini API 通信を処理し、チャットセッションを初期化および維持するモジュール。
    - **`__init__.py`**: パッケージの初期化ファイル。
- **`memory/`**: セッションメモリと会話履歴を保存するディレクトリ（Git にコミットされていません）。
- **`README.md`**: この README ファイル。プロジェクトの概要情報を提供します。
- **`rin.py`**: メイン Python ファイル。プログラムのメインループが含まれており、ユーザー入力を処理し、プラグインを呼び出し、Gemini と対話します。
- **`run.bat`**: Windows でアプリケーションを簡単に実行するためのバッチファイル（仮想環境をアクティブにし、`rin.py` を実行します）。
- **`utils/`**: 一般的なユーティリティモジュールが含まれています:
    - **`animation/`**: 動的エフェクトを作成するための `hieu_ung.py` モジュールを含むディレクトリ（例: 「思考中」アニメーション）。
    - **`cau_hinh.py`**: 定数、設定、API キー、色などを設定するための構成ファイル。
    - **`nhat_ky.py`**: プログラムのアクティビティログ（ロギング）を管理するためのモジュール。
    - **`rin.bat`**: 補助バッチスクリプトファイル（例: デバッグまたはテスト目的で使用できます）。
    - **`__init__.py`**: パッケージの初期化ファイル。
- **`__init__.py`** (ルート `Assistant/` ディレクトリ): ルートディレクトリのパッケージ初期化ファイル。

## 4. インストール

### 前提条件

**Assistant (Rin)** をインストールして実行する前に、システムに以下のソフトウェアがインストールされていることを確認してください。

1.  **Python:** Python バージョン 3.8 以降。[https://www.python.org/downloads/](https://www.python.org/downloads/) からダウンロードできます。

2.  **pip:** (Python に付属) Pip は Python のパッケージマネージャーであり、依存ライブラリをインストールするために使用されます。

3.  **Gemini API キー:** Gemini API を使用するには、有効な Gemini API キーが必要です。Google Generative AI のドキュメントを参照して API キーを取得してください。キーを取得したら、`utils/cau_hinh.py` ファイルの `API_KEY` 変数に入力してください。**API キーは安全に保管してください**。

### インストール手順

1. **プロジェクトのダウンロード:** GitHub から **Assistant** プロジェクトのソースコードをクローンまたはダウンロードします。

   ```bash
   git clone https://github.com/Rin1809/System_Assistant
   cd Assistant
   ```

2. **仮想環境の作成 (推奨):** このプロジェクト専用にライブラリを個別に管理するために、仮想環境を作成します。**Assistant** プロジェクトディレクトリで、次のコマンドを実行して `moitruongao` という名前の仮想環境を作成します。

   ```bash
   python -m venv moitruongao
   ```

3. **仮想環境のアクティブ化:**

   - **Windows:** `run.bat` ファイルを実行します。 `run.bat` は仮想環境を自動的にアクティブ化し、アプリケーションを実行します。

     または、コマンドプロンプト/PowerShell で次のコマンドを使用して手動でアクティブ化することもできます。
     ```bash
     moitruongao\Scripts\activate.bat
     ```

   - **macOS/Linux:** ターミナルで次のコマンドを実行します。
     ```bash
     source moitruongao/bin/activate
     ```

4. **ライブラリのインストール:** `requirements.txt` ファイル (プロジェクトに存在する場合) から必要な Python ライブラリをインストールします。それ以外の場合は、手動でインストールします (アクティブ化された仮想環境内):

   ```bash
   pip install -r requirements.txt  # requirements.txt ファイルが存在する場合

   # または requirements.txt が存在しない場合は手動でインストール:
   pip install google-generativeai pygments python-magic python-docx openpyxl rich psutil watchdog wmi
   ```

5. **API キーの設定:** `utils/cau_hinh.py` ファイルを開き、`API_KEY = "YOUR_API_KEY_HERE"` 変数のプレースホルダー値を Gemini API キーに置き換えます。

6. **アプリケーションの実行:**

   - **Windows (推奨):** `run.bat` ファイルを実行します。

   - **任意の OS (仮想環境をアクティブ化した後):** 次のコマンドを実行します。

     ```bash
     python rin.py
     ```

     Rin 仮想アシスタントがコマンドラインで起動します。

## 5. 使用方法

**Assistant (Rin) のコマンドラインインターフェース (CLI):**

`rin.py` または `run.bat` を実行すると、Rin のコマンドラインインターフェースが表示されます。自然言語コマンドを使用して Rin と対話できます。プラグイン機能を呼び出すための特別なプレフィックスを使用します。

- **通常の質問 (プレフィックスなし):** 一般的な質問については、質問を直接入力できます。Rin は Gemini を使用して回答します。例: `今日のハノイの天気は？`、`ベトナムの歴史の概要を説明`。
- **システムコマンドの実行 (プレフィックス `@`):** システムコマンド (Windows 上の PowerShell) を実行するには、コマンドを `@` 文字で開始します。例: `@notepad を開く`、`@ipconfig`。
- **Python コードの実行 (プレフィックス `$`)**: Python コードを実行するには、コマンドを `$` で開始します。例: `$10 の階乗を計算する Python コードを記述`、`$Python で現在の日時を出力`。
- **ファイル処理 (プレフィックス `#`)**: ファイル操作 (読み取り、編集、書き込みなど) を実行するには、プレフィックス `#` を使用します。`#` の後には、コマンドと二重引用符で囲まれたファイルパスが続きます。例: `#ファイル "path/to/my_file.txt" を読み取り`、`#ファイル "script.py" を編集、'old_text' を 'new_text' に置換`。

**一般的なコマンド:**

- **`rin`**: アシスタントの名前を呼んで「ウェイクアップ」または会話を開始します (すべてのコマンドで必要というわけではありません)。
- **`0`**: プログラムを終了するには、数字 `0` を入力して Enter キーを押します。
- **`2`**: 現在のプロセスを中断するには、数字 `2` を入力して Enter キーを押します (もしあれば)。
- **`!` + `[memory_file_name.json]`**: `memory/` ディレクトリに以前に保存された JSON ファイルからメモリをロードします。例: `!Memory_2024-12-28_10-30-45.json`。

**注意:**

- `#` コマンドのファイルパスは二重引用符 (`"`) で囲む必要があります。
- Rin は現在、Windows OS と PowerShell に最適化されています。
- ファイル処理プラグイン (`#`) を使用するには、有効なファイルパスを提供し、Rin にファイルアクセス権があることを確認する必要があります。

## 6. 使用例

以下は、**Assistant (Rin)** をさまざまなタスクに使用する方法を示す使用例です。

**例 1: 天気情報を尋ねる:**

```
[現在時刻] Rin: Me:  ハノイの今日の天気は？

[時間] Rin: Rin:  ☀️ ハノイの天気は今日、晴れていて綺麗ですよ! 気温は20～28℃です。外出時はサングラスをかけるのを忘れないでね!
```

**例 2: システムコマンドを使用してアプリケーションを開く:**

```
[現在時刻] Rin: Me:  @notepad を開く

[時間] Rin: Rin:  [プラグイン: システムコマンドの実行] Rin:

[システムコマンドの実行] ✨ 完了 (0.25秒) ✨
────────────────────────────────────────────────────────────────────────
✅ 実行成功
🔍  分析:
    -  - 結果:

        -   「コマンドは正常に実行されました。メモ帳が起動したはずです。」 (このような1行は15語を超えないようにしてください)
- ➡️ 出力:

    -

エラー:
────────────────────────────────────────────────────────────────────────
```
*(メモ帳がコンピュータ上で開きます)*

**例 3: Python を使用してディスク情報を取得する:**

```
[現在時刻] Rin: Me:  ディスク情報を印刷する python コードを記述

[時間] Rin: Rin:  [プラグイン: Python の実行] Rin:

[Python の実行] ✨ 完了 (1.55秒) ✨
────────────────────────────────────────────────────────────────────────
✅ Python コードが正常に実行されました。
🔍  分析:
    -  - 結果:

        -   「コードはエラーなしで正常に実行されました。」 (このような1行は15語を超えないようにしてください)
        -   「ディスク情報は期待どおりに抽出され、印刷されます。」
💽 ディスク情報:
    - ➡️ ディスク
      ➡️ 説明     ローカル固定ディスク
      ➡️ サイズ    931.51 GB
      ➡️ 空き容量   349.84 GB
      ➡️ ファイルシステム   NTFS
    - ➡️ ディスク   D:
      ➡️ 説明     ローカル固定ディスク
      ➡️ サイズ    1023.96 GB
      ➡️ 空き容量    754.85 GB
      ➡️ ファイルシステム   NTFS
    - ➡️ ディスク   E:
      ➡️ 説明     CD-ROM ディスク
      ➡️ サイズ    0.0 GB
      ➡️ 空き容量    0.0 GB
      ➡️ ファイルシステム   CDFS
    - ➡️ ディスク   F:
      ➡️ 説明     ローカル固定ディスク
      ➡️ サイズ    465.76 GB
      ➡️ 空き容量    444.04 GB
      ➡️ ファイルシステム   NTFS
    - ➡️ ディスク   G:
      ➡️ 説明     ローカル固定ディスク
      ➡️ サイズ    465.76 GB
      ➡️ 空き容量    439.14 GB
      ➡️ ファイルシステム   NTFS
    - ➡️ ディスク   C:
      ➡️ 説明     ローカル固定ディスク
      ➡️ サイズ    476.39 GB
      ➡️ 空き容量    44.47 GB
      ➡️ ファイルシステム   NTFS
────────────────────────────────────────────────────────────────────────
```

**例 4: Python コードファイルの内容を読み取る:**

```
[現在時刻] Rin: Me:  #ファイル "utils/cau_hinh.py" を読み取り

[時間] Rin: Rin:  [プラグイン: ファイル処理] Rin:
[ファイル処理] ✨ 完了 (0.00秒) ✨
────────────────────────────────────────────────────────────────────────
✅ ファイルの読み取りが正常に完了しました
    内容:
    ----------------------------------------
    # utils/cau_hinh.py
    import threading
    import sys
    import codecs
    import os
    import re
    from rich.console import Console
    from rich.table import Table

    # Rin ロック
    PRINT_LOCK = threading.Lock()

    # 色
    PINK1 = "\033[38;2;255;192;203m"
    PLUM2 = "\033[38;2;221;160;221m"
    RICH_PINK = "\033[38;2;255;105;180m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[38;5;226m"  # 薄い黄色の背景
    BLUE = "\033[94m"
    ORANGE = "\033[38;2;255;105;180m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNBOLD = "\033[0m"
    GREEN = "\033[38;5;154m"
    RIN = "\033[38;5;159m"
    TIME = "\033[38;5;231m"
    THISTLE1 = "\033[38;2;255;225;255m"
    DARK_ORANGE = "\033[38;2;255;140;0m"
    MODEL_NAME = "gemini-2.0-flash-exp" # 必要に応じてモデルを変更
    MODEL_NAME2 = "gemini-exp-1206"
    TEMP = 0.7
    TOP_P = 0.95
    TOP_K = 40
    MAX_OUTPUT_TOKENS = 8192 # 減らす == より速く
    API_KEY = "YOUR_API_KEY_HERE"

    SUCCESS = f"{GREEN}✔{RESET}"
    FAIL = f"{RED}❌{RESET}"
    ERROR = f"{RED}⚠{RESET}"

    # メモリ保存パス
    MEMORY_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "memory")

    MEMORY_FILE_FORMAT = "Memory_%Y-%m-%d_%H-%M-%S.json"
    SESSION_FILE_FORMAT = "Session_%Y-%m-%d_%H-%M-%S.json"

    def remove_ansi_escape_codes(text):
        """文字列から ANSI カラーコードを削除します。"""
        return re.sub(r'\x1b\[[0-9;]*[mG]', '', text)

    def format_output(plugin_name, message=None, execution_time=None, content=None, error=None, analysis=None, output=None, code=None, disk_info=None, detailed=True):
        """
        読みやすくするために出力をフォーマットします。
        """
        console = Console()

        detailed が False の場合:
            execution_time が None でない場合:
                console.print(f"[{plugin_name}] ✨ 完了 ({execution_time:.2f}s) ✨")
            message がある場合:
                console.print(f"✅ {message}")
            error がある場合:
                console.print(f"❌ {error}")
            戻り

        table = Table(title=f"[{plugin_name}]")

        table.add_column("フィールド", style="dim", width=20)
        table.add_column("値")

        message がある場合:
            table.add_row("✅ メッセージ", message)
        execution_time が None でない場合:
            table.add_row("✨ 時間", f"{execution_time:.2f}s")
        analysis がある場合:
            table.add_row("🔍 分析", analysis)
        output がある場合:
            table.add_row("➡️ 出力", output)
        content がある場合:
            table.add_row("📄 内容", content)
        code がある場合:
            table.add_row("💻 コード", code)
        disk_info がある場合:
            table.add_row("💽 ディスク情報", "")
            disk 内の disk_info の場合:
                table.add_row("    - ➡️ ドライブ", disk['caption'])
                table.add_row("      ➡️ 説明", disk['description'])
                table.add_row("      ➡️ サイズ", f"{disk['size']} GB")
                table.add_row("      ➡️ 空き容量", f"{disk['free_space']} GB")
                table.add_row("      ➡️ ファイルシステム", disk['file_system'])
        error がある場合:
            table.add_row("❌ エラー", error)

        console.print(table)
    ----------------------------------------
────────────────────────────────────────────────────────────────────────
```

**例 5: テキストファイルの編集 (テキストの置換):**

```
[現在時刻] Rin: Me:  #ファイル "example.txt" を編集し、"old text" を "new text" に置換

[時間] Rin: Rin:  [プラグイン: ファイル処理] Rin:
[ファイル処理] ✨ 完了 (0.01秒) ✨
────────────────────────────────────────────────────────────────────────
✅ ファイルの編集が正常に完了しました
    コード:
    ----------------------------------------
    変更なし
    ----------------------------------------
────────────────────────────────────────────────────────────────────────
```
*(ファイル `example.txt` が編集されます。もし "old text" が存在すれば、"new text" に置換されます)*

**さらに詳しく調べる:**

さまざまなコマンドを試したり、機能を組み合わせたり、プラグインをカスタマイズしたりして、**Assistant (Rin)** の全容を探ってみてください。

## 7. 高度な設定

- **設定ファイル `utils/cau_hinh.py`:** このファイルには、重要な構成が含まれています:
    - `API_KEY`:  **必須**、Gemini API キーに置き換える必要があります。
    - `MODEL_NAME`、`MODEL_NAME2`: 使用される Gemini モデルの名前。他のモデルを試すために変更できます。
    - `TEMP`、`TOP_P`、`TOP_K`、`MAX_OUTPUT_TOKENS`: Gemini モデルの構成パラメータ。これらをカスタマイズして、Gemini の創造性、精度、応答速度を調整できます。
    - カラー変数: `PINK1`、`RED`、`GREEN`、`YELLOW` など: コマンドラインインターフェースをカスタマイズするための ANSI カラーコード。
    - `MEMORY_DIR`、`MEMORY_FILE_FORMAT`、`SESSION_FILE_FORMAT`: メモリとセッションデータを保存するためのパスとファイル形式。

- **プラグインアーキテクチャ:** **Assistant (Rin)** にさらに機能を追加したい場合は、`cac_plugin/` ディレクトリに新しいプラグインを開発できます。プラグインの構築方法を理解するには、サンプルプラグイン (`thuc_thi_lenh_he_thong.py`、`thuc_thi_python.py`、`xu_ly_file_plugin.py`) を参照してください。

- **管理者として実行 (Windows):** 一部のプラグイン (例: `thuc_thi_lenh_he_thong.py`) を最大限に効果的に機能させる (特に管理者権限を必要とするコマンド) には、`rin.py` または `run.bat` を管理者権限で実行する必要があります。起動時に、Rin は管理者権限を確認し、必要に応じて管理者権限で再実行するように自動的に要求します。

</details>
