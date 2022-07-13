import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_access_rule(firewallManagement, resp_access_rule):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-access-rule",
        json=resp_access_rule,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_rule.add(
        layer="Network",
        position=1,
        name="Rule 1",
        action="Drop",
        action_settings={"enable-identity-captive-portal": False},
        content={},
        content_direction="any",
        content_negate=False,
        custom_fields={"field-1": "", "field-2": "", "field-3": ""},
        destination="Any",
        destination_negate=False,
        enabled=True,
        inline_layer="Inline",
        install_on="Policy Targets",
        service="smtp",
        service_negate=False,
        service_resource="",
        source="Any",
        source_negate=False,
        time=[{"uid": "aa785d6d-7785-aad5-36a3-ab2d74c966ee"}],
        track="",
        user_check="",
        vpn={"community": ["MyIntranet"]},
    )

    assert resp.uid == "1df8a4b0-fa8b-428b-b649-626b74bf7f81"
    assert resp.name == "Rule 1"
    assert resp.action.name == "Drop"


@responses.activate
def test_show_access_rule(firewallManagement, resp_access_rule):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-access-rule",
        json=resp_access_rule,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_rule.show(
        uid="1df8a4b0-fa8b-428b-b649-626b74bf7f81",
        layer="MyLayer",
        show_as_ranges=False,
        show_hits=True,
        hits_settings="",
    )

    assert resp.uid == "1df8a4b0-fa8b-428b-b649-626b74bf7f81"
    assert resp.name == "Rule 1"

    resp = firewallManagement.access_control_nat.access_rule.show(
        name="My Rule", layer="MyLayer"
    )

    assert resp.uid == "1df8a4b0-fa8b-428b-b649-626b74bf7f81"
    assert resp.name == "Rule 1"

    resp = firewallManagement.access_control_nat.access_rule.show(
        rule_number=3, layer="MyLayer"
    )

    assert resp.uid == "1df8a4b0-fa8b-428b-b649-626b74bf7f81"
    assert resp.name == "Rule 1"

    # Missing mandatory parameter
    with pytest.raises(TypeError):
        firewallManagement.access_control_nat.access_rule.show(rule_number=3)

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_rule.show(layer="Network")


@responses.activate
def test_set_access_rule(firewallManagement, resp_access_rule):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-access-rule",
        json=resp_access_rule,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_rule.set(
        uid="1df8a4b0-fa8b-428b-b649-626b74bf7f81",
        new_name="Rule 1",
        new_position=3,
        layer="Network",
        action="Drop",
        action_settings={"enable-identity-captive-portal": False},
        content={},
        content_direction="any",
        content_negate=False,
        custom_fields={"field-1": "", "field-2": "", "field-3": ""},
        destination="Any",
        destination_negate=False,
        enabled=True,
        inline_layer="Inline",
        install_on="Policy Targets",
        service="smtp",
        service_negate=False,
        service_resource="",
        source="Any",
        source_negate=False,
        time=[{"uid": "aa785d6d-7785-aad5-36a3-ab2d74c966ee"}],
        track="",
        user_check="",
        vpn={"community": ["MyIntranet"]},
    )

    assert resp.uid == "1df8a4b0-fa8b-428b-b649-626b74bf7f81"
    assert resp.name == "Rule 1"

    resp = firewallManagement.access_control_nat.access_rule.set(
        layer="Network",
        name="Rule 1",
        new_position=3,
    )

    assert resp.uid == "1df8a4b0-fa8b-428b-b649-626b74bf7f81"
    assert resp.name == "Rule 1"

    resp = firewallManagement.access_control_nat.access_rule.set(
        layer="Network",
        rule_number=4,
        new_position=3,
    )

    assert resp.uid == "1df8a4b0-fa8b-428b-b649-626b74bf7f81"
    assert resp.name == "Rule 1"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_rule.set(layer="Network")


@responses.activate
def test_delete_access_rule(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-access-rule",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_rule.delete(
        layer="Network", uid="1df8a4b0-fa8b-428b-b649-626b74bf7f81"
    )

    assert resp.message == "OK"

    resp = firewallManagement.access_control_nat.access_rule.delete(
        layer="Network", name="Rule 1"
    )

    assert resp.message == "OK"

    resp = firewallManagement.access_control_nat.access_rule.delete(
        layer="Network", rule_number=3
    )

    assert resp.message == "OK"

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_rule.delete(layer="Network")


@responses.activate
def test_show_access_rulebase(firewallManagement, resp_access_rulebase):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-access-rulebase",
        json=resp_access_rulebase,
        status=200,
    )

    resp = firewallManagement.access_control_nat.access_rule.show_access_rulebase(
        name="Network",
        offset=0,
        limit=20,
        order={"ASC": "name"},
        package="",
        details_level="standard",
        show_as_ranges=True,
        use_object_dictionnary=True,
        filter_results="",
        filter_settings={},
        show_hits=True,
        hits_settings={
            "from-date": "2014-01-01",
            "to-date": "2014-12-31T23:59",
            "target": "corporate-gw",
        },
    )

    assert isinstance(resp.total, int)

    resp = firewallManagement.access_control_nat.access_rule.show_access_rulebase(
        uid="21127e7c-d19b-4c65-b9c3-8e20e66ea1ae"
    )

    assert isinstance(resp.total, int)

    # Missing mandatory parameter
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.access_control_nat.access_rule.show_access_rulebase()
