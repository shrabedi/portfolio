"""Command-line interface for TaskMaster."""

import click
from tabulate import tabulate

from taskmaster.core.manager import TaskManager


@click.group()
def cli():
    """TaskMaster - CLI task management tool."""
    pass


@cli.command()
@click.argument("title")
@click.option("--priority", default="medium", help="Task priority")
@click.option("--due", help="Due date")
def add(title: str, priority: str, due: str) -> None:
    """Add a new task."""
    manager = TaskManager()
    task = manager.add(title, priority=priority, due=due)
    click.echo(click.style(f"✓ Task created (ID: {task['id']})", fg="green"))


@cli.command()
@click.option("--status", help="Filter by status")
@click.option("--priority", help="Filter by priority")
def list(status: str, priority: str) -> None:
    """List tasks."""
    manager = TaskManager()
    tasks = manager.list_tasks(status=status, priority=priority)

    if not tasks:
        click.echo("No tasks found.")
        return

    rows = [
        [t["id"], t["title"], t["priority"], t["status"], t["due"] or "-"]
        for t in tasks
    ]
    click.echo(tabulate(rows, headers=["ID", "Title", "Priority", "Status", "Due"]))


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id: int) -> None:
    """Mark task as complete."""
    manager = TaskManager()
    if manager.complete(task_id):
        click.echo(click.style(f"✓ Task {task_id} completed", fg="green"))
    else:
        click.echo(click.style("Task not found", fg="red"))


@cli.command()
@click.argument("query")
def search(query: str) -> None:
    """Search tasks."""
    manager = TaskManager()
    results = manager.search(query)

    if not results:
        click.echo("No tasks found.")
        return

    rows = [[t["id"], t["title"], t["priority"], t["status"]] for t in results]
    click.echo(tabulate(rows, headers=["ID", "Title", "Priority", "Status"]))


@cli.command()
def stats() -> None:
    """Show productivity statistics."""
    manager = TaskManager()
    data = manager.stats()

    click.echo("\n📊 Productivity Stats")
    click.echo(f"Total Tasks: {data['total']}")
    click.echo(f"Completed: {data['completed']}")
    click.echo(f"Completion Rate: {data['completion_rate']:.1f}%")
    click.echo("\nBy Priority:")
    for priority, count in data["by_priority"].items():
        click.echo(f"  {priority}: {count}")


if __name__ == "__main__":
    cli()
