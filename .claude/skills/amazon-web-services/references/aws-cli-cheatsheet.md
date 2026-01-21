# AWS CLI Cheatsheet

Danh sách các lệnh AWS CLI thông dụng để quản lý tài nguyên nhanh chóng.

## 1. Cấu hình & Danh tính (Configuration & Identity)
```bash
aws configure                   # Cấu hình Access Key, Secret Key, Region
aws sts get-caller-identity     # Kiểm tra tài khoản đang đăng nhập
aws configure list              # Xem cấu hình hiện tại
```

## 2. Amazon S3 (Lưu trữ đối tượng)
```bash
# Liệt kê các bucket
aws s3 ls

# Upload file lên bucket
aws s3 cp [FILE] s3://[BUCKET_NAME]/

# Đồng bộ thư mục local với S3
aws s3 sync ./local-dir s3://[BUCKET_NAME]/
```

## 3. AWS Lambda (Serverless)
```bash
# Liệt kê các hàm Lambda
aws lambda list-functions

# Gọi hàm Lambda từ CLI
aws lambda invoke --function-name [NAME] response.json
```

## 4. Amazon EC2 (Máy chủ ảo)
```bash
# Liệt kê các instance đang chạy
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"

# Khởi động / Dừng instance
aws ec2 start-instances --instance-ids [ID]
aws ec2 stop-instances --instance-ids [ID]
```

## 5. AWS Secrets Manager
```bash
# Lấy giá trị của một secret
aws secretsmanager get-secret-value --secret-id [NAME]

# Liệt kê các secret
aws secretsmanager list-secrets
```

## 6. IAM (Quản lý quyền)
```bash
# Liệt kê user
aws iam list-users

# Xem các chính sách (policies) của một user
aws iam list-attached-user-policies --user-name [NAME]
```
