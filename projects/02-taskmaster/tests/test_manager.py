"""Tests for TaskManager."""

import pytest

from taskmaster.core.manager import TaskManager


@pytest.fixture
def manager():
    """Create TaskManager instance."""
    return TaskManager()


def test_add_task(manager):
    """Test adding a task."""
    task = manager.add("Test task", priority="high")
    assert task["title"] == "Test task"
    assert task["priority"] == "high"


def test_list_tasks(manager):
    """Test listing tasks."""
    manager.add("Task 1", priority="high")
    manager.add("Task 2", priority="low")
    tasks = manager.list_tasks()
    assert len(tasks) >= 2


def test_complete_task(manager):
    """Test completing a task."""
    task = manager.add("Test task")
    assert manager.complete(task["id"])
    tasks = manager.list_tasks(status="completed")
    assert len(tasks) >= 1


def test_search_tasks(manager):
    """Test searching tasks."""
    manager.add("Python project")
    manager.add("Documentation")
    results = manager.search("python")
    assert len(results) >= 1


def test_stats(manager):
    """Test statistics."""
    manager.add("Task 1")
    manager.add("Task 2", priority="high")
    stats = manager.stats()
    assert stats["total"] >= 2
    assert "by_priority" in stats
