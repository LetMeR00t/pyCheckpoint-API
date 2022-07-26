import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing
from pycheckpoint_api.models import Color


@responses.activate
def test_add_policy_package(management, resp_package):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-package",
        json=resp_package,
        status=200,
    )

    resp = management.policy.package.add(
        name="New_Standard_Package_1",
        comments="My Comments",
        color=Color.GREEN,
        threat_prevention=False,
        access=True,
        desktop_security=False,
        installation_targets="all",
        qos=False,
        qos_policy_type="recommanded",
        tags=["t1"],
        vpn_traditional_mode=False,
    )

    assert resp.uid == "38b4ed6e-711c-49fa-b9f4-638290d621be"
    assert resp.name == "New Standard Package 1"


@responses.activate
def test_show_policy_package(management, resp_package):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-package",
        json=resp_package,
        status=200,
    )

    resp = management.policy.package.show(uid="38b4ed6e-711c-49fa-b9f4-638290d621be")

    assert resp.uid == "38b4ed6e-711c-49fa-b9f4-638290d621be"
    assert resp.name == "New Standard Package 1"

    resp = management.policy.package.show(name="New Standard Package 1")

    assert resp.uid == "38b4ed6e-711c-49fa-b9f4-638290d621be"
    assert resp.name == "New Standard Package 1"

    with pytest.raises(MandatoryFieldMissing):
        management.policy.package.show()


@responses.activate
def test_set_host(management, resp_package):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-package",
        json=resp_package,
        status=200,
    )

    resp = management.policy.package.set(
        uid="38b4ed6e-711c-49fa-b9f4-638290d621be",
        new_name="New Standard Package 1",
        comments="My Comments",
        color=Color.GREEN,
        threat_prevention=False,
        access=True,
        access_layers={"name": "New Standard Package 1 Network"},
        desktop_security=False,
        installation_targets="all",
        https_layer="",
        qos=False,
        qos_policy_type="recommanded",
        tags=["t1"],
        vpn_traditional_mode=False,
    )

    assert resp.uid == "38b4ed6e-711c-49fa-b9f4-638290d621be"
    assert resp.name == "New Standard Package 1"

    resp = management.policy.package.set(
        name="New Standard Package 1 Old",
        new_name="New Standard Package 1",
    )

    assert resp.uid == "38b4ed6e-711c-49fa-b9f4-638290d621be"
    assert resp.name == "New Standard Package 1"

    with pytest.raises(MandatoryFieldMissing):
        management.policy.package.set()


@responses.activate
def test_delete_package(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-package",
        json=resp_message_ok,
        status=200,
    )

    resp = management.policy.package.delete(uid="38b4ed6e-711c-49fa-b9f4-638290d621be")

    assert resp.message == "OK"

    resp = management.policy.package.delete(name="New Standard Package 1")

    assert resp.message == "OK"

    with pytest.raises(MandatoryFieldMissing):
        management.policy.package.delete()


@responses.activate
def test_show_packages(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-packages",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.policy.package.show_packages(
        filter_results="", order={"ASC": "name"}
    )

    assert isinstance(resp.total, int)
