import os
import re
import json
from datetime import datetime

def parse_token_usage():
    """
    Quét các file báo cáo trong thư mục plans/ để thống kê lượng token.
    Lưu ý: Đây là ước tính dựa trên độ dài văn bản nếu agent không xuất thông số cụ thể.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    plans_dir = os.path.join(base_dir, 'plans')
    report_data = []

    if not os.path.exists(plans_dir):
        return "Chưa có dữ liệu kế hoạch (plans/)."

    for root, dirs, files in os.walk(plans_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Ước tính token (1 token ~ 4 ký tự cho tiếng Anh, 1 ký tự ~ 1-2 token cho tiếng Việt)
                    # Đây là công thức tính gần đúng để theo dõi xu hướng
                    char_count = len(content)
                    est_tokens = int(char_count / 3)

                    report_data.append({
                        "file": file,
                        "date": datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d'),
                        "tokens": est_tokens
                    })

    # Tổng hợp theo ngày
    daily_stats = {}
    for entry in report_data:
        day = entry['date']
        daily_stats[day] = daily_stats.get(day, 0) + entry['tokens']

    output = [
        "# Token Usage Report (Estimated)",
        f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "| Ngày | Ước tính Token (Output) | Tương đương chi phí ($) |",
        "|------|-------------------------|-------------------------|"
    ]

    # Giả định chi phí trung bình 3$/1M token (kết hợp Sonnet/Haiku)
    for day in sorted(daily_stats.keys(), reverse=True):
        tokens = daily_stats[day]
        cost = (tokens / 1000000) * 3.0
        output.append(f"| {day} | {tokens:,} | ${cost:.4f} |")

    return "\n".join(output)

if __name__ == "__main__":
    report = parse_token_usage()

    # In ra terminal với encoding an toàn hoặc bỏ qua lỗi trên Windows
    try:
        print(report)
    except UnicodeEncodeError:
        print("Report generated (encoding issue displaying in terminal, but saved to file).")

    # Lưu report vào docs
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(base_dir, 'docs', 'token-usage-report.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Report saved to: {output_path}")
