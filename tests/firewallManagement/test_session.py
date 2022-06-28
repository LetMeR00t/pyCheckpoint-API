from box import Box
import requests
import responses
import pytest

from pycheckpoint.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_login_username_password(firewallManagement, session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        json=session,
        status=200,
    )

    resp = firewallManagement.session.login(
        username="test@example.com",
        password="hunter2",
        domain="MyDomain",
    )

    assert isinstance(resp, Box)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_login_api_key(firewallManagement, session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        json=session,
        status=200,
    )

    resp = firewallManagement.session.login(api_key="FFl8+KF1AJ2Tisac6d0K+w==")

    assert isinstance(resp, dict)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_login_missing_mandatory_parameters(firewallManagement, session):

    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.session.login(username="User1")
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.session.login(password="Password1")


@responses.activate
def test_logout(firewallManagement):
    delete_status = {"message": "OK"}
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/logout",
        json=delete_status,
        status=200,
    )

    resp = firewallManagement.session.logout()

    assert isinstance(resp, requests.Response)
    assert resp.status_code == 200
    assert resp.json()["message"] == "OK"


@responses.activate
def test_publish(firewallManagement):
    resp_publish = {"task-id": "01234567-89ab-cdef-a930-8c37a59972b3"}
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/publish",
        json=resp_publish,
        status=200,
    )

    resp = firewallManagement.session.publish()

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_discard(firewallManagement):
    resp_discard = {"message": "OK", "number-of-discarded-changes": 0}
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/discard",
        json=resp_discard,
        status=200,
    )

    resp = firewallManagement.session.discard()

    assert resp.message == "OK"


@responses.activate
def test_disconnect(firewallManagement):
    resp_disconnect = {"message": "OK"}
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/disconnect",
        json=resp_disconnect,
        status=200,
    )

    resp = firewallManagement.session.disconnect()

    assert resp.json()["message"] == "OK"


@responses.activate
def test_keepalive(firewallManagement):
    resp_keepalive = {"message": "OK"}
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/keepalive",
        json=resp_keepalive,
        status=200,
    )

    resp = firewallManagement.session.keepalive()

    assert resp.json()["message"] == "OK"


@responses.activate
def test_revert_to_revision(firewallManagement):
    resp_revert_to_revision = {"task-id": "01234567-89ab-cdef-a930-8c37a59972b3"}
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/revert-to-revision",
        json=resp_revert_to_revision,
        status=200,
    )

    resp = firewallManagement.session.revert_to_revision()

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_verify_revert(firewallManagement):
    resp_verify_revert = {"task-id": "01234567-89ab-cdef-a930-8c37a59972b3"}
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/verify-revert",
        json=resp_verify_revert,
        status=200,
    )

    resp = firewallManagement.session.verify_revert(
        to_session="d49ed10c-649a-476a-8e80-8282eda00e15"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_login_to_domain(firewallManagement, session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login-to-domain",
        json=session,
        status=200,
    )

    resp = firewallManagement.session.login_to_domain(domain="AnotherDomain")

    assert isinstance(resp, Box)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_show_session(firewallManagement):
    # Not all parameters from the response are tested here
    resp_show_session = {
        "name": "CustomName",
        "uid": "7a13a360-9b24-40d7-acd3-5b50247be33e",
    }
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-session",
        json=resp_show_session,
        status=200,
    )

    resp = firewallManagement.session.show_session()

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"


@responses.activate
def test_set_session(firewallManagement):
    # Not all parameters from the response are tested here
    resp_set_session = {
        "name": "CustomName",
        "uid": "7a13a360-9b24-40d7-acd3-5b50247be33e",
    }
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-session",
        json=resp_set_session,
        status=200,
    )

    resp = firewallManagement.session.set_session(
        description="This is my new description"
    )

    assert resp.uid == "7a13a360-9b24-40d7-acd3-5b50247be33e"
