import pytest

from src.task import Task


@pytest.mark.smoke
def test_create_task():
    t = Task('do_something', 'igor', True, 21)
    assert isinstance(t, Task)
    
def test_create_task_with_defaults():
    t = Task()
    assert isinstance(t, Task)