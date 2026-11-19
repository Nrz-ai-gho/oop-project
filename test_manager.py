import pytest

from manager_tasks import Task, TaskManager

@pytest.fixture
def manager():
    import sqlite3
    db = sqlite3.connect("tasks.db")
    c = db.cursor()
    c.execute("DELETE FROM tasks")
    db.commit()
    db.close()
    return TaskManager()

def test_task_creation():
    task = Task("Купить хлеб")
    assert task.title == "Купить хлеб"
    assert task.done == False    
    
def test_task_complete():
    task = Task("Купить хлеб")
    assert task.title == "Купить хлеб"
    task.complete()
    assert task.done == True
    
def test_add_remove(manager):
    manager.add("Купить молоко")
    
    import sqlite3 
    db = sqlite3.connect("tasks.db")
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM tasks")
    count = c.fetchone()[0]
    
    assert count == 1
    
def test_remove_from_empty_list(manager, capsys):
    manager.remove(1)
    captured = capsys.readouterr()
    assert "No such task" in captured.out
    
def test_remove_invalid_index(manager, capsys):
    manager.add("Learn Git")
    manager.remove(5)
    captured = capsys.readouterr()
    assert "No such task" in captured.out
    
def test_add_several_tasks(manager):
    manager.add("Reading")
    manager.add("Running")
    manager.add("Buy a strawberry")
    
    import sqlite3
    db = sqlite3.connect("tasks.db")
    c = db.cursor()
    c.execute("SELECT title FROM tasks")
    items = c.fetchall()
    
    assert len(items) == 3
    assert items[0][0] == "Reading"  
    assert items[1][0] == "Running"
    assert items[2][0] == "Buy a strawberry"
    
