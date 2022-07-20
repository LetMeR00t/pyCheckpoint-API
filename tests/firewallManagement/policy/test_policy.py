import responses


@responses.activate
def test_install_policy(firewallManagement, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/install-policy",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.policy.install_policy(
        policy_package="standard",
        access=True,
        threat_prevention=True,
        targets=["corporate-gateway"],
        qos=False,
        desktop_security=False,
        revision="the most recent revision",
    )

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"


@responses.activate
def test_verify_policy(firewallManagement, resp_task):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/verify-policy",
        json=resp_task,
        status=200,
    )

    resp = firewallManagement.policy.verify_policy(policy_package="standard")

    assert resp.task_id == "01234567-89ab-cdef-a930-8c37a59972b3"
