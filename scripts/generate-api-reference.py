import os
import re
import yaml
from datetime import datetime

def extract_frontmatter(file_path):
    """Trích xuất phần YAML frontmatter từ file markdown."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None
    return None

def generate_reference():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    agents_dir = os.path.join(base_dir, '.claude', 'agents')
    skills_dir = os.path.join(base_dir, '.claude', 'skills')
    output_path = os.path.join(base_dir, 'docs', 'api-reference.md')

    markdown = [
        "# Claude Anti-Chaotic - API & Agent Reference",
        f"\n**Tự động tạo lúc:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "Tài liệu này tổng hợp danh sách các Agent và Skills hiện có trong hệ thống.\n",
        "## 1. Danh sách Agents\n",
        "Các Agent chuyên biệt hỗ trợ quy trình phát triển phần mềm.\n",
        "| Agent | Mô tả | Model | Công cụ |",
        "|-------|-------|-------|---------|"
    ]

    # Xử lý Agents
    if os.path.exists(agents_dir):
        for filename in sorted(os.listdir(agents_dir)):
            if filename.endswith('.md'):
                data = extract_frontmatter(os.path.join(agents_dir, filename))
                if data:
                    name = data.get('name', filename[:-3])
                    desc = data.get('description', 'Không có mô tả')
                    model = data.get('model', 'Default')
                    tools = ", ".join(data.get('tools', [])) if isinstance(data.get('tools'), list) else 'N/A'
                    markdown.append(f"| **{name}** | {desc} | `{model}` | {tools} |")

    markdown.append("\n## 2. Danh sách Skills\n")
    markdown.append("Các mô-đun kiến thức chuyên sâu và script hỗ trợ.\n")
    markdown.append("| Skill | Phiên bản | Mô tả |")
    markdown.append("|-------|-----------|-------|")

    # Xử lý Skills
    if os.path.exists(skills_dir):
        for skill_name in sorted(os.listdir(skills_dir)):
            skill_path = os.path.join(skills_dir, skill_name, 'SKILL.md')
            if os.path.exists(skill_path):
                data = extract_frontmatter(skill_path)
                if data:
                    name = data.get('name', skill_name)
                    version = data.get('version', '1.0.0')
                    desc = data.get('description', 'Không có mô tả')
                    markdown.append(f"| **{name}** | v{version} | {desc} |")

    markdown.append("\n---\n*Tài liệu này được tạo tự động bởi `scripts/generate-api-reference.py`*")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(markdown))

    print(f"Successfully generated: {output_path}")

if __name__ == "__main__":
    generate_reference()
