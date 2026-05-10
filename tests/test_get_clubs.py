from jsonschema import validate
from schemas.club_list_response_schema import club_list_response_schema


def test_get_clubs_response_matches_schema(client):
    response = client.get_clubs()
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=club_list_response_schema)


def test_get_clubs_pagination(client):
    response1 = client.get_clubs(params={"page": 1, "page_size": 2})
    response2 = client.get_clubs(params={"page": 2, "page_size": 2})

    assert response1.status_code == 200
    assert response2.status_code == 200

    page1 = response1.json()
    page2 = response2.json()

    assert 0 < len(page1["results"]) <= 2
    assert 0 < len(page2["results"]) <= 2

    assert page1["results"] != page2["results"]


def test_get_clubs_search_filter(client):
    search_value = "book"

    response = client.get_clubs(params={"search": search_value})
    data = response.json()
    results = data["results"]

    assert response.status_code == 200
    assert isinstance(results, list)

    for club in results:
        title = club["bookTitle"].lower()
        authors = club["bookAuthors"].lower()

        assert (
                search_value in title
                or search_value in authors
        )


@pytest.mark.parametrize(
    "params, expected_status",
    [
        ({"page": -1}, (400, 404)),
        ({"page_size": 0}, (400, 422)),
        ({"page_size": 100000}, (400, 422)),
        ({"search": "@@@###"}, 200),
        ({"membership": "unknown_value"}, (400, 422))
    ]
)
def test_get_clubs_invalid_query_params(client, params, expected_status):
    response = client.get_clubs(params=params)

    assert response.status_code in expected_status