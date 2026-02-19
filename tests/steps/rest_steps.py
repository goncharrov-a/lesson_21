import allure
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@allure.step("GET /posts/{post_id}")
def get_post(post_id: int) -> requests.Response:
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=20)
    return response


@allure.step("GET /posts?userId={user_id}")
def get_posts_by_user(user_id: int) -> requests.Response:
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id}, timeout=20)
    return response


@allure.step("POST /posts with title '{title}'")
def create_post(title: str, body: str, user_id: int) -> requests.Response:
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=20)
    allure.attach(str(payload), "payload", allure.attachment_type.TEXT)
    return response
