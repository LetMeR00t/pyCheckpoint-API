import sys

# Add support for Python 3.7
if sys.version_info > (3, 8):
    from typing import Union, get_origin
else:
    from typing import Union, List

from pycheckpoint_api.firewallManagement.exception import (
    MandatoryFieldMissing,
    WrongType,
)


def sanitize_value(field: str, t: type, is_mandatory: bool = False, default=None, **kw):
    """This function is used to sanitize the value from a kv dictionnary (default value, type etc.)"""
    # Get the value
    value = kw.get(field, default)
    # If it's mandatory and the value is not provided, raise an exception
    if value is None and is_mandatory:
        raise MandatoryFieldMissing(field)
    # Otherwise, it means that the parameter is not mandatory or the value is set
    # Check also if the type is Union.
    origin = None
    if sys.version_info > (3, 8):
        origin = get_origin(t)
        final_type = [Union]
    else:
        origin = t
        final_type = [
            Union[str, List[str]],
            Union[dict, str, List[str]],
            Union[dict, List[dict]],
        ]
    if origin in final_type:
        if value is None or type(value) in t.__args__:
            return value
        else:
            raise WrongType(value=value, expected_type=t)
    elif value is None or isinstance(value, t):
        return value
    else:
        raise WrongType(value=value, expected_type=t)


def sanitize_secondary_parameters(d: dict, **kw):
    """This function is used to sanitize any secondary parameter (meaning not mandatory parameters)"""
    payload = {}
    for field, field_type in d.items():
        value = sanitize_value(field=field_type, t=type, is_mandatory=False, **kw)
        if value is not None:
            payload[field] = value
    return payload
