import responses


@responses.activate
def test_add_lsv_profile(firewallManagement, resp_lsv_profile):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-lsv-profile",
        json=resp_lsv_profile,
        status=200,
    )

    resp = firewallManagement.network_objects.lsv_profile.add(
        name="New lsv-profile", certificate_authority="dedicated_profile_certificate"
    )

    assert resp.uid == "160de00a-c8b8-4cb4-ae4b-8623d0e6f8b6"
    assert resp.name == "New lsv-profile"


@responses.activate
def test_show_lsv_profile(firewallManagement, resp_lsv_profile):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-lsv-profile",
        json=resp_lsv_profile,
        status=200,
    )

    resp = firewallManagement.network_objects.lsv_profile.show(
        uid="160de00a-c8b8-4cb4-ae4b-8623d0e6f8b6"
    )

    assert resp.uid == "160de00a-c8b8-4cb4-ae4b-8623d0e6f8b6"
    assert resp.name == "New lsv-profile"


@responses.activate
def test_set_lsv_profile(firewallManagement, resp_lsv_profile):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-lsv-profile",
        json=resp_lsv_profile,
        status=200,
    )

    resp = firewallManagement.network_objects.lsv_profile.set(
        uid="160de00a-c8b8-4cb4-ae4b-8623d0e6f8b6", new_name="New lsv-profile"
    )

    assert resp.uid == "160de00a-c8b8-4cb4-ae4b-8623d0e6f8b6"
    assert resp.name == "New lsv-profile"


@responses.activate
def test_delete_lsv_profile(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-lsv-profile",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.lsv_profile.delete(
        uid="160de00a-c8b8-4cb4-ae4b-8623d0e6f8b6"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_lsv_profiles(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-lsv-profiles",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.lsv_profile.show_lsv_profiles()

    assert isinstance(resp.total, int)
