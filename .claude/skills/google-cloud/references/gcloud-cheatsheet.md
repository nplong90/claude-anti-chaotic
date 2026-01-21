# gcloud CLI Cheatsheet

Danh sách các lệnh gcloud thường dùng cho phát triển và triển khai nhanh.

## 1. Cấu hình ban đầu
```bash
gcloud auth login               # Đăng nhập
gcloud config set project ID    # Thiết lập project ID
gcloud config list             # Xem cấu hình hiện tại
```

## 2. Cloud Run (Serverless Containers)
```bash
# Triển khai nhanh từ source
gcloud run deploy [SERVICE] --source . --region asia-east1 --allow-unauthenticated

# Xem logs
gcloud beta run services logs tail [SERVICE]
```

## 3. Cloud Storage (Bucket)
```bash
# Tạo bucket
gcloud storage buckets create gs://[BUCKET_NAME] --location=asia-east1

# Upload file
gcloud storage cp [FILE] gs://[BUCKET_NAME]/
```

## 4. Secret Manager
```bash
# Tạo secret
gcloud secrets create [NAME] --replication-policy="automatic"

# Thêm giá trị cho secret
echo -n "giá_trị_bí_mật" | gcloud secrets versions add [NAME] --data-file=-
```

## 5. IAM & Service Accounts
```bash
# Tạo service account
gcloud iam service-accounts create [SA_NAME]

# Cấp quyền (ví dụ: storage admin)
gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
    --role="roles/storage.admin"
```
