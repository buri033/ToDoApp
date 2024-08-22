class Todo:
    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str], tag: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []
        self.tag: str = tag

    def mark_completed(self):
        self.completed = True

    def add_tag(self):

        if self.tag in self.tags:
            return self.tags
        else:
            self.tags.append(self.tag)
