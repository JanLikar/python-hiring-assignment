from assignment import get_popular_repos


def test_get_popular_repos():
    assert get_popular_repos("Foo") == []
