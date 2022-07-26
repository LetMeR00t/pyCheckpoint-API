import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_abort_get_interfaces(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/abort-get-interfaces",
        json=resp_message_ok,
        status=200,
    )

    resp = management.network_objects.network_interface.abort_get_interfaces(
        task_id="01234567-89ab-cdef-a930-8c37a59972b3"
    )

    assert resp.message == "OK"


@responses.activate
def test_get_interfaces(management, resp_get_interfaces):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/get-interfaces",
        json=resp_get_interfaces,
        status=200,
    )

    resp = management.network_objects.network_interface.get_interfaces(
        target_name="gw123", with_topology=True
    )

    assert resp.tasks[0].task_id == "01234567-89ab-cdef-9e1f-0e1e68312345"

    resp = management.network_objects.network_interface.get_interfaces(
        target_uid="aa5d2edc-a588-5bb5-2365-15a2cd52e6dd", with_topology=True
    )

    assert resp.tasks[0].task_id == "01234567-89ab-cdef-9e1f-0e1e68312345"

    # Missing mask information
    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.network_interface.get_interfaces()
