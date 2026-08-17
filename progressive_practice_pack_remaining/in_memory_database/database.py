class InMemoryDatabase:
    """
    Progressive in-memory database practice problem.

    Implement only the behavior required by the levels you are currently practicing.
    """

    def __init__(self):
        # TODO
        pass

    # Level 1
    def set(self, key: str, field: str, value: int) -> None:
        # TODO
        pass

    def get(self, key: str, field: str):
        # TODO
        pass

    def delete(self, key: str, field: str) -> bool:
        # TODO
        pass

    # Level 2
    def scan(self, key: str) -> list[str]:
        # TODO
        pass

    def scan_by_prefix(self, key: str, prefix: str) -> list[str]:
        # TODO
        pass

    # Level 3
    def set_at(self, key: str, field: str, value: int, timestamp: int) -> None:
        # TODO
        pass

    def set_at_with_ttl(
        self,
        key: str,
        field: str,
        value: int,
        timestamp: int,
        ttl: int,
    ) -> None:
        # TODO
        pass

    def get_at(self, key: str, field: str, timestamp: int):
        # TODO
        pass

    def delete_at(self, key: str, field: str, timestamp: int) -> bool:
        # TODO
        pass

    def scan_at(self, key: str, timestamp: int) -> list[str]:
        # TODO
        pass

    def scan_by_prefix_at(
        self,
        key: str,
        prefix: str,
        timestamp: int,
    ) -> list[str]:
        # TODO
        pass

    # Level 4
    def backup(self, timestamp: int) -> int:
        # TODO
        pass

    def restore(self, timestamp: int, restore_timestamp: int) -> None:
        # TODO
        pass
