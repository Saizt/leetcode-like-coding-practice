
class CloudStorage: #stopped at level 3

    def __init__(self):
        self.storage = {}


    def add_file(self, name: str, size: int) -> bool:
        if name not in self.storage:
            self.storage[name] = size
            return True

        return False


    def get_file_size(self, name: str):
        return self.storage.get(name)


    def delete_file(self, name: str):
        return self.storage.pop(name, None)


    def find_file(self, prefix: str, suffix: str) -> list[str]:
        matches = []
        for name, size in self.storage.items():
            if name.startswith(prefix) and name.endswith(suffix):
                matches.append((name, size))

        matches.sort(key=lambda x: (-x[1], x[0]))
        return [f"{name}({size})" for name, size in matches]