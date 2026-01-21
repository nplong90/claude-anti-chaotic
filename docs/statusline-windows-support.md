# Windows Statusline Support Guide

Tài liệu này hướng dẫn cách thiết lập và sử dụng tính năng Statusline của Claude Code trên môi trường Windows.

## Tổng quan

Claude Anti-Chaotic cung cấp giải pháp cross-platform để hiển thị trạng thái của Claude (model, session cost, tokens, git branch) ngay trên terminal Windows thông qua PowerShell hoặc Node.js.

## 4 Tùy chọn thiết lập (Setup Options)

### Cách 1: PowerShell Native (Khuyên dùng cho PowerShell 5.1/7+)
Thêm dòng sau vào file `$PROFILE` của bạn:
```powershell
. "$PSScriptRoot\.claude\statusline.ps1"
```

### Cách 2: Node.js Universal Fallback
Sử dụng nếu bạn muốn hiệu suất nhanh nhất hoặc đang dùng terminal không hỗ trợ PowerShell:
```bash
node .claude/statusline.js
```

### Cách 3: Git Bash Integration
Thêm vào file `~/.bashrc`:
```bash
source .claude/statusline.sh
```

### Cách 4: WSL (Windows Subsystem for Linux)
WSL hoạt động như môi trường Linux thuần túy, bạn có thể dùng trực tiếp bản `.sh`.

## Các tính năng hỗ trợ

- ✅ Hiển thị Git Branch hiện tại.
- ✅ Theo dõi chi phí Session (Cost) và lượng Token tiêu thụ.
- ✅ Hiển thị Model đang sử dụng (Sonnet, Opus, etc.).
- ✅ Hỗ trợ màu sắc ANSI (tương thích với NO_COLOR).
- ✅ Tích hợp `ccusage` để đo lường metrics.

## Xử lý sự cố (Common Issues)

1. **Lỗi Font chữ/Emoji**: Đảm bảo terminal của bạn hỗ trợ UTF-8 (Khuyên dùng Windows Terminal).
2. **Lỗi Execution Policy**: Chạy `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.
3. **Hiệu suất chậm**: Bản Node.js (`statusline.js`) thường nhanh hơn bản PowerShell trên máy cấu hình thấp.

---
*Duy trì bởi Claude Anti-Chaotic Team*
