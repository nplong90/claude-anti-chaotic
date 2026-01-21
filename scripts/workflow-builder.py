import os
import sys

def get_agents():
    agents_dir = os.path.join('.claude', 'agents')
    if not os.path.exists(agents_dir):
        return []
    return [f[:-3] for f in os.listdir(agents_dir) if f.endswith('.md')]

def main():
    print("=== Claude Anti-Chaotic: Workflow Builder ===")
    print("Công cụ tạo lệnh (Slash Command) phối hợp Agent mới.\n")

    # 1. Tên lệnh
    cmd_name = input("Nhập tên lệnh mới (ví dụ: my-feature): ").strip().lower()
    if not cmd_name:
        print("Lỗi: Tên lệnh không được để trống.")
        return

    # 2. Mô tả
    description = input("Mô tả ngắn gọn về lệnh này: ").strip()

    # 3. Chọn Agents
    available_agents = get_agents()
    if not available_agents:
        print("Lỗi: Không tìm thấy agent nào trong .claude/agents/")
        return

    print("\nDanh sách Agent có sẵn:")
    for i, agent in enumerate(available_agents):
        print(f"{i+1}. {agent}")

    selected_indices = input("\nChọn các Agent tham gia (nhập số, cách nhau bởi dấu phẩy, ví dụ: 1,3,5): ").split(',')
    selected_agents = []
    try:
        for idx in selected_indices:
            selected_agents.append(available_agents[int(idx.strip()) - 1])
    except (ValueError, IndexError):
        print("Lỗi: Lựa chọn không hợp lệ.")
        return

    # 4. Kiểu phối hợp
    print("\nKiểu phối hợp (Orchestration Type):")
    print("1. Sequential (Nối tiếp: A -> B -> C)")
    print("2. Parallel (Song song: A + B + C)")
    orch_type = input("Chọn (1 hoặc 2): ").strip()

    # 5. Tạo nội dung Markdown
    md_content = f"""---
name: {cmd_name}
description: {description}
---

# Workflow: {cmd_name}

## 1. Phân tích & Chuẩn bị
Nhiệm vụ: $ARGUMENTS

## 2. Quy trình thực hiện
"""

    if orch_type == '1':
        md_content += "Các Agent sẽ thực hiện lần lượt theo thứ tự:\n\n"
        for agent in selected_agents:
            md_content += f"- **{agent}**: Thực hiện nhiệm vụ tương ứng và báo cáo kết quả.\n"
            md_content += f"  - Triệu hồi: `/{agent} $ARGUMENTS`\n"
    else:
        md_content += "Các Agent sẽ thực hiện song song để tối ưu thời gian:\n\n"
        for agent in selected_agents:
            md_content += f"- **{agent}** (Parallel)\n"
        md_content += "\nSau khi tất cả hoàn thành, Main Agent sẽ tổng hợp báo cáo.\n"

    md_content += """
## 3. Tiêu chuẩn chất lượng
- Tuân thủ Orchestration Protocol.
- Đảm bảo tính nhất quán giữa các báo cáo.
"""

    # 6. Lưu file
    output_dir = os.path.join('.claude', 'commands', 'custom')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f"{cmd_name}.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"\n✅ Thành công! Lệnh mới đã được tạo tại: {output_path}")
    print(f"Bây giờ bạn có thể dùng lệnh: /{cmd_name} [nhiệm vụ]")

if __name__ == "__main__":
    main()
