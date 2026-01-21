# Tutorial 06: Tạo Custom Agent với Creator CLI

Bên cạnh việc phối hợp các Agent có sẵn, bạn có thể dễ dàng tạo ra những Agent "chuyên gia" mới cho riêng dự án của mình bằng công cụ **Custom Agent Creator**.

## 1. Tại sao cần tạo Agent mới?

Mỗi dự án có những yêu cầu đặc thù. Việc tạo một Agent chuyên biệt giúp AI tập trung vào đúng chuyên môn, ví dụ:
- **Security Agent**: Chỉ tập trung vào quét lỗ hổng bảo mật.
- **Copywriter Agent**: Chuyên viết nội dung marketing hoặc thông báo release.
- **Legacy Code Expert**: Chuyên xử lý các đoạn mã cũ tốn nhiều thời gian.

## 2. Cách sử dụng

Chạy lệnh sau trên terminal:

```bash
python scripts/agent-creator.py
```

### Quy trình thiết lập:

1.  **Tên Agent**: Đặt tên gợi nhớ (ví dụ: `performance-expert`).
2.  **Mô tả**: Viết mục đích để Claude biết khi nào nên gọi Agent này.
3.  **Chọn Model**:
    - Dùng **Sonnet** cho các tác vụ code thông thường.
    - Dùng **Haiku** cho các tác vụ nhanh/đơn giản.
    - Dùng **Opus** cho các phân tích logic cực kỳ phức tạp.
4.  **Chọn Công cụ (Tools)**: Chỉ cấp những quyền cần thiết (ví dụ: chỉ cấp `Read` và `Grep` nếu Agent chỉ làm nhiệm vụ tra cứu).
5.  **Instructions**: Nhập các quy tắc "vàng" mà Agent phải tuân theo.

## 3. Triệu hồi Agent mới

Sau khi tạo xong, Agent sẽ xuất hiện trong thư mục `.claude/agents/`. Bạn có thể sử dụng ngay bằng lệnh:

```bash
/ask [tên-agent] "yêu cầu của bạn"
```

Hoặc tích hợp Agent này vào một Workflow mới bằng công cụ `workflow-builder.py`.

## 4. Lưu ý quan trọng

- **Single Responsibility**: Đừng tạo một Agent làm quá nhiều việc. Càng chuyên biệt, AI càng hoạt động hiệu quả.
- **Safety**: Hạn chế cấp quyền `Bash` hoặc `Edit` cho các Agent thực hiện các nhiệm vụ nghiên cứu thuần túy để tránh rủi ro thay đổi code ngoài ý muốn.

---
*Quay lại: [Hướng dẫn 05: Sử dụng Workflow Builder](05-using-workflow-builder.md)*
