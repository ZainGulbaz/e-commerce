class CustomError(Exception):
    def __init__(self, message, name):
        self.message = message
        self.name = name