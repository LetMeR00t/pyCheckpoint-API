from typing import List, Union

import pytest

from pycheckpoint_api.firewallManagement.exception import (
    MandatoryFieldMissing,
    WrongType,
)
from pycheckpoint_api.utils import sanitize_secondary_parameters, sanitize_value


def test_sanitize_value():

    # Normal test, no issue
    kw = {"field1": "value1"}
    result = sanitize_value(
        field="field1", t=str, is_mandatory=False, default=None, **kw
    )

    assert result == "value1"

    # Mandatory field missing
    kw = {"field1": "value1"}
    with pytest.raises(MandatoryFieldMissing):
        result = sanitize_value(
            field="field2", t=str, is_mandatory=True, default=None, **kw
        )

    # Wrong type
    kw = {"field1": "value1"}
    with pytest.raises(WrongType):
        result = sanitize_value(
            field="field1", t=int, is_mandatory=False, default=None, **kw
        )

    # No mandatory field doesn't exist, should return None
    kw = {"field1": "value1"}
    result = sanitize_value(
        field="field2", t=str, is_mandatory=False, default=None, **kw
    )

    assert result is None

    # Union field used, should be acceptable if the type is in the Union
    kw = {"field1": "value1"}
    result = sanitize_value(
        field="field1", t=Union[str, List[str]], is_mandatory=False, default=None, **kw
    )

    assert result == "value1"

    # Union field used, but with the wrong type (not in Union)
    kw = {"field1": 1}
    with pytest.raises(WrongType) as exception:
        result = sanitize_value(
            field="field1",
            t=Union[str, List[str]],
            is_mandatory=False,
            default=None,
            **kw
        )
    assert "This value has not the expected type" in str(exception.value)

    # Union field used, having the specific case of using a typing.List object instead of list
    kw = {"field1": ["value1", "value2"]}
    result = sanitize_value(
        field="field1", t=Union[str, List[str]], is_mandatory=False, default=None, **kw
    )

    assert result == ["value1", "value2"]


def test_sanitize_secondary_parameters():

    # Normal use case
    d = {"field1": str}
    kw = {"field1": "value1"}
    result = sanitize_secondary_parameters(d=d, **kw)

    assert result == kw

    # Normal use case, avoiding unused/unexpected information
    d = {"field1": str}
    kw = {"field1": "value1", "field2": "value2"}
    result = sanitize_secondary_parameters(d=d, **kw)

    assert result == {"field1": "value1"}
