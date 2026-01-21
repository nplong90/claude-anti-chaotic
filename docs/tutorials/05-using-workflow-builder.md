# Tutorial 05: Sử dụng Workflow Builder

Hệ thống cung cấp một công cụ mạnh mẽ giúp bạn tự thiết kế các lệnh (Slash Commands) phối hợp Agent mới mà không cần phải viết code hay cấu hình Markdown thủ công.

## 1. Workflow Builder là gì?

**Workflow Builder** là một trình thuật sĩ (Wizard) chạy trên dòng lệnh. Nó cho phép bạn:
- Định nghĩa tên lệnh mới (ví dụ: `/deploy-prod`, `/audit-security`).
- Lựa chọn các Agent tham gia vào quy trình từ danh sách có sẵn.
- Thiết lập quy trình chạy nối tiếp (Sequential) hoặc song song (Parallel).

## 2. Cách sử dụng

Để bắt đầu tạo quy trình mới, hãy chạy script sau:

```bash
python scripts/workflow-builder.py
```

### Các bước thực hiện trong Wizard:

1.  **Tên lệnh**: Nhập tên lệnh bạn muốn dùng (viết thường, không dấu cách).
2.  **Mô tả**: Nhập mục đích của lệnh để AI hiểu khi nào cần gợi ý lệnh này.
3.  **Chọn Agent**: Nhập số thứ tự của các Agent bạn muốn phối hợp (ví dụ: `1,12,7` để chọn Planner, Researcher và Tester).
4.  **Kiểu phối hợp**:
    - **Sequential**: Agent A làm xong mới đến Agent B. Phù hợp cho luồng logic phụ thuộc nhau.
    - **Parallel**: Tất cả Agent cùng chạy một lúc. Phù hợp cho việc nghiên cứu hoặc kiểm tra đa luồng để tiết kiệm thời gian.

## 3. Kết quả

Sau khi hoàn tất, script sẽ tự động tạo một file cấu hình tại:
`.claude/commands/custom/[tên-lệnh].md`

Bây giờ, bạn có thể sử dụng lệnh mới ngay lập tức trong Claude Code:
```bash
/[tên-lệnh] "nhiệm vụ của bạn ở đây"
```

## 4. Mẹo nâng cao

- Bạn có thể mở file `.md` vừa tạo để tinh chỉnh thêm các câu lệnh prompt cụ thể cho từng Agent.
- Kết hợp các Agent chuyên biệt (như `ui-ux-designer` và `code-reviewer`) để tạo ra các quy trình kiểm soát chất lượng giao diện tự động.

---
*Quay lại: [Hướng dẫn 04: Quy trình Debug chuyên sâu](04-debugging-and-fixing-workflow.md)*
