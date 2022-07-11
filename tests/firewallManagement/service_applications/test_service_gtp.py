import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_gtp(firewallManagement, resp_service_gtp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-gtp",
        json=resp_service_gtp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_gtp.add(
        name="New_gtp_Service_1",
        version="v2",
        access_point_name={"enable": False},
        allow_usage_of_static_ip=True,
        apply_access_policy_on_user_traffic={
            "enable": False,
            "add-imsi-field-to-log": False,
        },
        cs_fallback_and_srvcc=False,
        imsi_prefix={"enable": True, "prefix": "313460000000001"},
        interface_profile={
            "profile": {
                "uid": "b458696d-8967-469c-91cc-c6162c14cb27",
                "name": "Any",
                "type": "GTPInterfaceProfile",
                "domain": {
                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                    "name": "Check Point Data",
                    "domain-type": "data domain",
                },
            }
        },
        ldap_group={"enable": False, "according-to": "MS-ISDN"},
        ms_isdn={"enable": False, "ms-isdn": "1"},
        radio_access_technology={
            "utran": False,
            "geran": False,
            "wlan": False,
            "gan": False,
            "hspa-evolution": False,
            "eutran": False,
            "virtual": False,
            "nb-iot": False,
            "other-types-range": {"enable": False, "types": ""},
        },
        restoration_and_recovery=False,
        reverse_service=False,
        selection_mode={"enable": True, "mode": 2},
        trace_management=True,
        tags=["t1"],
    )

    assert resp.uid == "70e390d7-b070-4d6e-b8d7-53b7f6cc7fe6"
    assert resp.name == "New_gtp_Service_1"


@responses.activate
def test_show_service_gtp(firewallManagement, resp_service_gtp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-gtp",
        json=resp_service_gtp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_gtp.show(
        uid="70e390d7-b070-4d6e-b8d7-53b7f6cc7fe6"
    )

    assert resp.uid == "70e390d7-b070-4d6e-b8d7-53b7f6cc7fe6"
    assert resp.name == "New_gtp_Service_1"


@responses.activate
def test_set_service_gtp(firewallManagement, resp_service_gtp):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-gtp",
        json=resp_service_gtp,
        status=200,
    )

    resp = firewallManagement.service_applications.service_gtp.set(
        uid="70e390d7-b070-4d6e-b8d7-53b7f6cc7fe6",
        new_name="New_gtp_Service_1",
        version="v2",
        access_point_name={"enable": False},
        allow_usage_of_static_ip=True,
        apply_access_policy_on_user_traffic={
            "enable": False,
            "add-imsi-field-to-log": False,
        },
        cs_fallback_and_srvcc=False,
        imsi_prefix={"enable": True, "prefix": "313460000000001"},
        interface_profile={
            "profile": {
                "uid": "b458696d-8967-469c-91cc-c6162c14cb27",
                "name": "Any",
                "type": "GTPInterfaceProfile",
                "domain": {
                    "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
                    "name": "Check Point Data",
                    "domain-type": "data domain",
                },
            }
        },
        ldap_group={"enable": False, "according-to": "MS-ISDN"},
        ms_isdn={"enable": False, "ms-isdn": "1"},
        radio_access_technology={
            "utran": False,
            "geran": False,
            "wlan": False,
            "gan": False,
            "hspa-evolution": False,
            "eutran": False,
            "virtual": False,
            "nb-iot": False,
            "other-types-range": {"enable": False, "types": ""},
        },
        restoration_and_recovery=False,
        reverse_service=False,
        selection_mode={"enable": True, "mode": 2},
        trace_management=True,
        tags=["t1"],
    )

    assert resp.uid == "70e390d7-b070-4d6e-b8d7-53b7f6cc7fe6"
    assert resp.name == "New_gtp_Service_1"

    resp = firewallManagement.service_applications.service_gtp.set(
        name="New_gtp_Service_1",
        allow_usage_of_static_ip=True,
    )

    assert resp.uid == "70e390d7-b070-4d6e-b8d7-53b7f6cc7fe6"
    assert resp.name == "New_gtp_Service_1"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.service_gtp.set()


@responses.activate
def test_delete_service_gtp(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-gtp",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.service_gtp.delete(
        uid="70e390d7-b070-4d6e-b8d7-53b7f6cc7fe6"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_gtp(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-gtp",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.service_applications.service_gtp.show_services_gtp()

    assert isinstance(resp.total, int)
