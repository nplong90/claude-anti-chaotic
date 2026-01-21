# Statusline Technical Architecture

Tài liệu này mô tả kiến trúc kỹ thuật của hệ thống Statusline đa nền tảng trong Claude Anti-Chaotic.

## Thiết kế hệ thống

Hệ thống Statusline được thiết kế để cung cấp thông tin thời gian thực về phiên làm việc của Claude Code với độ trễ thấp nhất có thể.

### Các thành phần chính

1.  **Statusline Dispatcher (`statusline.sh/.ps1`)**:
    *   Chịu trách nhiệm phát hiện hệ điều hành và shell hiện tại.
    *   Gọi script thực thi phù hợp (PowerShell trên Windows, Bash trên Linux/macOS).

2.  **PowerShell Engine (`statusline.ps1`)**:
    *   Sử dụng các object native của .NET để tối ưu hiệu suất trên Windows.
    *   Xử lý mã hóa UTF-8 và ANSI colors cho Windows Terminal.

3.  **Node.js Fallback (`statusline.js`)**:
    *   Script vạn năng có thể chạy trên mọi môi trường có Node.js.
    *   Được tối ưu để giảm thời gian khởi động (cold start < 100ms).

4.  **Integration Hooks**:
    *   Kết nối với dữ liệu từ Claude Code CLI (thông qua session files hoặc môi trường).
    *   Tích hợp công cụ `ccusage` để lấy thông tin chi phí chính xác.

## Luồng dữ liệu (Data Flow)

```
Claude CLI -> Session State -> Statusline Scripts -> Terminal Prompt
```

1.  **Claude CLI** cập nhật trạng thái phiên vào một file tạm hoặc biến môi trường.
2.  **Statusline Script** được kích hoạt mỗi khi terminal hiển thị prompt mới.
3.  Script đọc dữ liệu, tính toán metrics (token/sec, cost).
4.  Script format chuỗi ký tự ANSI và in ra màn hình.

## Tối ưu hóa hiệu suất (Performance)

- **PowerShell**: Sử dụng `Write-Host` và các kỹ thuật string building nhanh để đạt tốc độ ~150ms.
- **Node.js**: Tránh require các thư viện nặng, sử dụng native modules để đạt tốc độ ~50-100ms.
- **Caching**: Các thông tin ít thay đổi (như Git branch) được cache ngắn hạn để giảm I/O.

## Khả năng mở rộng

Kiến trúc cho phép dễ dàng thêm các module hiển thị mới như:
- Tình trạng CI/CD pipeline.
- Trạng thái Docker containers.
- Thông tin từ các MCP servers đang chạy.

---
*Duy trì bởi Claude Anti-Chaotic Team*
