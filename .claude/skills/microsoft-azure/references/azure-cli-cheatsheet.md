# Azure CLI Cheatsheet

Danh sách các lệnh Azure CLI (az) thông dụng để quản lý tài nguyên.

## 1. Đăng nhập & Quản lý Subscription
```bash
az login                        # Đăng nhập qua trình duyệt
az account list --output table  # Liệt kê các subscriptions
az account set --subscription ID # Chọn subscription làm việc
```

## 2. Resource Groups (Nhóm tài nguyên)
```bash
az group create --name [NAME] --location eastus  # Tạo mới
az group list --output table                      # Liệt kê
az group delete --name [NAME]                    # Xóa nhóm (cẩn thận!)
```

## 3. Azure App Service (Web Apps)
```bash
# Triển khai nhanh code local lên Azure
az webapp up --name [APP_NAME] --resource-group [RG_NAME] --plan [PLAN_NAME]

# Xem logs trực tiếp
az webapp log tail --name [APP_NAME] --resource-group [RG_NAME]
```

## 4. Azure Functions (Serverless)
```bash
# Liệt kê các function apps
az functionapp list --resource-group [RG_NAME]

# Triển khai (thường dùng Azure Functions Core Tools)
func azure functionapp publish [APP_NAME]
```

## 5. Storage (Blob Storage)
```bash
# Tạo Storage Account
az storage account create --name [NAME] --resource-group [RG] --location eastus --sku Standard_LRS

# Upload file lên container
az storage blob upload --account-name [NAME] --container-name [C_NAME] --name [BLOB_NAME] --file [LOCAL_PATH]
```

## 6. Azure Key Vault (Bảo mật)
```bash
# Tạo Key Vault
az keyvault create --name [NAME] --resource-group [RG]

# Thêm secret
az keyvault secret set --vault-name [NAME] --name "MySecret" --value "P@ssword123"
```
