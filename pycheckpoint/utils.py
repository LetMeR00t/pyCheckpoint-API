from pycheckpoint.firewallManagement.exception import MandatoryFieldMissing, WrongType


def sanitize_value(
    field: str, type: type, is_mandatory: bool = False, default=None, **kw
):
    """This function is used to sanitize the value from a kv dictionnary (default value, type etc.)"""
    # Get the value
    value = kw.get(field, default)
    # If it's mandatory and the value is not provided, raise an exception
    if is_mandatory and value is None:
        raise MandatoryFieldMissing(field)
    # Otherwise, it means that the parameter is not mandatory or the value is set
    if isinstance(value, type) or value is None:
        return value
    else:
        raise WrongType(value=value, expected_type=type)
