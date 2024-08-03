class LoginError(Exception):
    def __init__(self, message="An error occurred during login"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class EmptyFieldError(LoginError):
    def __init__(self, message="Fields cannot be empty"):
        super().__init__(message)

class IncorrectPasswordError(LoginError):
    def __init__(self, message="Incorrect password"):
        super().__init__(message)

class InvalidUsernameError(LoginError):
    def __init__(self, message="Invalid username"):
        super().__init__(message)


class SignupError(Exception):
    def __init__(self, message="An error occurred during signup"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class EmptyFieldError(SignupError):
    def __init__(self, message="Fields cannot be empty"):
        super().__init__(message)

class UsernameTakenError(SignupError):
    def __init__(self, message="Username already taken"):
        super().__init__(message)