import sys

# Add support for Python 3.7
if sys.version_info > (3, 8):
    from typing import Dict, List, Union, get_origin, Any
else:
    from typing import Union, List, Dict, Any

from pycheckpoint_api.firewallManagement.exception import (
    MandatoryFieldMissing,
    WrongType,
)


def sanitize_value(
    field: str, t: type, is_mandatory: bool = False, default: Any = None, **kw
) -> Any:
    """This function is used to sanitize the value from a keyword dictionnary (such as default value, type etc.)

    Args:
        field (str): Name of the field to sanitize
        t (type): Expected type from the given ``field``
        is_mandatory (bool, optional): Indicates if ``field`` is mandatory. Defaults to False
        default (:obj:`Any`, optional): Default value for ``field`` if any. Defaults to None
        **kw (dict, required): The ``field`` value will be extracted from the provided keyword aguments

    Raises:
        MandatoryFieldMissing: The value is not given as a keyword parameter and it's mandatory
        WrongType: If ``t`` is not equals to the value type for the given field

    Returns:
        :obj:`Any`: the value for the given field if all checks passed

    Examples:
        >>> sanitize_value(field="field1", t=str, is_mandatory=False,
            ... default=None, {"field1": "value1"})
        "value1"

        >>> sanitize_value(field="field1", t=int, is_mandatory=False, default=None, {"field1": "value1"})
        # Exception raised as "value1" is not an integer
    """
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
        elif (isinstance(value, list) and List[str] in t.__args__) or (
            isinstance(value, dict) and Dict[str] in t.__args__
        ):
            return value
        else:
            raise WrongType(value=value, expected_type=t)
    elif value is None or isinstance(value, t):
        return value
    else:
        raise WrongType(value=value, expected_type=t)


def sanitize_secondary_parameters(d: dict, **kw) -> dict:
    """This function is used to sanitize any secondary parameter (meaning not mandatory parameters)

    Args:
        d (dict): A dictionnary with a list of parameters to sanitize
        **kw (dict, required): Arbitrary keyword arguments for secondary parameters.

    Returns:
        dict: a sanitized dictionnary with secondary parameters

    Examples:
        >>> d = {"field1": str}
        >>> kw = {"field1": "value1"}
        >>> sanitize_secondary_parameters(d=d, **kw)
        {"field1": "value1"}

        >>> d = {"field1": str}
        >>> kw = {"field1": "value1", "field2": "value2"}
        >>> sanitize_secondary_parameters(d=d, **kw)
        {"field1": "value1"}
    """
    payload = {}
    for field, field_type in d.items():
        value = sanitize_value(field=field, t=field_type, is_mandatory=False, **kw)
        if value is not None:
            payload[field] = value
    return payload
