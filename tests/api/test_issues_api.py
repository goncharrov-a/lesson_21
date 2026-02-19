import allure
import pytest

from tests.marks import jira_issues, layer, microservice, owner, tm4j
from tests.steps import rest_steps as steps

pytestmark = [
    layer("rest"),
    owner("goncharov"),
    allure.feature("Posts API"),
    pytest.mark.api,
]


@tm4j("AE-T1")
@jira_issues("AE-101")
@microservice("Content")
@allure.story("Get post by id")
@allure.title("Should return single post by id")
@pytest.mark.smoke
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id(post_id):
    response = steps.get_post(post_id)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == post_id
    assert "title" in body
    assert "body" in body
    assert "userId" in body


@tm4j("AE-T2")
@jira_issues("AE-102")
@microservice("Content")
@allure.story("Get posts by user")
@allure.title("Should return list of posts for selected user")
@pytest.mark.regress
@pytest.mark.parametrize("user_id", [1, 5])
def test_get_posts_by_user(user_id):
    response = steps.get_posts_by_user(user_id)

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert all(item["userId"] == user_id for item in posts)


@tm4j("AE-T3")
@jira_issues("AE-103")
@microservice("Content")
@allure.story("Create post")
@allure.title("Should create new post")
@pytest.mark.critical
@pytest.mark.parametrize(
    "title, body, user_id",
    [
        ("First API Note", "Body for first note", 11),
        ("Second API Note", "Body for second note", 22),
    ],
)
def test_create_post(title, body, user_id):
    response = steps.create_post(title, body, user_id)

    assert response.status_code == 201
    payload = response.json()
    assert payload["title"] == title
    assert payload["body"] == body
    assert payload["userId"] == user_id
    assert "id" in payload


@tm4j("AE-T4")
@jira_issues("AE-104")
@microservice("Content")
@allure.story("Negative check for demo defect")
@allure.title("Should fail to demonstrate defect in Allure")
@pytest.mark.regress
def test_demo_defect_for_allure():
    response = steps.get_post(1)

    assert response.status_code == 404
