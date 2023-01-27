def test_tests_are_running():
    assert True


def test_get_points(client, db_session):
    response = client.get("/api/v1/points")
    assert response.status_code == 200, response.text
