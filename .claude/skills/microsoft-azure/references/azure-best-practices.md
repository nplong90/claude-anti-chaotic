# Azure Best Practices

Các nguyên tắc và mẹo tối ưu hóa khi sử dụng Microsoft Azure.

## 1. Quản lý Tài nguyên & Quản trị (Governance)
- **Resource Groups**: Nhóm các tài nguyên có cùng vòng đời vào một Resource Group để dễ dàng quản lý và xóa bỏ.
- **Tagging**: Sử dụng Tags để phân loại tài nguyên theo bộ phận (Department), môi trường (Environment), hoặc dự án (Project) để theo dõi chi phí.
- **Azure Policy**: Áp dụng các chính sách để đảm bảo tính tuân thủ (ví dụ: chỉ cho phép tạo tài nguyên ở region Đông Nam Á).

## 2. Bảo mật (Security)
- **Entra ID (Azure AD)**: Sử dụng Role-Based Access Control (RBAC) để cấp quyền tối thiểu. Tuyệt đối không chia sẻ tài khoản cá nhân.
- **Managed Identities**: Sử dụng Managed Identities để các dịch vụ Azure (như App Service) truy cập Key Vault mà không cần lưu trữ credentials trong code.
- **Key Vault**: Lưu trữ tất cả secrets, certificates và keys trong Azure Key Vault.

## 3. Tối ưu hóa Chi phí (Cost Management)
- **Azure Advisor**: Thường xuyên kiểm tra Azure Advisor để nhận các đề xuất về giảm chi phí và tăng hiệu năng.
- **Reserved Instances**: Sử dụng Reserved Instances cho các server chạy liên tục trong 1-3 năm để tiết kiệm tới 72%.
- **Auto-scaling**: Cấu hình tự động tăng/giảm scale để chỉ trả phí cho những gì thực sự sử dụng.

## 4. Hiệu suất & Sẵn sàng (Performance & Availability)
- **Availability Sets/Zones**: Sử dụng Availability Zones để bảo vệ ứng dụng khỏi lỗi trung tâm dữ liệu.
- **Azure Front Door / Traffic Manager**: Sử dụng để điều hướng lưu lượng toàn cầu và tăng tốc độ truy cập.
- **Caching**: Tận dụng Azure Cache for Redis để giảm tải cho cơ sở dữ liệu.

## 5. Vận hành & Tự động hóa
- **Bicep / Terraform**: Ưu tiên sử dụng Infrastructure as Code (IaC) để triển khai hạ tầng nhất quán.
- **Azure Monitor & App Insights**: Tích hợp Application Insights để theo dõi chi tiết hiệu năng ứng dụng và logs.
- **Deployment Slots**: Sử dụng Deployment Slots trong App Service để thực hiện Zero-downtime deployment (Blue/Green deployment).
