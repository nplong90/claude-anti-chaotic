# Tutorial 04: Quy trình Debug và Fix bug chuyên sâu

Hệ thống AI Agent của chúng ta được thiết kế để không chỉ sửa lỗi mà còn tìm ra nguyên nhân gốc rễ (Root Cause) để ngăn chặn lỗi tái diễn. Bài này hướng dẫn bạn cách phối hợp các Agent trong quy trình xử lý lỗi.

## 1. Các Agent tham gia

- **Debugger**: Chuyên gia thám tử. Phân tích logs, tái hiện lỗi và tìm nguyên nhân gốc rễ.
- **Fixer (Main Agent)**: Người thực hiện sửa đổi mã nguồn.
- **Tester**: Xác nhận lỗi đã được sửa và không gây ra lỗi mới (regression).

## 2. Quy trình 4 bước xử lý lỗi

### Bước 1: Phân tích với `/debug`
Khi gặp lỗi, hãy dùng lệnh:
```bash
/debug "Lỗi 500 khi người dùng nhấn thanh toán"
```
Agent **Debugger** sẽ:
1. Đọc logs hệ thống.
2. Kiểm tra các file liên quan.
3. Giải thích *tại sao* lỗi xảy ra.

### Bước 2: Lên phương án sửa lỗi
Sau khi Debugger báo cáo, hãy dùng:
```bash
/plan "Sửa lỗi thanh toán dựa trên phân tích của Debugger"
```
Agent **Planner** sẽ tạo ra các bước sửa lỗi an toàn, bao gồm cả việc thêm các đoạn code kiểm tra (validation).

### Bước 3: Sửa lỗi với các lệnh `/fix:*`
Tùy vào độ khó, bạn có thể chọn:
- `/fix:fast`: Cho các lỗi hiển nhiên (typo, thiếu import).
- `/fix:hard`: Cho các lỗi logic phức tạp cần nhiều Agent cùng xử lý.
- `/fix:types`: Riêng cho lỗi TypeScript/Type mapping.

### Bước 4: Kiểm thử bắt buộc
Không bao giờ đóng task bug mà chưa chạy:
```bash
/test
```
Agent **Tester** sẽ chạy lại kịch bản gây lỗi trước đó để đảm bảo nó đã biến mất.

## 3. Mẹo nâng cao: Fix lỗi CI/CD

Nếu dự án của bạn bị fail trên GitHub Actions, bạn có thể copy link log và dùng:
```bash
/fix:ci [URL_LOG_GITHUB]
```
Agent sẽ tự động đọc log từ xa, phân tích lý do fail (do môi trường, do test, hay do build) và đề xuất lệnh sửa ngay lập tức.

## 4. Ghi chép bài học

Sau khi fix xong, hãy dùng:
```bash
/journal
```
Việc ghi lại "Tại sao lỗi xảy ra" vào Journal giúp các Agent khác (và cả bạn) có thêm kinh nghiệm để tránh các lỗi tương tự trong tương lai.

---
*Quay lại: [Hướng dẫn 03: Tích hợp Cloud Skills](03-cloud-skills-integration.md)*
