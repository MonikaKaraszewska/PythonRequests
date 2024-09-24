import uuid

import requests
import pytest
endpoint = "https://todo.pixegami.io/"

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
