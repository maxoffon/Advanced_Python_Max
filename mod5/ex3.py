class BlockErrors:
    def __init__(self, errors):
        self.errors = errors

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for cls in exc_type.__bases__:
            if cls in self.errors:
                return True
        return exc_type in self.errors
