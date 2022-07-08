class MandatoryFieldMissing(Exception):
    """Exception raised when a mandatory field is missing

    Attributes:
        field (str): Field that is empty
        message (str): Custom string to show when the exception occurs
    """

    def __init__(
        self, field, message="This field has no value provided whereas it's mandatory"
    ):
        self.field = field
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.field} -> {self.message}"


class WrongType(Exception):
    """Exception raised when the type is not expected

    Attributes:
        value (str): Field that is concerned
        type (str): expected type
        message (str): Custom string to show when the exception occurs
    """

    def __init__(
        self,
        value: str,
        expected_type: str,
        message: str = "This value has not the expected type",
    ):
        self.value = value
        self.expected_type = expected_type
        self.message = (
            message
            + ": it's "
            + str(type(self.value))
            + " instead of "
            + str(self.expected_type)
        )
        super().__init__(self.message)

    def __str__(self):
        return f"{self.value} -> {self.message}"
