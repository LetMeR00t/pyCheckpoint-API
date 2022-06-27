import responses


@responses.activate
def test_create(firewallManagement, session):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/login",
        json=session,
        status=200,
    )

    resp = firewallManagement.session.create(
        username="test@example.com", password="hunter2", domain="MyDomain"
    )

    assert isinstance(resp, dict)
    assert resp.sid == "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"


@responses.activate
def test_delete(firewallManagement):
    delete_status = {"message": "OK"}
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/logout",
        json=delete_status,
        status=200,
    )

    resp = firewallManagement.session.delete()

    assert isinstance(resp, int)
    assert resp == 200
