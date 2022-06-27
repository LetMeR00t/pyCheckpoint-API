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
