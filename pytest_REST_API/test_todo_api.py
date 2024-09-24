'''https://www.youtube.com/watch?v=7dgQRVqF1N0'''

import requests
import pytest
import uuid

endpoint = "https://todo.pixegami.io/"

response = requests.get(endpoint)
# print(response)
# print(response.text)

data = response.json()
# print(data)

def test_can_call_endpoint():
    response = requests.get(endpoint)
    assert response.status_code == 200

def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()

    task_id = data['task']['task_id']
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']
    assert get_task_data['is_done'] == payload['is_done']


def test_can_update_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    task_id = create_task_response.json()['task']['task_id']
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "UPDATE content",
        "is_done": True
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['is_done'] == new_payload['is_done']

def test_can_list_tasks():
    n=3
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    user_id = payload["user_id"]
    list_task_response = list_task(user_id)
    assert list_task_response.status_code == 200
    data= list_task_response.json()
    tasks = data['tasks']
    assert len(tasks) == n


def test_can_delete_task():
    payload = new_task_payload()
    create_new_task_to_delete = create_task(payload)
    assert create_new_task_to_delete.status_code ==200
    data_create_task_to_delete = create_new_task_to_delete.json()
    id_task_to_delete = data_create_task_to_delete['task']['user_id']
    deletion = delete_task(id_task_to_delete)
    assert deletion.status_code == 200
    get_task_deleted = get_task(id_task_to_delete)
    assert get_task_deleted.status_code == 404


def create_task(payload):
    return requests.put(endpoint + "/create-task", json=payload)


def update_task(payload,):
    return requests.put(endpoint + "/update-task", json=payload)

def get_task(task_id):
    return requests.get(endpoint + f"/get-task/{task_id}")


def list_task(user_id):
    return requests.get(endpoint + f"/list-tasks/{user_id}")

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }
def delete_task(task_id):
    return requests.delete(endpoint + f"/delete-task/{task_id}")