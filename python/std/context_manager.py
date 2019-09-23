"""
https://www.python.org/dev/peps/pep-0343/
"""


class ExceptionRaised:
    """Helper for tests"""

    def __init__(self, exc):
        self.exc = exc

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        assert exc_type is not None
        assert self.exc is exc_type
        return True
