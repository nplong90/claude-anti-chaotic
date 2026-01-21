# Optimization Strategies

Tài liệu này hướng dẫn các kỹ thuật tối ưu hóa hiệu suất và chi phí (Token usage) khi sử dụng hệ thống Claude Anti-Chaotic.

## 1. Chiến lược Caching (Bộ nhớ đệm)

Caching giúp Agent không phải đọc lại các dữ liệu lớn hoặc thực hiện lại các phân tích tốn kém.

### 1.1. Codebase Summary Caching
- **Vấn đề**: File `repomix-output.xml` có thể rất lớn (hàng chục nghìn token). Việc nạp file này vào mỗi session rất tốn kém.
- **Giải pháp**:
  - Chỉ chạy lệnh `/docs:summarize` (hoặc repomix) khi có thay đổi lớn về cấu trúc thư mục.
  - Sử dụng file `docs/codebase-summary.md` làm "Cache" ngữ cảnh chính cho Agent thay vì nạp toàn bộ mã nguồn.

### 1.2. Research Caching
- Trước khi thực hiện một nghiên cứu mới (`/ask` hoặc `/cook`), Agent sẽ kiểm tra thư mục `./plans/<plan-name>/research/`.
- Nếu thông tin đã tồn tại và còn hiệu lực (< 7 ngày), Agent sẽ kế thừa thay vì gọi API tìm kiếm lại.

## 2. Tối ưu hóa Token (Token Optimization)

### 2.1. Phân tầng ngữ cảnh (Context Layering)
Agent được cấu hình để nạp ngữ cảnh theo mức độ ưu tiên:
1.  **Mức 1 (Siêu nhẹ)**: `CLAUDE.md` và `docs/codebase-summary.md`.
2.  **Mức 2 (Trung bình)**: Các file báo cáo nhiệm vụ liên quan trong `./plans/`.
3.  **Mức 3 (Chi tiết)**: Chỉ đọc code của các file cụ thể cần chỉnh sửa (sử dụng tool `Read` với `offset` và `limit`).

### 2.2. Kỹ thuật "Prompt Compression"
- Loại bỏ các câu chữ thừa thãi trong báo cáo giữa các Agent.
- Ưu tiên định dạng Markdown tối giản: sử dụng bảng, danh sách thay vì đoạn văn dài.
- Quy tắc: "Sacrifice grammar for concision" (Hy sinh ngữ pháp để đổi lấy sự súc tích).

## 3. Tối ưu hóa thực thi (Execution Speed)

### 3.1. Parallel Spawning (Triệu hồi song song)
- Tận dụng khả năng chạy song song của các Sub-agents (ví dụ: nhiều Researcher tìm kiếm các mảng khác nhau cùng lúc).
- Giảm thời gian chờ đợi tổng thể của một quy trình phức tạp.

### 3.2. Scout Block Hook
- Tự động chặn Agent truy cập vào các thư mục "nặng" nhưng không chứa logic (như `node_modules`, `.git`, `dist`).
- Tránh việc Agent bị "sa lầy" vào việc đọc hàng triệu dòng code thư viện không cần thiết.

---
*Duy trì bởi Claude Anti-Chaotic Team - Cập nhật lần cuối: 2026-01-21*
