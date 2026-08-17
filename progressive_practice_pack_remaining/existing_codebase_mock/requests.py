from models import Request


def expand_leaves(request: Request) -> list[Request]:
    if request.children:
        return list(request.children)
    return []
