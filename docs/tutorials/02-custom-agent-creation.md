# Tutorial 02: Tùy chỉnh Custom Agent

Hệ thống của chúng ta cho phép bạn định nghĩa các AI Agent riêng biệt để phục vụ nhu cầu cụ thể của từng dự án. Tất cả cấu hình agent nằm trong thư mục `.claude/agents/` hoặc `.opencode/agent/`.

## 1. Cấu trúc của một Agent File

Một agent được định nghĩa dưới dạng file Markdown (.md) với phần Frontmatter (YAML) ở trên đầu.

### Ví dụ về file `my-expert.md`:
```markdown
---
name: MyExpert
description: Một chuyên gia về giải thuật và tối ưu hóa
tools: [Bash, Read, Grep, Edit]
---

# MyExpert Agent Instructions

Bạn là một chuyên gia về giải thuật. Nhiệm vụ của bạn là:
1. Phân tích độ phức tạp thời gian của code.
2. Đề xuất các giải thuật tối ưu hơn.
3. Luôn ưu tiên giải pháp tiết kiệm bộ nhớ.
```

## 2. Các thành phần quan trọng

- **name**: Tên định danh của agent.
- **description**: Mô tả ngắn gọn để Claude biết khi nào cần dùng agent này.
- **tools**: Danh sách các công cụ mà agent được phép sử dụng.
- **Instructions**: Phần nội dung Markdown bên dưới là "tính cách" và "quy tắc" của agent.

## 3. Cách sử dụng Agent mới

Sau khi tạo file trong thư mục `.claude/agents/`, bạn có thể gọi agent này thông qua lệnh `/ask` hoặc tích hợp vào các workflow phức tạp.

Ví dụ, nếu bạn muốn dùng `MyExpert` để review code:
```bash
/ask MyExpert "Hãy phân tích và tối ưu hóa hàm calculateInterest trong file src/finance.ts"
```

## 4. Best Practices khi tạo Agent

1. **Focus**: Mỗi agent chỉ nên làm tốt một việc duy nhất (Single Responsibility).
2. **Context**: Cung cấp cho agent các ví dụ về "Good output" và "Bad output".
3. **Safety**: Chỉ cấp các công cụ (tools) thực sự cần thiết để tránh agent thực hiện các hành động không mong muốn.

---
*Quay lại: [Hướng dẫn 01: Cơ bản về Agent Orchestration](01-agent-orchestration-basics.md)*
