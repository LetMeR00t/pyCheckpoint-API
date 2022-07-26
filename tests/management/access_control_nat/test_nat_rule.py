import pytest
import responses

from pycheckpoint_api.management.exception import MandatoryFieldMissing


@responses.activate
def test_add_nat_rule(management, resp_nat_rule):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-nat-rule",
        json=resp_nat_rule,
        status=200,
    )

    resp = management.access_control_nat.nat_rule.add(
        package="standard",
        position="top",
        name="New NAT Rule 1",
        enabled=True,
        install_on="6c488338-8eec-4103-ad21-cd461ac2c476",
        method="static",
        original_destination="Any",
        original_service="New_TCP_Service_1",
        original_source="Any",
        translated_destination="Any",
        translated_service="New_TCP_Service_1",
        translated_source="Any",
    )

    assert resp.uid == "a5a88521-c996-a256-9625-b5a5d56c39ad"
    assert resp.name == "New NAT Rule 1"


@responses.activate
def test_show_nat_rule(management, resp_nat_rule):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-nat-rule",
        json=resp_nat_rule,
        status=200,
    )

    resp = management.access_control_nat.nat_rule.show(
        uid="a5a88521-c996-a256-9625-b5a5d56c39ad",
        package="standard",
    )

    assert resp.uid == "a5a88521-c996-a256-9625-b5a5d56c39ad"
    assert resp.name == "New NAT Rule 1"

    resp = management.access_control_nat.nat_rule.show(
        name="New NAT Rule 1",
        package="standard",
    )

    assert resp.uid == "a5a88521-c996-a256-9625-b5a5d56c39ad"
    assert resp.name == "New NAT Rule 1"

    resp = management.access_control_nat.nat_rule.show(
        rule_number=3,
        package="standard",
    )

    assert resp.uid == "a5a88521-c996-a256-9625-b5a5d56c39ad"
    assert resp.name == "New NAT Rule 1"

    # Missing mandatory parameter
    with pytest.raises(TypeError):
        management.access_control_nat.nat_rule.show(rule_number=3)

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        management.access_control_nat.nat_rule.show(package="standard")


@responses.activate
def test_set_nat_rule(management, resp_nat_rule):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-nat-rule",
        json=resp_nat_rule,
        status=200,
    )

    resp = management.access_control_nat.nat_rule.set(
        uid="a5a88521-c996-a256-9625-b5a5d56c39ad",
        new_name="New NAT Rule 1",
        new_position=3,
        package="standard",
        position="top",
        enabled=True,
        install_on="6c488338-8eec-4103-ad21-cd461ac2c476",
        method="static",
        original_destination="Any",
        original_service="New_TCP_Service_1",
        original_source="Any",
        translated_destination="Any",
        translated_service="New_TCP_Service_1",
        translated_source="Any",
    )

    assert resp.uid == "a5a88521-c996-a256-9625-b5a5d56c39ad"
    assert resp.name == "New NAT Rule 1"

    resp = management.access_control_nat.nat_rule.set(
        package="standard",
        name="New NAT Rule 1",
        new_position=3,
    )

    assert resp.uid == "a5a88521-c996-a256-9625-b5a5d56c39ad"
    assert resp.name == "New NAT Rule 1"

    resp = management.access_control_nat.nat_rule.set(
        package="standard",
        rule_number=4,
        new_position=3,
    )

    assert resp.uid == "a5a88521-c996-a256-9625-b5a5d56c39ad"
    assert resp.name == "New NAT Rule 1"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        management.access_control_nat.nat_rule.set(package="standard")


@responses.activate
def test_delete_nat_rule(management, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-nat-rule",
        json=resp_message_ok,
        status=200,
    )

    resp = management.access_control_nat.nat_rule.delete(
        package="standard", uid="a5a88521-c996-a256-9625-b5a5d56c39ad"
    )

    assert resp.message == "OK"

    resp = management.access_control_nat.nat_rule.delete(
        package="standard", name="New NAT Rule 1"
    )

    assert resp.message == "OK"

    resp = management.access_control_nat.nat_rule.delete(
        package="standard", rule_number=3
    )

    assert resp.message == "OK"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        management.access_control_nat.nat_rule.delete(package="standard")


@responses.activate
def test_show_nat_rulebase(management, resp_nat_rulebase):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-nat-rulebase",
        json=resp_nat_rulebase,
        status=200,
    )

    resp = management.access_control_nat.nat_rule.show_nat_rulebase(
        package="standard",
        offset=0,
        limit=20,
        order={"ASC": "name"},
        details_level="standard",
        use_object_dictionnary=True,
        filter_results="",
        filter_settings={},
    )

    assert isinstance(resp.total, int)
