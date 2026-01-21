# Claude Anti-Chaotic

Personal Claude Code workflows và AI agent orchestration cho phát triển phần mềm chuyên nghiệp.

## Tính năng chính

- **AI-Powered Planning** - Tự động lên kế hoạch và thiết kế kiến trúc
- **Multi-Agent Orchestration** - Các agent chuyên biệt làm việc song song
- **Automated Testing** - Tạo và chạy test tự động
- **Smart Documentation** - Tài liệu đồng bộ với code

## Cấu trúc project

```
├── .claude/                 # Claude Code configuration
│   ├── agents/             # Agent definitions
│   ├── commands/           # Custom commands
│   ├── skills/             # Claude skills
│   └── workflows/          # Development workflows
├── .opencode/              # Open Code agent definitions
├── docs/                   # Project documentation
├── guide/                  # Guides & tutorials
├── scripts/                # Utility scripts
├── tests/                  # Test templates
├── CLAUDE.md               # Claude instructions
└── README.md               # This file
```

## Yêu cầu

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- Git
- Node.js 18+

## Bắt đầu

```bash
# Start Claude Code
claude

# Các commands thường dùng
/plan "implement feature X"      # Lên kế hoạch
/cook "build feature X"          # Implement
/test                            # Chạy tests
/review                          # Code review
/docs                            # Update docs
/watzup                          # Check status
```

## Workflow phát triển

### Feature mới
```bash
/plan "add user authentication"   # Research & plan
/cook "implement auth"            # Build
/test                             # Validate
/review                           # Quality check
```

### Fix bug
```bash
/debug "investigate issue"        # Analyze
/fix "resolve the bug"            # Fix
/test                             # Verify
```

## Agents

| Agent | Chức năng |
|-------|-----------|
| Planner | Lên kế hoạch implementation |
| Researcher | Research công nghệ & patterns |
| Tester | Tạo và chạy tests |
| Code Reviewer | Review code quality |
| Debugger | Phân tích và fix bugs |
| Docs Manager | Quản lý documentation |
| Git Manager | Quản lý commits & branches |

## Cấu hình

### CLAUDE.md
File hướng dẫn chính cho Claude Code. Chỉnh sửa để định nghĩa:
- Project guidelines
- Development standards
- Workflow rules

### .claude/workflows/
Các workflow files định nghĩa quy trình làm việc.

### .claude/skills/
Custom skills mở rộng khả năng của Claude.

## Usage Examples

### Feature mới
```bash
# Research và plan
claude "I need to implement user authentication with OAuth2"
# Planner agent tạo plan chi tiết

# Implement theo plan
claude "Implement the authentication plan"

# Đảm bảo quality
claude "Review and test the authentication system"
```

### Debugging
```bash
# Investigate vấn đề
claude "Debug the slow database queries"
# Debugger agent phân tích logs và performance

# Tạo solution
claude "Optimize the identified query performance issues"

# Validate fix
claude "Test query performance improvements"
```

### Project Maintenance
```bash
# Check project health
claude "What's the current project status?"

# Update documentation
claude "Sync documentation with recent changes"

# Plan next sprint
claude "Plan the next development phase"
```

## API Keys (Optional)

Nếu dùng Gemini skills, set API key:

```bash
export GEMINI_API_KEY='your-api-key'
```

Hoặc tạo file `.env`:
```
GEMINI_API_KEY=your-api-key
```

## License

MIT License

## Gemini Skills Examples

```bash
# Audio analysis
claude "Analyze this audio file and summarize the key points: audio.mp3"

# Video understanding
claude "Describe what happens in this video: video.mp4"

# Document processing
claude "Extract all tables from this PDF: document.pdf"

# Image generation
claude "Generate an image of a serene mountain landscape"

# Image analysis
claude "What objects are in this image: photo.jpg"
```

## Model Context Protocol (MCP)

Setup MCP servers trong `.claude/.mcp.json`:

```bash
mv .claude/.mcp.json.example .claude/.mcp.json
```

### Ví dụ MCP servers:

**Context7:**
```json
{
   "mcpServers": {
      "context7": {
         "command": "npx",
         "args": ["-y", "@upstash/context7-mcp", "--api-key", "YOUR_API_KEY"]
      }
   }
}
```

**Chrome DevTools:**
```json
{
   "mcpServers": {
      "chrome-devtools": {
         "command": "npx",
         "args": ["-y", "chrome-devtools-mcp@latest"]
      }
   }
}
```

## Best Practices

### Development Principles
- **YAGNI**: You Aren't Gonna Need It - avoid over-engineering
- **KISS**: Keep It Simple, Stupid - prefer simple solutions
- **DRY**: Don't Repeat Yourself - eliminate code duplication

### Code Quality
- All code changes go through automated review
- Comprehensive testing is mandatory
- Security considerations are built-in

### Git Workflow
- Clean, conventional commit messages
- Professional git history
- Focused, atomic commits

## Advanced Features

### Multi-Project Support
- Manage multiple repositories simultaneously
- Shared agent configurations across projects

### Custom Agent Creation
- Define project-specific agents
- Extend existing agent capabilities
- Create domain-specific expertise

### Integration Capabilities
- Discord notifications for project updates
- GitHub Actions integration
- CI/CD pipeline enhancement

## Customization Guide

1. **Project Setup**
   - Update `CLAUDE.md` with your project specifics
   - Modify agent configurations in `.opencode/agent/`

2. **Agent Specialization**
   - Add domain-specific knowledge to agents
   - Create custom agents for unique requirements

3. **Workflow Optimization**
   - Define project-specific commands
   - Create shortcuts for common tasks
