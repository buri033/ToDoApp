import random


class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed: bool = True

    def add_tag(self, tag: str):

        if tag in self.tags:
            return self.tags
        else:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id}-{self.title}"


class TodoBook:
    def __init__(self):
        self.todos: dict = {}

    def add_todo(self, title: str, description: str) -> int:
        id = len(self.todos) + 1
        objecttodo = Todo(4, "Cien años de Recocha", "Camarón que se parcha, se lo lleva la recocha")
        self.todos[4] = objecttodo
        return id
