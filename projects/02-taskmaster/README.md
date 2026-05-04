# TaskMaster

A powerful command-line task management tool with persistent storage, priority levels, and productivity tracking.

## Features

- **Task Management**: Create, read, update, delete tasks from CLI
- **Priority Levels**: Organize tasks by priority (low, medium, high, critical)
- **Persistent Storage**: Auto-save to JSON with backup capabilities
- **Search & Filter**: Quick search and filter tasks by status, priority, date
- **Statistics**: Track productivity metrics and task completion rates
- **Due Dates**: Set reminders and manage deadlines
- **Bulk Operations**: Mark multiple tasks complete in one command
- **Colored Output**: Beautiful terminal UI with colors

## Quick Start

```bash
pip install -r requirements.txt

# Add a task
taskmaster add "Complete project documentation" --priority high --due "2026-05-15"

# List all tasks
taskmaster list

# Mark task as done
taskmaster complete 1

# Search tasks
taskmaster search "documentation"

# Get statistics
taskmaster stats
```

## Installation

```bash
git clone https://github.com/shrabedi/portfolio.git
cd portfolio/projects/02-taskmaster
pip install -r requirements.txt
```

## Usage

### Commands

```bash
# Add task
taskmaster add <task> [--priority PRIORITY] [--due DUE_DATE] [--tags TAGS]

# List tasks
taskmaster list [--status STATUS] [--priority PRIORITY]

# Update task
taskmaster update <id> [--title TITLE] [--priority PRIORITY] [--status STATUS]

# Complete task
taskmaster complete <id>

# Delete task
taskmaster delete <id>

# Search
taskmaster search <query>

# Statistics
taskmaster stats

# Clear completed
taskmaster clear
```

### Priority Levels

- `low` - Background tasks, nice-to-haves
- `medium` - Regular tasks
- `high` - Important tasks
- `critical` - Urgent, must-complete today

### Task Status

- `pending` - Not started
- `in_progress` - Currently working on
- `completed` - Finished
- `blocked` - Waiting on something

## Architecture

- `taskmaster/cli/` - Command-line interface (Click)
- `taskmaster/core/` - Task management logic
- `taskmaster/storage/` - Persistence layer
- `tests/` - Test suite

## Data Storage

Tasks are stored in `~/.taskmaster/tasks.json`:

```json
[
  {
    "id": 1,
    "title": "Complete project",
    "priority": "high",
    "status": "pending",
    "created": "2026-05-05T10:30:00",
    "due": "2026-05-15T23:59:59"
  }
]
```

## Performance

- Sub-100ms operations on 5000+ tasks
- Efficient JSON serialization
- Atomic writes with backup

## Testing

```bash
pytest tests/ -v --cov=taskmaster
```

## License

MIT

## Author

Hussain Raza Abedi
