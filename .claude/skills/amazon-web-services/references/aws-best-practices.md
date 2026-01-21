# AWS Best Practices

Các nguyên tắc và mẹo tối ưu hóa khi sử dụng Amazon Web Services.

## 1. Security (Bảo mật) - Ưu tiên hàng đầu
- **Least Privilege**: Luôn sử dụng IAM Roles và Policies với quyền tối thiểu. Không bao giờ sử dụng tài khoản Root cho các tác vụ hàng ngày.
- **MFA**: Kích hoạt Multi-Factor Authentication cho tất cả người dùng IAM và tài khoản Root.
- **Secrets Management**: Sử dụng AWS Secrets Manager hoặc Parameter Store thay vì lưu credentials trong biến môi trường hoặc file config.
- **VPC Isolation**: Đặt các tài nguyên nhạy cảm (DB, Private API) trong Private Subnets và sử dụng NAT Gateway.

## 2. Cost Optimization (Tối ưu chi phí)
- **Right-sizing**: Chọn loại instance (EC2, RDS) phù hợp với tải thực tế. Sử dụng Compute Optimizer để nhận đề xuất.
- **Spot Instances**: Sử dụng Spot Instances cho các tác vụ không yêu cầu tính liên tục cao để tiết kiệm tới 90% chi phí.
- **S3 Lifecycle**: Thiết lập quy tắc tự động chuyển dữ liệu sang S3 Glacier để lưu trữ lâu dài với chi phí thấp.
- **AWS Budgets**: Thiết lập cảnh báo ngân sách để tránh các hóa đơn bất ngờ.

## 3. Reliability (Độ tin cậy)
- **Multi-AZ**: Triển khai ứng dụng trên nhiều Availability Zones để đảm bảo tính sẵn sàng cao.
- **Auto Scaling**: Sử dụng Auto Scaling Groups để tự động điều chỉnh số lượng instance theo nhu cầu.
- **Backups**: Luôn kích hoạt sao lưu tự động cho RDS và sử dụng AWS Backup cho các dịch vụ khác.

## 4. Performance (Hiệu suất)
- **CloudFront**: Sử dụng CDN để giảm độ trễ cho người dùng cuối trên toàn cầu.
- **Graviton**: Ưu tiên sử dụng các instance dựa trên chip AWS Graviton để có hiệu năng/giá thành tốt nhất.
- **Read Replicas**: Sử dụng Read Replicas cho RDS để giảm tải cho database chính.

## 5. Operational Excellence (Vận hành)
- **Infrastructure as Code (IaC)**: Sử dụng AWS CDK hoặc Terraform để quản lý hạ tầng một cách nhất quán và có thể tái lập.
- **CloudWatch**: Thiết lập Dashboards và Alarms để theo dõi sức khỏe hệ thống theo thời gian thực.
- **Logging**: Kích hoạt CloudTrail để lưu lại toàn bộ lịch sử thao tác trên tài khoản.
