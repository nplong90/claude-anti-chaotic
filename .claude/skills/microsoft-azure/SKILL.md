---
name: microsoft-azure
description: Chuyên gia về Microsoft Azure. Cung cấp kiến thức và hướng dẫn triển khai Azure App Service, Azure Functions, AKS (Kubernetes), Azure SQL, và Blob Storage. Sử dụng khi thiết kế kiến trúc hệ thống trên Azure, tối ưu hóa chi phí hoặc tự động hóa hạ tầng với Azure CLI và Bicep/Terraform.
license: MIT
version: 1.0.0
---

# Microsoft Azure Skill

Hướng dẫn toàn diện về việc triển khai và quản lý hạ tầng trên nền tảng Microsoft Azure.

## Các dịch vụ trọng tâm

### 1. Compute & Containers
- **Azure App Service**: Host các ứng dụng web, mobile backends và RESTful APIs.
- **Azure Functions**: Giải pháp compute serverless dựa trên sự kiện.
- **Azure Kubernetes Service (AKS)**: Quản lý cụm Kubernetes đơn giản và mạnh mẽ.
- **Azure Container Instances (ACI)**: Chạy container nhanh chóng mà không cần quản lý VM.

### 2. Storage & Databases
- **Azure Blob Storage**: Lưu trữ dữ liệu không cấu trúc quy mô lớn (Object storage).
- **Azure SQL Database**: Dịch vụ cơ sở dữ liệu quan hệ (PaaS) dựa trên SQL Server.
- **Azure Cosmos DB**: Cơ sở dữ liệu NoSQL phân tán toàn cầu, đa mô hình.

### 3. Networking & Security
- **Azure Virtual Network (VNet)**: Mạng riêng ảo biệt lập và bảo mật.
- **Microsoft Entra ID (tên cũ Azure AD)**: Quản lý danh tính và quyền truy cập.
- **Azure Key Vault**: Lưu trữ bảo mật các secrets, keys và certificates.

## Khi nào nên sử dụng Skill này

- Khi cần triển khai các ứng dụng web chuẩn doanh nghiệp trên **App Service**.
- Khi cần tích hợp sâu với hệ sinh thái Microsoft (Active Directory, Office 365).
- Khi xây dựng hệ thống serverless với **Azure Functions**.
- Khi quản lý hạ tầng bằng **Azure CLI** hoặc **Infrastructure as Code (Bicep/ARM/Terraform)**.

## Lệnh Azure CLI cơ bản

```bash
# Đăng nhập
az login

# Liệt kê các Resource Groups
az group list --output table

# Triển khai ứng dụng web (Web App)
az webapp up --name [APP_NAME] --resource-group [RG_NAME] --plan [PLAN_NAME]
```

## Tài liệu tham khảo
- `references/azure-cli-cheatsheet.md`: Danh sách lệnh Azure CLI thông dụng.
- `references/azure-best-practices.md`: Quy tắc tối ưu hóa kiến trúc Azure.

---
*Duy trì bởi Claude Anti-Chaotic Team*
