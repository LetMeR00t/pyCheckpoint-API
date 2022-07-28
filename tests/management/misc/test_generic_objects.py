import responses


@responses.activate
def test_get_rulebaseactions(management, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-generic-objects",
        json=resp_from_to_objects,
        status=200,
    )

    resp = management.misc.generic_objects.get_rulebaseactions()

    assert isinstance(resp.total, int)
