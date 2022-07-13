import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_nat_section(firewallManagement, resp_nat_section):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-nat-section",
        json=resp_nat_section,
        status=200,
    )

    resp = firewallManagement.access_control_nat.nat_section.add(
        package="standard",
        position=1,
        name="New NAT Section 1",
    )

    assert resp.uid == "bb89a652-369a-2884-dd59-f69ea241567cd"
    assert resp.name == "New NAT Section 1"


@responses.activate
def test_show_nat_section(firewallManagement, resp_nat_section):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-nat-section",
        json=resp_nat_section,
        status=200,
    )

    resp = firewallManagement.access_control_nat.nat_section.show(
        uid="bb89a652-369a-2884-dd59-f69ea241567cd", package="standard"
    )

    assert resp.uid == "bb89a652-369a-2884-dd59-f69ea241567cd"
    assert resp.name == "New NAT Section 1"

    resp = firewallManagement.access_control_nat.nat_section.show(
        name="My Rule", package="standard"
    )

    assert resp.uid == "bb89a652-369a-2884-dd59-f69ea241567cd"
    assert resp.name == "New NAT Section 1"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.nat_section.show(package="standard")


@responses.activate
def test_set_nat_section(firewallManagement, resp_nat_section):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-nat-section",
        json=resp_nat_section,
        status=200,
    )

    resp = firewallManagement.access_control_nat.nat_section.set(
        package="standard",
        uid="bb89a652-369a-2884-dd59-f69ea241567cd",
        new_name="New NAT Section 1",
    )

    assert resp.uid == "bb89a652-369a-2884-dd59-f69ea241567cd"
    assert resp.name == "New NAT Section 1"

    resp = firewallManagement.access_control_nat.nat_section.set(
        package="standard", name="New NAT Section 1 Old", new_name="New NAT Section 1"
    )

    assert resp.uid == "bb89a652-369a-2884-dd59-f69ea241567cd"
    assert resp.name == "New NAT Section 1"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.nat_section.set(package="standard")


@responses.activate
def test_delete_nat_section(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-nat-section",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.access_control_nat.nat_section.delete(
        package="standard", uid="bb89a652-369a-2884-dd59-f69ea241567cd"
    )

    assert resp.message == "OK"

    resp = firewallManagement.access_control_nat.nat_section.delete(
        package="standard", name="New NAT Section 1"
    )

    assert resp.message == "OK"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.nat_section.delete(package="standard")
