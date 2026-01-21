# Google Cloud Best Practices

Các quy tắc và mẹo để tối ưu hóa việc sử dụng Google Cloud Platform trong dự án.

## 1. Quản lý Quyền truy cập (IAM)
- **Quyền tối thiểu (Least Privilege)**: Luôn cấp quyền hẹp nhất có thể cho Service Account. Không sử dụng quyền `Owner` cho các ứng dụng.
- **Service Accounts riêng biệt**: Sử dụng mỗi Service Account cho một dịch vụ hoặc chức năng riêng để dễ dàng thu hồi và kiểm soát.
- **Sử dụng Workload Identity**: Khi chạy trên GKE, hãy dùng Workload Identity thay vì lưu file JSON key của Service Account trong container.

## 2. Tối ưu hóa Chi phí
- **Tận dụng Cloud Run**: Sử dụng Cloud Run cho các ứng dụng có lưu lượng không ổn định để tận dụng tính năng "scale to zero" (không chạy không tốn tiền).
- **Vòng đời dữ liệu (Storage Lifecycle)**: Thiết lập quy tắc tự động chuyển dữ liệu cũ sang Nearline hoặc Coldline storage trên Cloud Storage.
- **Cleanup**: Tự động xóa các đĩa đệm (disks) không gắn vào VM và các địa chỉ IP tĩnh không sử dụng.

## 3. Bảo mật Dữ liệu
- **Secret Manager**: Tuyệt đối không lưu API Key, Database Password trong biến môi trường `.env` hoặc trong code. Hãy dùng Secret Manager.
- **Mã hóa**: GCP tự động mã hóa dữ liệu ở trạng thái nghỉ (at rest). Nếu cần kiểm soát cao hơn, hãy sử dụng Cloud KMS.

## 4. Hiệu suất và Khả dụng
- **Vùng (Regions)**: Chọn region gần với người dùng nhất (ví dụ: `asia-southeast1` ở Singapore cho người dùng Việt Nam).
- **Health Checks**: Luôn cấu hình Health Checks cho Cloud Run và Load Balancer để hệ thống tự động loại bỏ các instance bị lỗi.

## 5. Tự động hóa
- **Infrastucture as Code (IaC)**: Sử dụng Terraform hoặc Google Cloud Deployment Manager để quản lý hạ tầng thay vì tạo thủ công trên Console.
- **CI/CD**: Tích hợp gcloud CLI vào quy trình GitHub Actions để tự động deploy khi có code mới.
