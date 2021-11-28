class errors(Exception):
    """Base custom exception class"""
    def __init__(self, message):
        self.message = message

class EmptyInputError(errors):
    """Throws when an input is empty.
    
    Attributes:
    - message: the error message."""
    def __init__(self, message):
        super().__init__(message)

class PasswordError(errors):
    """Throws when an input is empty.
    
    Attributes:
    - message: the error message."""
    def __init__(self, message):
        super().__init__(message)