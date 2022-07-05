import responses


@responses.activate
def test_add_simple_cluster(firewallManagement, resp_task):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-simple-cluster",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.add(
        name="cluster1", ip_address="17.23.5.1"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_show_simple_cluster(firewallManagement, resp_simple_cluster):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-simple-cluster",
        json=resp_simple_cluster,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.show(
        uid="4a5d882a-5568-2c3b-aa78-751ab23d6c11"
    )

    assert resp.uid == "4a5d882a-5568-2c3b-aa78-751ab23d6c11"
    assert resp.name == "cluster1"
    assert resp.ipv4_address == "17.23.5.1"


@responses.activate
def test_set_simple_cluster(firewallManagement, resp_task):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-simple-cluster",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.set(
        uid="4a5d882a-5568-2c3b-aa78-751ab23d6c11", ip_address="17.23.5.1"
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_delete_simple_cluster(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-simple-cluster",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.delete(
        uid="4a5d882a-5568-2c3b-aa78-751ab23d6c11"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_simple_clusters(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-simple-clusters",
        json=resp_from_to_objects,
        status=200,
    )

    resp = firewallManagement.network_objects.simple_cluster.show_simple_clusters()

    assert isinstance(resp.total, int)
