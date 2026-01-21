---
name: amazon-web-services
description: Chuyên gia về Amazon Web Services (AWS). Cung cấp kiến thức và hướng dẫn triển khai Lambda, EC2, ECS/EKS, S3, DynamoDB và RDS. Sử dụng khi thiết kế kiến trúc hệ thống trên AWS, quản lý hạ tầng bằng AWS CLI, hoặc triển khai serverless với AWS SAM/CDK.
license: MIT
version: 1.0.0
---

# Amazon Web Services (AWS) Skill

Hướng dẫn toàn diện về việc triển khai và quản lý hạ tầng trên nền tảng AWS.

## Các dịch vụ trọng tâm

### 1. Compute & Containers
- **AWS Lambda**: Chạy code dưới dạng serverless functions.
- **Amazon EC2**: Máy chủ ảo (Virtual Private Servers) có khả năng mở rộng.
- **Amazon ECS/EKS**: Quản lý container (Docker) và Kubernetes (EKS).
- **AWS Fargate**: Chạy container mà không cần quản lý server.

### 2. Storage & Databases
- **Amazon S3**: Lưu trữ đối tượng (Object storage) với độ bền cao.
- **Amazon DynamoDB**: Cơ sở dữ liệu NoSQL tốc độ milisecond.
- **Amazon RDS**: Cơ sở dữ liệu quan hệ (PostgreSQL, MySQL, Aurora) được quản lý.

### 3. Networking & Security
- **Amazon VPC**: Mạng riêng ảo biệt lập.
- **AWS IAM**: Quản lý quyền truy cập và định danh người dùng.
- **AWS Secrets Manager**: Quản lý và xoay vòng các bí mật (API keys, credentials).

## Khi nào nên sử dụng Skill này

- Khi cần triển khai kiến trúc **Serverless** với Lambda và API Gateway.
- Khi cần thiết lập hệ thống lưu trữ tĩnh hoặc media trên **S3**.
- Khi cần quản lý hạ tầng tự động bằng **AWS CLI** hoặc **Infrastructure as Code (CDK/Terraform)**.
- Khi cần tối ưu hóa hiệu suất và chi phí trên hệ sinh thái AWS.

## Lệnh AWS CLI cơ bản

```bash
# Cấu hình tài khoản
aws configure

# Liệt kê các file trong S3
aws s3 ls s3://[BUCKET_NAME]

# Triển khai Lambda (ví dụ qua SAM)
sam deploy --guided
```

## Tài liệu tham khảo
- `references/aws-cli-cheatsheet.md`: Danh sách lệnh AWS CLI thông dụng.
- `references/aws-best-practices.md`: Quy tắc tối ưu hóa kiến trúc AWS.

---
*Duy trì bởi Claude Anti-Chaotic Team*
