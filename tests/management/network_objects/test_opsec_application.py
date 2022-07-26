import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_opsec_application(management, resp_opsec_application):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-opsec-application",
        json=resp_opsec_application,
        status=200,
    )

    resp = management.network_objects.opsec_application.add(
        name="MyOpsecApplication",
        host="SomeHost",
        cpmi={
            "enabled": "true",
            "use-administrator-credentials": "false",
            "administrator-profile": "Super User",
        },
        lea={"enabled": "false"},
        one_time_password="SomePassword",
        tags=["t1"],
    )

    assert resp.uid == "1741bb6c-3b19-456c-a635-b96c8456a0e8"
    assert resp.name == "MyOpsecApplication"


@responses.activate
def test_show_opsec_application(management, resp_opsec_application):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-opsec-application",
        json=resp_opsec_application,
        status=200,
    )

    resp = management.network_objects.opsec_application.show(
        uid="1741bb6c-3b19-456c-a635-b96c8456a0e8"
    )

    assert resp.uid == "1741bb6c-3b19-456c-a635-b96c8456a0e8"
    assert resp.name == "MyOpsecApplication"


@responses.activate
def test_set_opsec_application(management, resp_opsec_application):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-opsec-application",
        json=resp_opsec_application,
        status=200,
    )

    resp = management.network_objects.opsec_application.set(
        uid="1741bb6c-3b19-456c-a635-b96c8456a0e8",
        new_name="MyOpsecApplication",
        host="SomeHost",
        cpmi={
            "enabled": "true",
            "use-administrator-credentials": "false",
            "administrator-profile": "Super User",
        },
        lea={"enabled": "false"},
        one_time_password="SomePassword",
        tags=["t1"],
    )

    assert resp.uid == "1741bb6c-3b19-456c-a635-b96c8456a0e8"
    assert resp.name == "MyOpsecApplication"

    resp = management.network_objects.opsec_application.set(
        name="MyOpsecApplication Old", new_name="MyOpsecApplication"
    )

    assert resp.uid == "1741bb6c-3b19-456c-a635-b96c8456a0e8"
    assert resp.name == "MyOpsecApplication"

    # Missing name or UID information
    with pytest.raises(MandatoryFieldMissing):
        management.network_objects.opsec_application.set()


@responses.activate
def test_delete_opsec_application(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-opsec-application",
        json=resp_message_ok,
        status=200,
    )

    resp = management.network_objects.opsec_application.delete(
        uid="1741bb6c-3b19-456c-a635-b96c8456a0e8"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_opsec_applications(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-opsec-applications",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.network_objects.opsec_application.show_opsec_applications()

    assert isinstance(resp.total, int)
