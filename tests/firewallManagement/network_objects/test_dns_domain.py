import responses


@responses.activate
def test_add_dns_domain(firewallManagement, resp_dns_domain):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-dns-domain",
        json=resp_dns_domain,
        status=200,
    )

    resp = firewallManagement.network_objects.dns_domain.add(
        name=".www.example.com", is_sub_domain=False
    )

    assert resp.uid == "ea6b168b-87d8-4ab6-9a8c-89c422dbde88"
    assert resp.name == ".www.example.com"


@responses.activate
def test_show_dns_domain(firewallManagement, resp_dns_domain):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-dns-domain",
        json=resp_dns_domain,
        status=200,
    )

    resp = firewallManagement.network_objects.dns_domain.show(
        uid="ea6b168b-87d8-4ab6-9a8c-89c422dbde88"
    )

    assert resp.uid == "ea6b168b-87d8-4ab6-9a8c-89c422dbde88"
    assert resp.name == ".www.example.com"


@responses.activate
def test_set_dns_domain(firewallManagement, resp_dns_domain):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-dns-domain",
        json=resp_dns_domain,
        status=200,
    )

    resp = firewallManagement.network_objects.dns_domain.set(
        uid="ea6b168b-87d8-4ab6-9a8c-89c422dbde88", new_name=".www.example.com"
    )

    assert resp.uid == "ea6b168b-87d8-4ab6-9a8c-89c422dbde88"
    assert resp.name == ".www.example.com"


@responses.activate
def test_delete_dns_domain(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-dns-domain",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.dns_domain.delete(
        uid="ea6b168b-87d8-4ab6-9a8c-89c422dbde88"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_dns_domains(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-dns-domains",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.dns_domain.show_dns_domains()

    assert isinstance(resp.total, int)
