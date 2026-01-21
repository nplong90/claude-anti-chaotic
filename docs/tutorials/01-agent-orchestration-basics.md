# Tutorial 01: Agent Orchestration Basics

Chào mừng bạn đến với hướng dẫn sử dụng hệ thống AI Agent của Claude Anti-Chaotic. Tài liệu này sẽ hướng dẫn bạn cách phối hợp các Agent chuyên biệt để phát triển phần mềm chuyên nghiệp.

## 1. Khái niệm về Agent Orchestration

Thay vì chỉ hỏi AI những câu hỏi rời rạc, **Orchestration** (Sự phối dàn) cho phép nhiều Agent cùng làm việc theo một quy trình (workflow) định sẵn. Mỗi Agent đóng một vai trò khác nhau như một thành viên trong team dev:

- **Planner**: Kiến trúc sư, người lên kế hoạch.
- **Researcher**: Người tìm kiếm công nghệ và giải pháp.
- **Cook (Developer)**: Người viết code dựa trên plan.
- **Tester**: Kiểm thử viên.
- **Code Reviewer**: Người soát lỗi và đảm bảo chất lượng.

## 2. Quy trình "Phát triển Tính năng" (Feature Development)

Đây là quy trình phổ biến nhất bạn sẽ sử dụng.

### Bước 1: Lên kế hoạch với `/plan`
Khi bạn có ý tưởng mới, đừng viết code ngay. Hãy dùng:
```bash
/plan "Thêm tính năng đăng nhập bằng Google OAuth2"
```
Agent **Planner** sẽ phối hợp với **Researcher** để tạo ra một file kế hoạch chi tiết trong thư mục `docs/plans/` (nếu có) hoặc hiển thị trực tiếp.

### Bước 2: Thực hiện với `/cook`
Sau khi đã có kế hoạch và bạn đồng ý, hãy ra lệnh:
```bash
/cook "Triển khai tính năng đăng nhập Google"
```
Agent **Cook** sẽ tự động thực hiện các bước trong plan, từ tạo file đến cài đặt thư viện.

### Bước 3: Kiểm tra với `/test`
Đảm bảo tính năng hoạt động đúng:
```bash
/test
```
Agent **Tester** sẽ chạy các bộ test hiện có hoặc tạo mới nếu cần.

### Bước 4: Review và Đóng gói với `/review` và `/git:cp`
Cuối cùng, dùng `/review` để kiểm tra chất lượng code và `/git:cp` để commit và push lên GitHub một cách chuyên nghiệp.

## 3. Các quy trình khác

- **Fixing Bug**: `/debug` -> `/fix:hard` -> `/test`.
- **Documentation**: `/docs:update` để đồng bộ tài liệu với code vừa viết.
- **Project Health**: `/watzup` để xem hôm nay các Agent đã làm được những gì.

---
*Tiếp theo: [Hướng dẫn 02: Tùy chỉnh Custom Agent](02-custom-agent-creation.md)*
