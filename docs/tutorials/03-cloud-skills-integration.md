# Tutorial 03: Tích hợp Cloud Skills vào Workflow

Trong các bài trước, chúng ta đã tìm hiểu về cách hoạt động của Agent và cách tạo mới chúng. Bài này sẽ hướng dẫn bạn cách sử dụng các **Skills** (đặc biệt là Cloud Skills như GCP, Cloudflare) để tự động hóa việc triển khai hạ tầng.

## 1. Skill là gì?

**Skill** là một tập hợp kiến thức chuyên sâu và các script hỗ trợ được đóng gói để các Agent có thể sử dụng. Ví dụ, khi bạn yêu cầu triển khai ứng dụng, Agent sẽ "triệu hồi" Skill `google-cloud` để biết cách dùng lệnh `gcloud` chính xác nhất.

## 2. Cách Agent sử dụng Cloud Skill

Quy trình diễn ra như sau:
1. **Yêu cầu**: Bạn nhập `/cook "Triển khai backend lên Cloud Run"`.
2. **Kích hoạt**: Agent **Planner** nhận thấy từ khóa "Cloud Run" và sẽ kích hoạt Skill `google-cloud`.
3. **Tham chiếu**: Agent đọc các file trong `skills/google-cloud/references/` để lấy các best practices (như bảo mật IAM, chọn region).
4. **Thực thi**: Agent tạo ra các lệnh bash dựa trên hướng dẫn trong Skill và thực hiện chúng.

## 3. Thực hành: Triển khai ứng dụng đầu tiên

Để triển khai ứng dụng lên Google Cloud bằng hệ thống này, bạn có thể thực hiện theo các bước:

### Bước 1: Chuẩn bị môi trường
Đảm bảo bạn đã cài đặt `gcloud` CLI và đăng nhập:
```bash
gcloud auth login
```

### Bước 2: Sử dụng lệnh /cook
Chạy lệnh sau để AI tự động cấu hình và triển khai:
```bash
/cook "Cấu hình Dockerfile và deploy lên Cloud Run region asia-southeast1"
```

Hệ thống sẽ:
- Dùng Skill `devops` để tạo Dockerfile chuẩn.
- Dùng Skill `google-cloud` để chạy lệnh deploy.

## 4. Tùy chỉnh Cloud Skill của bạn

Bạn có thể thêm các script tự động hóa riêng vào thư mục `skills/google-cloud/scripts/`. Ví dụ:
- Script kiểm tra chi phí trước khi deploy.
- Script tự động dọn dẹp các bản build cũ.

Mỗi khi bạn thêm một script mới, hãy cập nhật file `SKILL.md` để Agent biết cách sử dụng nó.

---
*Quay lại: [Hướng dẫn 02: Tùy chỉnh Custom Agent](02-custom-agent-creation.md)*
