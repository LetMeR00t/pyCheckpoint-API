import pytest
import responses
from box import Box

from pycheckpoint_api.management import Management
from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_login_logout(management, session, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        json=session,
        status=200,
    )
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/logout",
        json=resp_message_ok,
        status=200,
    )

    api = None
    with Management(
        hostname="127.0.0.1",
        port=443,
        user="test@example.com",
        password="hunter2",
        domain="MyDomain",
        version="1.5",
        ssl_verify=False,
    ) as api:

        assert (
            api._session.headers.get("X-chkp-sid")
            == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"
        )

    assert api._session.headers.get("X-chkp-sid") is None


@responses.activate
def test_login_user_password(management, session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        json=session,
        status=200,
    )

    resp = management.session.login(
        user="test@example.com",
        password="hunter2",
        domain="MyDomain",
    )

    assert isinstance(resp, Box)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_login_api_key(management, session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        json=session,
        status=200,
    )

    resp = management.session.login(api_key="FFl8+KF1AJ2Tisac6d0K+w==")

    assert isinstance(resp, dict)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_login_missing_mandatory_parameters(management):

    with pytest.raises(MandatoryFieldMissing):
        management.session.login(user="User1")
    with pytest.raises(MandatoryFieldMissing):
        management.session.login(password="Password1")
    with pytest.raises(MandatoryFieldMissing) as exception:
        management.session.login()
    assert "This field has no value provided whereas it's mandatory" in str(
        exception.value
    )


@responses.activate
def test_logout(management, resp_message_ok):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/logout",
        json=resp_message_ok,
        status=200,
    )

    resp = management.session.logout()

    assert resp.message == "OK"


@responses.activate
def test_publish(management, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/publish",
        json=resp_task,
        status=200,
    )

    # If we don't provide any UID, use the current one
    resp = management.session.publish()

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"

    # If we provide a specific UID, use this one
    resp = management.session.publish(uid="01234567-89ab-cdef-a930-8c37a59972b3")

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_discard(management, resp_message_ok_with_number_of_discarded_changes):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/discard",
        json=resp_message_ok_with_number_of_discarded_changes,
        status=200,
    )

    # If we don't provide any UID, use the current one
    resp = management.session.discard()

    assert resp.message == "OK"

    # If we provide a specific UID, use this one
    resp = management.session.discard(uid="01234567-89ab-cdef-a930-8c37a59972b3")

    assert resp.message == "OK"


@responses.activate
def test_disconnect(management, resp_message_ok):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/disconnect",
        json=resp_message_ok,
        status=200,
    )

    resp = management.session.disconnect(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")

    assert resp.message == "OK"


@responses.activate
def test_keepalive(management, resp_message_ok):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/keepalive",
        json=resp_message_ok,
        status=200,
    )

    resp = management.session.keepalive()

    assert resp.message == "OK"


@responses.activate
def test_revert_to_revision(management, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/revert-to-revision",
        json=resp_task,
        status=200,
    )

    # If we don't provide any UID, use the current one
    resp = management.session.revert_to_revision()

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"

    # If we provide a specific UID, use this one
    resp = management.session.revert_to_revision(
        to_session="7a13a360-9b24-40d7-acd3-5b50247be33e"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_verify_revert(management, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/verify-revert",
        json=resp_task,
        status=200,
    )

    resp = management.session.verify_revert(
        to_session="d49ed10c-649a-476a-8e80-8282eda00e15"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_login_to_domain(management, session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login-to-domain",
        json=session,
        status=200,
    )

    resp = management.session.login_to_domain(domain="AnotherDomain")

    assert isinstance(resp, Box)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_show_session(management, resp_session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-session",
        json=resp_session,
        status=200,
    )

    # If we don't provide any UID, use the current one
    resp = management.session.show_session()

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"

    # If we provide a specific UID, use this one
    resp = management.session.show_session(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_set_session(management, resp_session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-session",
        json=resp_session,
        status=200,
    )

    resp = management.session.set_session(
        description="This is my new description",
        new_name="MySession",
        tags=["t1", "t2"],
    )

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_purge_published_sessions(management, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/purge-published-sessions",
        json=resp_task,
        status=200,
    )

    resp = management.session.purge_published_sessions(number_of_sessions_to_preserve=5)

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"

    resp = management.session.purge_published_sessions(
        preserve_to_date="2022-07-10T11:43:07.931Z"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"

    with pytest.raises(MandatoryFieldMissing):
        management.session.purge_published_sessions()


@responses.activate
def test_switch_session(management, resp_session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/switch-session",
        json=resp_session,
        status=200,
    )

    resp = management.session.switch_session(uid="7a13a360-9b24-40d7-acd3-5b50247be33e")

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"

    with pytest.raises(TypeError):
        management.session.switch_session()


@responses.activate
def test_take_over_session(management, resp_session):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/take-over-session",
        json=resp_session,
        status=200,
    )

    resp = management.session.take_over_session(
        uid="7a13a360-9b24-40d7-acd3-5b50247be33e", disconnect_active_session=True
    )

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_show_sessions(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-sessions",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.session.show_sessions(
        filter_results="session_", order=[{"ASC": "name"}], view_published_sessions=True
    )

    assert isinstance(resp.total, int)


@responses.activate
def test_continue_session_in_smartconsole(management, resp_message_ok):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/continue-session-in-smartconsole",
        json=resp_message_ok,
        status=200,
    )

    resp = management.session.continue_session_in_smartconsole()

    assert resp.message == "OK"


@responses.activate
def test_show_last_published_session(management, resp_session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-last-published-session",
        json=resp_session,
        status=200,
    )

    resp = management.session.show_last_published_session()

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_show_login_message(management, resp_login_message):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-login-message",
        json=resp_login_message,
        status=200,
    )

    resp = management.session.show_login_message()

    assert resp.message == "C"


@responses.activate
def test_set_login_message(management, resp_login_message):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-login-message",
        json=resp_login_message,
        status=200,
    )

    resp = management.session.set_login_message(
        header="D", message="C", show_message=True, warning=True
    )

    assert resp.header == "D"


@responses.activate
def test_set_automatic_purge(management, resp_automatic_purge):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-automatic-purge",
        json=resp_automatic_purge,
        status=200,
    )

    resp = management.session.set_automatic_purge(
        enabled=True,
        number_of_sessions_to_keep=10,
        scheduling={
            "start-date": "2022-07-10T11:43:07.931Z",
            "time-units": "hours",
            "check-interval": 24,
        },
    )

    assert resp.enabled is True
    assert resp.number_of_sessions_to_keep == "10"


@responses.activate
def test_show_automatic_purge(management, resp_automatic_purge):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-automatic-purge",
        json=resp_automatic_purge,
        status=200,
    )

    resp = management.session.show_automatic_purge()

    assert resp.enabled is True
    assert resp.number_of_sessions_to_keep == "10"
