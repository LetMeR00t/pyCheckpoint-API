class MandatoryFieldMissing(Exception):
    """Exception raised when a mandatory field is missing"""

    def __init__(
        self,
        field: str,
        message: str = "This field has no value provided whereas it's mandatory",
    ):
        """Constructor of the class

        Args:
            field (str): Field that is empty
            message (str, optional): Custom string to show when the exception occurs.
            ... Defaults to "This field has no value provided whereas it's mandatory"


        Examples:
            >>> raise MandatoryFieldMissing("uid or name")

        """
        self.field = field
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.field} -> {self.message}"


class WrongType(Exception):
    """Exception raised when the type is not expected"""

    def __init__(
        self,
        value: str,
        expected_type: str,
        message: str = "This value has not the expected type",
    ):
        """Constructor of the class

        Args:
            value (str): Field that is concerned
            expected_type (str): Expected type
            message (str, optional): Custom string to show when the exception occurs.
            ... Defaults to "This value has not the expected type"


        Examples:
            >>> raise WrongType(value="value1", expected_type=int)

        """
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
