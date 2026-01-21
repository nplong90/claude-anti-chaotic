# Deployment Guide

Hướng dẫn chi tiết cách cài đặt môi trường phát triển và triển khai dự án Claude Anti-Chaotic.

## 1. Cài đặt Môi trường Phát triển (Windows)

Dự án này được tối ưu hóa cho môi trường Windows với hỗ trợ Statusline và các hook bảo mật.

### Yêu cầu hệ thống
- **Node.js**: Phiên bản 18.0.0 trở lên.
- **Git**: Đã cài đặt và cấu hình (khuyên dùng Git Bash).
- **Claude Code CLI**: Đã cài đặt (`npm install -g @anthropic-ai/claude-code`).

### Các bước thiết lập
1. **Clone dự án**:
   ```bash
   git clone https://github.com/nplong90/claude-anti-chaotic.git
   cd claude-anti-chaotic
   ```

2. **Cấu hình Statusline**:
   - Mở PowerShell với quyền Admin.
   - Chạy lệnh: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.
   - Thêm `.claude/statusline.ps1` vào profile PowerShell của bạn.

3. **Cấu hình Biến môi trường**:
   - Tạo file `.env` dựa trên `.env.example`.
   - Thêm `GEMINI_API_KEY` nếu bạn sử dụng các skill liên quan đến đa phương thức.

## 2. Sử dụng AI Agent để Triển khai (Cloud Deployment)

Hệ thống cung cấp các Skill chuyên biệt để giúp bạn triển khai ứng dụng lên các nền tảng đám mây lớn.

### Triển khai lên Google Cloud (GCP)
Sử dụng lệnh `/cook` để tự động hóa quy trình:
```bash
/cook "Triển khai ứng dụng hiện tại lên Cloud Run region asia-southeast1"
```
Agent sẽ sử dụng Skill `google-cloud` để tạo Dockerfile, build image và deploy.

### Triển khai lên Amazon Web Services (AWS)
```bash
/cook "Triển khai backend Lambda sử dụng AWS SAM"
```
Agent sẽ tham chiếu Skill `amazon-web-services` để cấu hình template và thực hiện lệnh `sam deploy`.

### Triển khai lên Microsoft Azure
```bash
/cook "Deploy ứng dụng web lên Azure App Service"
```
Agent sẽ dùng Skill `microsoft-azure` để chạy lệnh `az webapp up`.

## 3. Quy trình CI/CD

Dự án tích hợp sẵn GitHub Actions để tự động hóa việc phát hành phiên bản.

1. **Commit code**: Luôn sử dụng **Conventional Commits** (ví dụ: `feat: add new feature`).
2. **Push to Main**: Khi push lên nhánh `main`, GitHub Actions sẽ:
   - Chạy các bộ test tự động.
   - Phân tích commit để tăng version (Semantic Versioning).
   - Tạo GitHub Release và Changelog tự động.

## 4. Bảo mật khi triển khai

- **Secret Management**: Tuyệt đối không commit file `.env` hoặc các keys. Sử dụng `Secret Manager` của các nền tảng cloud (đã có hướng dẫn trong các Skill tương ứng).
- **Scout Block Hook**: Hệ thống tự động chặn AI đọc các thư mục nặng như `node_modules` để tiết kiệm token và tăng tốc độ xử lý.

---
*Duy trì bởi Claude Anti-Chaotic Team*
