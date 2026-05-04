"""Task management core."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

TASK_FILE = Path.home() / ".taskmaster" / "tasks.json"


class TaskManager:
    """Manage tasks with persistence."""

    def __init__(self):
        """Initialize task manager."""
        self.tasks: List[Dict] = []
        TASK_FILE.parent.mkdir(parents=True, exist_ok=True)
        self._load()

    def _load(self) -> None:
        """Load tasks from disk."""
        if TASK_FILE.exists():
            with open(TASK_FILE) as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def _save(self) -> None:
        """Save tasks to disk."""
        with open(TASK_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2, default=str)

    def add(
        self,
        title: str,
        priority: str = "medium",
        due: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Dict:
        """Add new task."""
        task = {
            "id": max([t["id"] for t in self.tasks], default=0) + 1,
            "title": title,
            "priority": priority,
            "status": "pending",
            "tags": tags or [],
            "created": datetime.now().isoformat(),
            "due": due,
        }
        self.tasks.append(task)
        self._save()
        return task

    def list_tasks(self, status: Optional[str] = None, priority: Optional[str] = None) -> List[Dict]:
        """List tasks with optional filters."""
        result = self.tasks
        if status:
            result = [t for t in result if t["status"] == status]
        if priority:
            result = [t for t in result if t["priority"] == priority]
        return result

    def complete(self, task_id: int) -> bool:
        """Mark task as complete."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                self._save()
                return True
        return False

    def delete(self, task_id: int) -> bool:
        """Delete task."""
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self._save()
        return True

    def search(self, query: str) -> List[Dict]:
        """Search tasks by title."""
        return [t for t in self.tasks if query.lower() in t["title"].lower()]

    def stats(self) -> Dict:
        """Get productivity statistics."""
        completed = len([t for t in self.tasks if t["status"] == "completed"])
        return {
            "total": len(self.tasks),
            "completed": completed,
            "pending": len([t for t in self.tasks if t["status"] == "pending"]),
            "completion_rate": (completed / len(self.tasks) * 100) if self.tasks else 0,
            "by_priority": {
                p: len([t for t in self.tasks if t["priority"] == p])
                for p in ["low", "medium", "high", "critical"]
            },
        }
