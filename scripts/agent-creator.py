import os

def main():
    print("=== Claude Anti-Chaotic: Custom Agent Creator ===")
    print("Công cụ tạo AI Agent chuyên biệt mới.\n")

    # 1. Tên Agent
    agent_name = input("Nhập tên Agent (ví dụ: security-expert): ").strip().lower()
    if not agent_name:
        print("Lỗi: Tên Agent không được để trống.")
        return

    # 2. Mô tả
    description = input("Mô tả mục đích của Agent này: ").strip()

    # 3. Model
    print("\nChọn Model cho Agent:")
    print("1. Claude 3.5 Sonnet (Cân bằng - Khuyên dùng)")
    print("2. Claude 3.5 Haiku (Nhanh, tiết kiệm)")
    print("3. Claude 3 Opus (Thông minh nhất, tốn kém)")
    model_choice = input("Chọn (1-3): ").strip()

    models = {
        "1": "anthropic/claude-3-5-sonnet-20241022",
        "2": "anthropic/claude-3-5-haiku-20241022",
        "3": "anthropic/claude-3-opus-20240229"
    }
    selected_model = models.get(model_choice, models["1"])

    # 4. Công cụ (Tools)
    print("\nChọn các bộ công cụ cơ bản (nhập số, cách nhau bởi dấu phẩy):")
    print("1. Read (Đọc file)")
    print("2. Write (Viết file)")
    print("3. Edit (Sửa file)")
    print("4. Bash (Chạy lệnh terminal)")
    print("5. Grep (Tìm kiếm nội dung)")

    tool_map = {"1": "Read", "2": "Write", "3": "Edit", "4": "Bash", "5": "Grep"}
    tool_indices = input("Chọn (ví dụ: 1,3,5): ").split(',')
    selected_tools = []
    for idx in tool_indices:
        tool = tool_map.get(idx.strip())
        if tool:
            selected_tools.append(tool)

    # 5. Instructions (Tính cách & Quy tắc)
    print("\nNhập các quy tắc/hướng dẫn cốt lõi cho Agent (nhấn Enter 2 lần để kết thúc):")
    instructions = []
    while True:
        line = input("> ")
        if not line:
            break
        instructions.append(line)

    # 6. Tạo nội dung Markdown
    tools_str = ", ".join(selected_tools)
    inst_str = "\n".join([f"- {line}" for line in instructions])

    md_content = f"""---
name: {agent_name}
description: {description}
model: {selected_model}
tools: [{tools_str}]
---

# {agent_name.replace('-', ' ').title()} Agent Instructions

Bạn là một chuyên gia trong lĩnh vực: {description}.

## Nhiệm vụ cốt lõi
{inst_str if instructions else "- Thực hiện các yêu cầu của người dùng một cách chuyên nghiệp."}

## Quy trình làm việc
1. Phân tích yêu cầu và bối cảnh mã nguồn.
2. Sử dụng các công cụ được cấp để thực hiện nhiệm vụ.
3. Luôn kiểm tra kết quả trước khi báo cáo.
4. Báo cáo súc tích, tập trung vào kết quả kỹ thuật.

## Tiêu chuẩn chất lượng
- Code phải sạch, dễ bảo trì.
- Tuân thủ các tiêu chuẩn bảo mật của dự án.
- Ưu tiên sự đơn giản và hiệu quả.
"""

    # 7. Lưu file
    agents_dir = os.path.join('.claude', 'agents')
    if not os.path.exists(agents_dir):
        os.makedirs(agents_dir)

    output_path = os.path.join(agents_dir, f"{agent_name}.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"\n✅ Thành công! Agent mới đã được tạo tại: {output_path}")
    print(f"Bây giờ bạn có thể triệu hồi Agent này bằng cách dùng lệnh `/ask {agent_name}` hoặc tích hợp vào Workflow.")

if __name__ == "__main__":
    main()
