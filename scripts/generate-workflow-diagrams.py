import os
import re

def generate_mermaid_diagrams():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    commands_dir = os.path.join(base_dir, '.claude', 'commands')
    output_path = os.path.join(base_dir, 'docs', 'workflows-visualization.md')

    if not os.path.exists(commands_dir):
        print(f"Error: {commands_dir} not found.")
        return

    content = [
        "# Workflow Visualization",
        "\nTài liệu này trực quan hóa các quy trình phối hợp (orchestration) của AI Agent trong hệ thống Claude Anti-Chaotic bằng sơ đồ Mermaid.\n",
        "## 1. Quy trình phát triển tính năng (/cook)\n",
        "Quy trình phức tạp nhất, phối hợp nhiều Agent từ lập kế hoạch đến triển khai và kiểm thử.\n",
        "```mermaid",
        "sequenceDiagram",
        "    participant U as User",
        "    participant M as Main Agent",
        "    participant R as Researcher",
        "    participant S as Scout",
        "    participant P as Planner",
        "    participant D as UI/UX Designer",
        "    participant T as Tester",
        "    participant DB as Debugger",
        "    participant CR as Code Reviewer",
        "    participant PM as Project Manager",
        "    participant DM as Docs Manager",
        "",
        "    U->>M: /cook [task]",
        "    M->>R: Research request (Parallel)",
        "    M->>S: Scout codebase (Parallel)",
        "    R-->>M: Research Report",
        "    S-->>M: Scout Report",
        "    M->>P: Request Plan",
        "    P-->>M: Implementation Plan",
        "    M->>M: Implement Backend/Core",
        "    M->>D: Implement Frontend/UI",
        "    M->>T: Run Tests",
        "    alt Tests Fail",
        "        T->>DB: Report Failures",
        "        DB-->>M: Root Cause Analysis",
        "        M->>M: Fix Code",
        "        M->>T: Re-run Tests",
        "    end",
        "    M->>CR: Request Code Review",
        "    CR-->>M: Review Feedback",
        "    M->>U: Final Report & Approval",
        "    U->>M: Approve",
        "    M->>PM: Update Roadmap & Tasks",
        "    M->>DM: Update Documentation",
        "    M->>U: Finished!",
        "```\n",
        "## 2. Quy trình sửa lỗi (/debug)\n",
        "Tập trung vào việc phân tích nguyên nhân gốc rễ.\n",
        "```mermaid",
        "graph TD",
        "    U[User] -->|/debug| M[Main Agent]",
        "    M --> DB[Debugger Agent]",
        "    DB -->|Read Logs| DB",
        "    DB -->|Analyze Code| DB",
        "    DB -->|Identify Root Cause| R[Report to User]",
        "    R -->|Optional| P[Planner Agent]",
        "    P -->|Create Fix Plan| M",
        "```\n",
        "## 3. Quy trình lập kế hoạch (/plan)\n",
        "```mermaid",
        "graph LR",
        "    U[User] -->|/plan| M[Main Agent]",
        "    M -->|Analyze Complexity| C{Complexity?}",
        "    C -->|Simple| PF[plan:fast]",
        "    C -->|Complex| PH[plan:hard]",
        "    PF --> P[Planner Agent]",
        "    PH --> P",
        "    P -->|Generate Docs| D[docs/plans/]",
        "```\n",
        "## 4. Các mẫu phối hợp phổ biến\n",
        "### Chaining (Nối tiếp)\n",
        "```mermaid",
        "graph LR",
        "    A[Agent A] -->|Report| B[Agent B] -->|Report| C[Agent C]",
        "```\n",
        "### Parallel Fan-Out (Song song)\n",
        "```mermaid",
        "graph TD",
        "    M[Coordinator] --> A1[Researcher 1]",
        "    M --> A2[Researcher 2]",
        "    M --> A3[Scout]",
        "    A1 --> R[Synthesized Report]",
        "    A2 --> R",
        "    A3 --> R",
        "```\n",
        "---\n*Tài liệu này được tạo tự động để hỗ trợ việc hiểu kiến trúc hệ thống.*"
    ]

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(content))

    print(f"Successfully generated: {output_path}")

if __name__ == "__main__":
    generate_mermaid_diagrams()
