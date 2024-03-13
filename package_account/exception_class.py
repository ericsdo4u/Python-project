class InvalidPinException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidAccountNumberException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InsufficientFundException(Exception):
    def __init__(self, message):
        super().__init__(message)

