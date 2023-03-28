# Exception classes
class RabbitmqException(Exception):
    def __init__(self, message: str = "Error publishing message to RabbitMQ"):
        self.message = message
        super().__init__(self.message)

class DatabaseException(Exception):
    def __init__(self, message: str = "Error creating prontuario"):
        self.message = message
        super().__init__(self.message)

class BadRequestException(Exception):
    def __init__(self, message: str = "Invalid data in request"):
        self.message = message
        super().__init__(self.message)