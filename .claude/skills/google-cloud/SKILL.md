---
name: google-cloud
description: Chuyên gia về Google Cloud Platform (GCP). Cung cấp kiến thức và hướng dẫn triển khai Cloud Run, GKE, Cloud Functions, BigQuery, và Cloud Storage. Sử dụng khi thiết kế kiến trúc hệ thống trên GCP, tối ưu hóa chi phí cloud, hoặc tự động hóa hạ tầng với gcloud CLI.
license: MIT
version: 1.0.0
---

# Google Cloud Platform (GCP) Skill

Hướng dẫn toàn diện về việc triển khai và quản lý hạ tầng trên Google Cloud Platform.

## Các dịch vụ trọng tâm

### 1. Compute & Serverless
- **Cloud Run**: Triển khai các containerized applications theo mô hình serverless.
- **Google Kubernetes Engine (GKE)**: Quản lý cụm Kubernetes ở quy mô doanh nghiệp.
- **Cloud Functions**: Chạy các hàm sự kiện (event-driven) mà không cần quản lý server.
- **Compute Engine**: Máy ảo (VMs) tùy chỉnh linh hoạt.

### 2. Storage & Databases
- **Cloud Storage**: Lưu trữ đối tượng (Object storage) quy mô lớn.
- **Cloud SQL**: Cơ sở dữ liệu quan hệ (MySQL, PostgreSQL, SQL Server) được quản lý hoàn toàn.
- **Firestore**: Cơ sở dữ liệu NoSQL linh hoạt, mở rộng cao.
- **BigQuery**: Kho dữ liệu (Data warehouse) phân tích quy mô petabyte.

### 3. Networking & Security
- **Cloud Load Balancing**: Phân phối lưu lượng toàn cầu.
- **Cloud IAM**: Quản lý quyền truy cập chi tiết.
- **Secret Manager**: Lưu trữ và quản lý các thông tin nhạy cảm (API keys, passwords).

## Khi nào nên sử dụng Skill này

- Khi cần container hóa ứng dụng và chạy trên **Cloud Run**.
- Khi cần thiết lập các luồng xử lý dữ liệu với **BigQuery** và **Pub/Sub**.
- Khi cần cấu hình bảo mật với **IAM Roles** và **Service Accounts**.
- Khi muốn tự động hóa việc tạo tài nguyên bằng **gcloud CLI** hoặc **Terraform**.

## Lệnh gcloud CLI cơ bản

```bash
# Đăng nhập và chọn project
gcloud auth login
gcloud config set project [PROJECT_ID]

# Triển khai lên Cloud Run
gcloud run deploy [SERVICE_NAME] --source .

# Quản lý Cloud Storage
gsutil mb gs://[BUCKET_NAME]
gsutil cp [FILE_PATH] gs://[BUCKET_NAME]/
```

## Tài liệu tham khảo
- `references/gcloud-cheatsheet.md`: Danh sách các lệnh gcloud thường dùng.
- `references/gcp-best-practices.md`: Các quy tắc tối ưu chi phí và bảo mật.

---
*Duy trì bởi Claude Anti-Chaotic Team*
