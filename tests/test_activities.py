def test_get_activities_returns_activity_details(client):
    # Arrange
    expected_activity = "Chess Club"
    expected_fields = {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert expected_activity in activities
    assert expected_fields <= activities[expected_activity].keys()
    assert isinstance(activities[expected_activity]["participants"], list)


def test_get_activities_returns_all_configured_activities(client):
    # Arrange
    expected_activity_count = 15

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == expected_activity_count
